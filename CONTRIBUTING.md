# Contributing Guide

기여해 주셔서 감사합니다. 이 프로젝트의 모든 참여자는 [행동강령](CODE_OF_CONDUCT.md)을 지켜야 합니다.
이 프로젝트에 기여한 내용은 [MIT License](LICENSE)로 배포됩니다.

## 기여하는 방법
- 버그나 제안: [Issues](https://github.com/ParkJongHwan517/donga_oss/issues)에 남깁니다. (템플릿 사용)
- 질문이나 아이디어: [Discussions](https://github.com/ParkJongHwan517/donga_oss/discussions)에서 이야기합니다.
- 코드나 문서 수정: 아래 브랜치 전략과 PR 절차를 따릅니다.
- 처음이라면 [Wiki의 Getting Started](https://github.com/ParkJongHwan517/donga_oss/wiki/Getting-Started)부터 읽으세요.

## 로컬에서 검사하기
PR을 올리기 전에 CI와 같은 검사를 직접 실행할 수 있습니다.

```bash
python -m pip install -r requirements-dev.txt
ruff check .          # lint
ruff format --check . # 포맷
python -m pytest      # 테스트
```
GitHub Actions의 `CI` 워크플로우가 PR마다 같은 검사를 Python 3.10~3.13, Ubuntu/Windows/macOS 조합에서 실행합니다.

## 브랜치 전략 (Feature Branch)
- `main`: 항상 배포 가능한 상태. 직접 push 금지, PR로만 병합.
- 작업마다 `main`에서 브랜치를 새로 만든다.

| 접두사 | 용도 | 예시 |
|---|---|---|
| `feat/` | 새 기능 | `feat/size-compare` |
| `fix/` | 버그 수정 | `fix/null-size-error` |
| `docs/` | 문서 | `docs/contributing-review-guide` |
| `chore/` | 설정, 빌드, 기타 | `chore/pr-template-codeowners` |
| `refactor/` | 리팩터링 | `refactor/parser` |

## 커밋 메시지 (Conventional Commits)
```
<type>(<scope>): <설명>

[본문]
```
- type: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- 제목은 50자 이내, 명령형/현재형, 끝에 마침표 없음
- 예: `feat(compare): 기준 옷 대비 허리 차이 계산 추가`

## PR 절차
1. 이슈 생성 (선택)
2. 브랜치 생성 후 작업, Conventional Commits로 커밋
3. push 후 PR 생성 (PR 템플릿 작성)
4. 리뷰 진행 — 리뷰 규칙은 [REVIEW_GUIDE.md](REVIEW_GUIDE.md) 참고
5. 모든 [MUST] 해결 + 승인 후 Squash merge
6. 병합된 브랜치 삭제

## 브랜치 보호 규칙 (main)
- PR 없이 push 금지
- 병합 전 PR 생성 필수 (개인 레포: 승인 수 0, 셀프 리뷰 후 병합)
- 대화(코멘트) 해결 후 병합
