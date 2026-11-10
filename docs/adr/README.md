# Architecture Decision Records (ADR)

프로젝트의 **중요한 기술 결정**과 그 이유를 짧은 문서로 남기는 곳입니다.
코드만 봐서는 알 수 없는 "왜 이렇게 했는가"를 기록해 두기 위한 것입니다.

## 언제 쓰나
- 기술 스택, 프레임워크, DB 같은 선택을 할 때
- 협업 방식이나 구조를 바꿀 때
- 나중에 "왜 이렇게 했지?"라는 질문이 나올 만한 결정을 할 때

## 작성 방법
1. [`0000-template.md`](0000-template.md)를 복사해 `NNNN-짧은-제목.md`로 저장합니다. (번호는 순서대로)
2. Status를 `Proposed`로 두고 PR을 올립니다.
3. 리뷰를 거쳐 병합하면 `Accepted`로 바꿉니다.
4. 결정이 바뀌면 기존 문서를 지우지 않고 `Superseded by ADR-NNNN`으로 표시하고 새 ADR을 씁니다.

## Status 값
| 상태 | 의미 |
|---|---|
| Proposed | 제안됨, 논의 중 |
| Accepted | 채택됨 |
| Deprecated | 더 이상 사용하지 않음 |
| Superseded | 다른 ADR로 대체됨 |

## 목록
| 번호 | 제목 | 상태 |
|---|---|---|
| [0001](0001-use-fastapi-and-supabase.md) | 백엔드로 FastAPI와 Supabase를 사용한다 | Accepted |
| [0002](0002-adopt-feature-branch-workflow.md) | Feature 브랜치 전략과 Conventional Commits를 사용한다 | Accepted |

관련: 큰 변경은 먼저 GitHub Discussions의 RFC 카테고리에서 논의하고, 결론이 나면 ADR로 남깁니다.
