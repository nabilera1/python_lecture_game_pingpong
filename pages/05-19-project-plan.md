> **5부 테스트·프로젝트·공유** · 19차시 · 6단계 모형: **공유·확장**  
> 게임: 프로젝트 계획서 · 순서도 · 클래스 구조도  
> 핵심 개념: 프로젝트 계획서, 요구사항, 기능 목록, 우선순위, 순서도, 클래스 구조도, 상태

## 학습 목표

1. 배운 게임 중 하나를 골라 개선하거나 새 게임을 기획할 수 있다.
2. 기능 목록을 입력·처리·출력과 하위 문제로 분해하여 계획서를 작성할 수 있다.
3. 순서도·함수 설계표·클래스 구조도(차트)로 프로그램을 설계할 수 있다.

## 핵심 질문

> **지금까지 배운 6단계를 내 힘으로 다시 밟으려면 무엇부터 계획해야 할까?**

이제 **문제 발견 → 구조화 → 설계 → 구현 → 테스트 → 공유**의 6단계를 모둠이 스스로 진행합니다. 오늘은 계획서와 설계 차트를 완성하는 날입니다. 좋은 계획서는 **'무엇을 만들지'뿐 아니라 '어떻게 확인할지'까지** 적혀 있습니다.

## 프로젝트 주제 고르기

| 유형 | 예시 | 난이도 |
| --- | --- | --- |
| 텍스트 게임 개선 | 업다운 난이도 선택 + 최고 기록 파일 저장, 행맨 카테고리 추가 | ★★ |
| 텍스트 게임 새로 만들기 | 끝말잇기, 퀴즈 게임, 숫자 맞히기 대결(2인) | ★★ |
| 핑퐁 게임 확장 | 공 가속, 컴퓨터 상대(AI 패들), 난이도, 일시정지, 효과음 | ★★★ |
| 던전 탈출 확장 | 새 몬스터·아이템, 층(레벨) 추가, 점수 순위표 | ★★★ |

선택 기준: **2차원 리스트 또는 딕셔너리를 의미 있게 사용**할 수 있는가? (수행평가 '다차원 데이터 구조의 적용' 요소와 연결)

## 계획서 핵심 항목

| 항목 | 작성 내용 | 예시 (핑퐁 AI 상대 모드) |
| --- | --- | --- |
| 문제 정의 | 누구의 어떤 불편/재미를 위해? | 혼자서도 핑퐁을 즐기고 싶다 |
| 입력–처리–출력 | IPO 표 | 입력: W/S, 처리: AI 패들이 공을 따라감, 출력: 화면 |
| 기능 목록 + 우선순위 | 꼭(必) / 있으면 좋음 | 必 AI 패들, 必 난이도 3단계, 좋음: 효과음 |
| 데이터 구조 | 변수·리스트·딕셔너리·2차원 리스트 | `LEVELS = {"쉬움": 3, "보통": 5, "어려움": 7}` |
| 함수/클래스 설계 | 이름·매개변수·반환값·역할 | `AIPaddle.follow(ball)` |
| 테스트 계획 | 정상·경계·예외 케이스 | 공이 맨 위에 있을 때 AI 패들이 화면 밖으로 안 나가나? |
| 역할 분담·일정 | 드라이버/내비게이터, 20~22차시 일정 | 20차시 구현, 21차시 테스트 |

## 차트로 설계하기

**순서도**는 흐름을, **클래스 구조도**는 '누가 무엇을 가지고 무엇을 하는지'를 보여 줍니다.

```text
┌──────────── AIPaddle (Paddle 확장) ───────────┐
│ 속성: rect, color, speed, level               │
│ 메서드: follow(ball) - 공의 y를 따라 이동       │
│        draw(screen)                           │
└───────────────────────────────────────────────┘
```

**상태(state)** 로 게임 흐름을 설계하는 방법도 있습니다.

```text
 [준비] ──스페이스──▶ [진행] ──5점 도달──▶ [종료]
   ▲                 P │ ▲ P              │ R
   │                   ▼ │                │
   │                 [일시정지]            │
   └──────────────────────────────────────┘
```

진행 중 P를 누르면 일시정지, 일시정지에서 다시 P를 누르면 진행으로 돌아갑니다.

이 차트는 평가 요소 '**차트 작성**'의 근거가 됩니다. 구현이 끝난 뒤 실제 코드와 차트가 일치하는지 확인합니다.

## 딕셔너리로 설정 묶기

