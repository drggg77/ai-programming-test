# 성적 관리 프로그램

## ① 무엇을 하나요 (What)
성적 CSV 파일을 읽어 유효한 데이터만 골라 내고, pytest 자동화 테스트와 커버리지로 동작을 검증합니다.

## ② 왜 만들었나요 (Why)
실제 CSV 파일에는 빈 줄, 잘못된 형식, 점수 범위 초과, 중복 이름 등이 섞여 있어 이를 걸러 내고 회귀를 막기 위해서입니다.

## ③ 어떻게 쓰나요 (How)
```bash
python load_scores.py scores.csv
```

## ④ 어떻게 테스트하나요
```bash
python -m pytest test_load_scores.py
python -m pytest --cov=load_scores --cov-report term-missing
```

실행 결과:
- `test_load_scores.py` 단독 실행: `11 passed` (커버리지 76%)[cite: 17]
- 전체 테스트 실행: `23 passed in 0.24s` (`load_scores.py` 커버리지 80%, 미실행 구간 `77-86`)[cite: 17]

## ⑤ 파일 구성
| 파일 | 하는 일 |
| --- | --- |
| `load_scores.py` | 성적 CSV를 읽고 유효성 및 예외를 처리하는 핵심 로직 |
| `test_load_scores.py` | 직접 설계·작성한 정상/예외/경계값 테스트 코드 |
| `test_ai_A.py` | 전체 코드를 바탕으로 AI가 생성한 테스트 코드 |
| `test_ai_B.py` | 명세를 바탕으로 AI가 생성한 테스트 코드 |
| `bug3_logic.py` | AI 테스트/검증 실험용 파일 |

## ⑥ 만든 사람 · AI를 어디에 썼는지
- 만든 사람: 이호재 (2026100364)
- AI를 쓴 곳: 테스트 케이스 초안 생성 및 비교표 구성 보조.
- 내가 직접 판단한 것: 테스트 실행 결과(O/X) 확인, `pytest-cov` 커버리지 측정 및 누락 구간 원인 분석, 최종 문서·커밋 정리.
- AI 출력을 그대로 믿지 않고 검증한 점: AI가 작성한 테스트의 실제 실행 여부와 커버리지 수치를 터미널로 직접 확인하고 비교표에 반영함.