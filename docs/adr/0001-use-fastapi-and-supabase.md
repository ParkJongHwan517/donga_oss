# ADR-0001: 백엔드로 FastAPI와 Supabase를 사용한다

- **상태**: Accepted
- **날짜**: 2026-11-10
- **결정자**: @ParkJongHwan517
- **관련**: [README 기술스택](../../README.md)

## 배경 (Context)
FIT은 사용자의 Reference outFit과 상품 실측 정보를 저장하고 비교하는 서비스다.
12주 안에 혼자 개발해야 하므로 인증, DB 같은 공통 기능을 직접 만드는 비용을 줄여야 한다.
프런트엔드는 HTML/CSS/JavaScript로 시작하고, 수치 비교 로직은 서버에서 처리한다.

## 결정 (Decision)
- 백엔드 API는 **Python + FastAPI**로 만든다.
- 데이터베이스와 인증은 **Supabase**(PostgreSQL 기반)를 사용한다.

## 대안 (Alternatives)
| 대안 | 장점 | 단점 |
|---|---|---|
| Django + 자체 PostgreSQL | 기능이 풍부함 | 설정과 인증 구현 비용이 큼 |
| Node.js(Express) + Firebase | 프런트와 언어 통일 | 관계형 데이터(옷-실측-상품)에 덜 적합 |
| FastAPI + SQLite | 가장 단순함 | 인증, 배포, 다중 사용자 지원을 직접 해야 함 |

## 결과 (Consequences)
- 좋아지는 점: 회원가입/로그인을 Supabase Auth로 빠르게 구현하고, FastAPI의 자동 문서(`/docs`)로 API를 확인할 수 있다.
- 감수해야 할 점: Supabase 서비스에 의존하며, 키 관리(`.env`)에 주의해야 한다.
- 앞으로 해야 할 일: Week 2에 FastAPI와 Supabase 연동을 구현한다.
