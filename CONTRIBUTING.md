# Contributing Guide

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
- 병합 전 리뷰 승인 필요
- 대화(코멘트) 해결 후 병합