```python
LEVELS = {
    "쉬움":   {"ball_speed": 4, "ai_speed": 3},
    "보통":   {"ball_speed": 6, "ai_speed": 5},
    "어려움": {"ball_speed": 8, "ai_speed": 7},
}
level = LEVELS["보통"]
print(level["ball_speed"])    # 6  ← 딕셔너리 안의 딕셔너리(중첩)
```

## 실습 활동

1. 모둠별 프로젝트 주제를 정하고 계획서(활동지)를 작성하세요.
2. 핵심 기능 하나의 순서도와 전체 클래스(또는 함수) 구조도를 그리세요.
3. 테스트 계획을 정상·경계·예외로 3개 이상 미리 적어 두세요.

활동지: [ws19-project-plan.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws19-project-plan.md)

## 확인 퀴즈

**Q1.** 프로젝트 계획서에 '테스트 계획'을 미리 쓰는 이유로 가장 알맞은 것은?

- ① 분량을 늘리려고
- ② 완성 기준을 미리 정해 구현 방향을 잡으려고
- ③ 선생님이 시켜서
- ④ 코드를 짧게 하려고

**Q2.** 기능 목록에서 우선순위를 정하는 가장 큰 이유는?

- ① 멋있어 보여서
- ② 주어진 시간 안에 꼭 필요한 기능부터 완성하려고
- ③ 코드를 길게 하려고
- ④ 모두 동시에 하려고

**Q3.** '준비 → 진행 → 종료'처럼 게임의 흐름을 나타내는 설계 방법은?

- ① 상태 다이어그램
- ② 판정표
- ③ 추적표
- ④ IPO 표

**Q4.** `LEVELS = {"쉬움": {"speed": 4}}`에서 4를 꺼내는 코드는?

- ① LEVELS["speed"]
- ② LEVELS["쉬움"]["speed"]
- ③ LEVELS[0][0]
- ④ LEVELS.speed

**Q5.** 클래스 구조도에 반드시 들어가야 하는 것은?

- ① 실행 화면 사진
- ② 속성과 메서드
- ③ 글꼴 이름
- ④ 파일 크기

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 난이도 설정 불러오기 (기본)

코드 안에 `LEVELS = {"쉬움": [4, 3], "보통": [6, 5], "어려움": [8, 7]}`(공 속도, AI 속도)를 두세요. 난이도 이름을 입력받아 `공 속도 ○, AI 속도 ○`를 출력하고, 없는 이름이면 `보통` 설정을 사용하되 첫 줄에 `알 수 없는 난이도: 보통으로 설정`을 출력하세요.

- 입력: 난이도 이름
- 출력: 설정값

예제 입력 1

```text
어려움
```

예제 출력 1

```text
공 속도 8, AI 속도 7
```

예제 입력 2

```text
지옥
```

예제 출력 2

```text
알 수 없는 난이도: 보통으로 설정
공 속도 6, AI 속도 5
```

### 문제 2. 게임 상태 전환기 (도전)

게임 상태는 `준비`에서 시작합니다. 명령 문자열의 글자마다 다음 규칙으로 상태를 바꾸고, 바뀔 때마다(바뀌지 않으면 출력 없음) 새 상태를 출력하세요. 규칙: 준비에서 S → 진행 / 진행에서 P → 일시정지 / 일시정지에서 P → 진행 / 진행에서 W → 종료 / 종료에서 R → 준비. 그 밖의 명령은 무시합니다.

- 입력: 명령 문자열 (S, P, W, R 등)
- 출력: 바뀐 상태들

예제 입력 1

```text
SPPWR
```

예제 출력 1

```text
진행
일시정지
진행
종료
준비
```

예제 입력 2

```text
PSWWS
```

예제 출력 2

```text
진행
종료
```

정답과 해설은 **[부록] 06-1-19. 19차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-19-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 6단계를 모둠이 스스로: 오늘은 기획·설계
- 계획서 = 문제 정의 + IPO + 기능(우선순위) + 데이터 + 설계 + 테스트 계획
- 차트: 순서도, 클래스 구조도, 상태 다이어그램
- 설정과 규칙은 딕셔너리로 묶기

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `game.py` | [game.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/game.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/game.py) |
| 소스코드 `08_rps_table.py` | [08_rps_table.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/08_rps_table.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/08_rps_table.py) |
| 학습용 PPT | [19-project-plan.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/19-project-plan.pptx) |
| 학생 활동지 | [ws19-project-plan.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws19-project-plan.md) |
| 코딩 테스트 1 정답 코드 | [ch19_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch19_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch19_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch19_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch19_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch19_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
