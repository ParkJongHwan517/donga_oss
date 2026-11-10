# ADR-0002: Feature 브랜치 전략과 Conventional Commits를 사용한다

- **상태**: Accepted
- **날짜**: 2026-11-10
- **결정자**: @ParkJongHwan517
- **관련**: PR #15, #16, [CONTRIBUTING.md](../../CONTRIBUTING.md), [REVIEW_GUIDE.md](../../REVIEW_GUIDE.md)

## 배경 (Context)
`main`에 직접 커밋하면 변경 이유와 검토 기록이 남지 않는다.
개인 프로젝트이지만 협업 방식을 익히고, 나중에 팀원이 합류해도 같은 규칙을 쓸 수 있어야 한다.

## 결정 (Decision)
- 작업마다 `main`에서 feature 브랜치(`feat/`, `fix/`, `docs/`, `chore/`)를 만들고 PR로만 병합한다.
- 커밋 메시지는 Conventional Commits를 따른다.
- PR 리뷰는 `[MUST]` / `[SHOULD]` 태그로 구조화한다.
- `main`에는 브랜치 보호 규칙(PR 필수)을 적용한다.

## 대안 (Alternatives)
| 대안 | 장점 | 단점 |
|---|---|---|
| `main`에 직접 커밋 | 빠름 | 이력과 리뷰가 남지 않음 |
| Git Flow(develop, release 브랜치) | 릴리스 관리가 체계적 | 개인 프로젝트에는 과함 |

## 결과 (Consequences)
- 좋아지는 점: 변경 단위가 PR로 남고, 커밋 이력이 일관된다.
- 감수해야 할 점: 작은 수정에도 브랜치와 PR 절차가 필요하다.
- 개인 레포라 승인 수는 0으로 두고 셀프 리뷰 후 병합한다.
