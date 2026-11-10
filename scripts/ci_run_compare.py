"""두 개의 CI 실행에서 의존성 설치 시간과 캐시 적중 여부를 비교한다.

Composite Action이 로그에 남기는 'Dependencies installed in Ns (cache-hit: ...)' 줄을 읽는다.

사용 예:
    python scripts/ci_run_compare.py --repo OWNER/REPO RUN_ID_BEFORE RUN_ID_AFTER
"""

from __future__ import annotations

import argparse
import re
import statistics
import subprocess
from collections import defaultdict

PATTERN = re.compile(r"Dependencies installed in (\d+)s \(cache-hit: '(\w*)'\)")


def platform(job_name: str) -> str:
    for name in ("windows", "macos"):
        if name in job_name:
            return name
    return "ubuntu"


def read_installs(repo: str, run_id: str) -> list[tuple[str, int, bool]]:
    log = subprocess.run(
        ["gh", "run", "view", run_id, "--repo", repo, "--log"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    ).stdout
    rows = []
    for line in log.splitlines():
        job, _, rest = line.partition("\t")
        match = PATTERN.search(rest)
        if match and "echo" not in rest:
            rows.append((platform(job), int(match.group(1)), match.group(2) == "true"))
    return rows


def summarize(rows: list[tuple[str, int, bool]]) -> dict[str, tuple[float, int, int]]:
    grouped: dict[str, list[tuple[int, bool]]] = defaultdict(list)
    for name, seconds, hit in rows:
        grouped[name].append((seconds, hit))
        grouped["all"].append((seconds, hit))
    return {
        name: (
            statistics.mean(s for s, _ in values),
            sum(1 for _, hit in values if hit),
            len(values),
        )
        for name, values in grouped.items()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("before")
    parser.add_argument("after")
    args = parser.parse_args()

    before = summarize(read_installs(args.repo, args.before))
    after = summarize(read_installs(args.repo, args.after))

    print("| 구분 | 이전 설치(초) | 이전 캐시 적중 | 이후 설치(초) | 이후 캐시 적중 | 변화 |")
    print("|---|---|---|---|---|---|")
    for name in ("ubuntu", "windows", "macos", "all"):
        if name not in before or name not in after:
            continue
        b_mean, b_hit, b_n = before[name]
        a_mean, a_hit, a_n = after[name]
        change = (b_mean - a_mean) / b_mean * 100 if b_mean else 0.0
        print(
            f"| {name} | {b_mean:.1f} | {b_hit}/{b_n} | {a_mean:.1f} | {a_hit}/{a_n} "
            f"| {change:+.1f}% |"
        )


if __name__ == "__main__":
    main()
