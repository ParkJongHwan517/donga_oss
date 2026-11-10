"""Cache Benchmark 실행 기록을 모아 평균과 개선률을 계산한다.

GitHub CLI(gh)로 완료된 실행의 잡/스텝 시간을 읽어서 마크다운 표를 출력한다.

사용 예:
    python scripts/cache_benchmark_report.py --repo OWNER/REPO --limit 3
"""

from __future__ import annotations

import argparse
import json
import statistics
import subprocess
from datetime import datetime

STEP_NAME = "Setup Python environment"
JOBS = ("no-cache", "cache-cold", "cache-warm")


def gh_json(*args: str) -> object:
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def seconds(start: str, end: str) -> float:
    fmt = start.replace("Z", "+00:00"), end.replace("Z", "+00:00")
    return (datetime.fromisoformat(fmt[1]) - datetime.fromisoformat(fmt[0])).total_seconds()


def collect(repo: str, workflow: str, limit: int) -> list[dict[str, dict[str, float]]]:
    runs = gh_json(
        "run", "list", "--repo", repo, "--workflow", workflow,
        "--status", "success", "--limit", str(limit), "--json", "databaseId",
    )  # fmt: skip
    results = []
    for run in runs:
        data = gh_json("api", f"repos/{repo}/actions/runs/{run['databaseId']}/jobs")
        per_job: dict[str, dict[str, float]] = {}
        for job in data["jobs"]:
            if job["name"] not in JOBS:
                continue
            step = next(s for s in job["steps"] if s["name"] == STEP_NAME)
            per_job[job["name"]] = {
                "prep": seconds(step["started_at"], step["completed_at"]),
                "job": seconds(job["started_at"], job["completed_at"]),
            }
        if set(per_job) == set(JOBS):
            results.append({"id": run["databaseId"], **per_job})
    return results


def gain(before: float, after: float) -> float:
    return (before - after) / before * 100 if before else 0.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--workflow", default="cache-benchmark.yml")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()

    results = collect(args.repo, args.workflow, args.limit)
    if not results:
        raise SystemExit("완료된 벤치마크 실행이 없습니다.")

    print("| 실행 | no-cache 준비(초) | cache-cold 준비(초) | cache-warm 준비(초) | 개선률(warm) |")
    print("|---|---|---|---|---|")
    for r in results:
        n, c, w = (r[j]["prep"] for j in JOBS)
        print(f"| #{r['id']} | {n:.0f} | {c:.0f} | {w:.0f} | {gain(n, w):.1f}% |")

    for key, label in (("prep", "환경 준비 단계"), ("job", "잡 전체")):
        mean = {j: statistics.mean(r[j][key] for r in results) for j in JOBS}
        base = mean["no-cache"]
        print()
        print(f"**{label} 평균** (n={len(results)})")
        print(f"- no-cache: {base:.1f}s")
        for name in ("cache-cold", "cache-warm"):
            print(f"- {name}: {mean[name]:.1f}s ({gain(base, mean[name]):.1f}%)")


if __name__ == "__main__":
    main()
