# GitHub Discussions 운영 가이드

이슈는 "해야 할 일(버그, 작업)"을, Discussions는 "논의와 질문"을 위한 곳입니다.

## 카테고리 설계

| 카테고리 | 형식 | 용도 | 예시 |
|---|---|---|---|
| 📣 Announcements | Announcement | 공지, 릴리스 소식 (관리자만 작성) | "v0.1 마일스톤 완료" |
| 💬 General | Open-ended | 자유로운 대화 | 프로젝트 방향 잡담 |
| ❓ Q&A | Question / Answer | 사용법, 오류 질문 (답변 채택 가능) | "Supabase 연결이 안 돼요" |
| 💡 Ideas | Open-ended | 기능 아이디어 | "상품 비교 화면에 그래프 추가" |
| 🗳️ Polls | Poll | 투표로 결정할 때 | "색상 테마 선택" |
| 📝 RFC | Open-ended | 큰 변경 제안과 토론 | "RFC: 핏 비교 결과 표시 방식" |

## RFC 진행 절차
1. **RFC** 카테고리에서 새 토론을 만든다. (양식: `.github/DISCUSSION_TEMPLATE/rfc.yml`)
2. 의견 수렴 기간(3일~2주) 동안 댓글로 논의한다.
3. 작성자가 결론을 요약해 댓글로 남기고, 토론을 마무리한다.
4. 채택된 결정은 [`docs/adr/`](adr/README.md)에 ADR로 기록한다.
5. 후속 작업은 이슈로 만들고 PR로 진행한다.

## 이슈와 Discussions 구분
| 상황 | 어디에 |
|---|---|
| 버그를 발견했다 | Issue (Bug report) |
| 만들고 싶은 기능이 정해졌다 | Issue (Feature request) |
| 방법을 모르겠다 | Discussions → Q&A |
| 방향이 정해지지 않은 아이디어 | Discussions → Ideas |
| 구조나 방식을 크게 바꾸고 싶다 | Discussions → RFC |
