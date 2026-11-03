> **1부 텍스트 게임으로 문제 바라보기** · 1차시 · 6단계 모형: **문제 발견**  
> 게임: 업다운 · 가위바위보 · 기억력 게임 체험  
> 핵심 개념: 알고리즘, 프로그램, 입력-처리-출력, print(), 문자열

## 학습 목표

1. 파이썬 개발 환경에서 .py 파일을 실행할 수 있다.
2. print() 함수로 원하는 문장을 출력할 수 있다.
3. 익숙한 게임의 규칙을 입력–처리–출력(IPO)으로 분석할 수 있다.

## 핵심 질문

> **우리가 늘 하던 놀이(게임)의 규칙을 컴퓨터는 어떻게 알고 있을까?**

업다운 게임을 친구와 해 본 적이 있나요? 한 사람이 1~100 사이 숫자를 생각하고, 다른 사람이 맞힐 때까지 "더 커!", "더 작아!"라고 알려 주는 게임입니다.

이 게임을 컴퓨터와 하려면 컴퓨터에게 **순서대로, 빠짐없이, 모호하지 않게** 규칙을 알려 주어야 합니다. 이렇게 문제를 해결하는 절차를 **알고리즘**이라 하고, 알고리즘을 컴퓨터가 이해하는 언어로 적은 것을 **프로그램**이라고 합니다.

이번 시간에는 완성된 텍스트 게임 3개를 직접 실행해 보고, 그 안에 숨어 있는 규칙(알고리즘)을 찾아봅니다.

## 파이썬 프로그램 실행하기

1. [00-2. 개발 환경 준비하기] 페이지를 참고해 파이썬과 편집기(IDLE 또는 VS Code)를 준비합니다.
2. 소스코드 파일(`01_updown_basic.py`)을 내려받아 편집기로 엽니다.
3. IDLE은 **F5**, VS Code는 오른쪽 위 **▶ 실행** 버튼을 누릅니다.

터미널에서 직접 실행할 수도 있습니다.

```bash
python 01_updown_basic.py
```

## 첫 번째 코드: print()

`print()`는 괄호 안의 내용을 화면에 출력하는 **함수**입니다. 따옴표로 감싼 글자 묶음을 **문자열(string)** 이라고 합니다.

```python
print("=== 업다운 ===")                 # 문자열 출력
print("1~100 사이의 숫자를 맞혀 보세요!")
print("기회는", 7, "번")                 # 쉼표로 여러 값 출력 (사이에 공백)
print("=" * 20)                          # 문자열 * 정수 → 반복
```

실행 결과

```text
=== 업다운 ===
1~100 사이의 숫자를 맞혀 보세요!
기회는 7 번
====================
```

`#` 뒤의 내용은 **주석**입니다. 컴퓨터는 무시하고, 사람이 읽기 위한 설명입니다.

## 게임 속 입력–처리–출력 찾기

모든 프로그램은 **입력(Input) → 처리(Process) → 출력(Output)** 구조로 바라볼 수 있습니다.

| 게임 | 입력 (사용자가 하는 일) | 처리 (컴퓨터가 판단하는 일) | 출력 (보여 주는 것) | 종료 조건 |
| --- | --- | --- | --- | --- |
| 업다운 | 1~100 사이 숫자 | 정답과 비교해 크다/작다/같다 판단 | UP / DOWN / 정답 | 정답 또는 기회 7회 소진 |
| 가위바위보 | 가위·바위·보 중 하나 | 컴퓨터 선택과 비교해 승패 판단 | 이김 / 짐 / 비김, 점수 | 한쪽이 먼저 2승 |
| 기억력 게임 | 본 숫자를 순서대로 입력 | 보여 준 숫자와 같은지 비교 | 정답 / 오답, 라운드 수 | 한 번이라도 틀림 |

이 표가 바로 앞으로 우리가 코드로 옮길 **설계도의 첫 단계**입니다.

## 코드 살짝 엿보기

업다운 게임 코드의 핵심 부분입니다. 아직 몰라도 괜찮습니다. 어떤 줄이 입력·처리·출력인지 찾아만 보세요.

```python
text = input(f"[{low}~{high}] 남은 기회 {chance}회 > ")   # 입력
guess = int(text)
if guess == secret:                                        # 처리 (판단)
    print("정답!")                                         # 출력
elif guess < secret:
    print("UP! 더 큰 수예요.")
else:
    print("DOWN! 더 작은 수예요.")
```

- `input()` : 사용자에게 입력을 받는 함수 → **입력**
- `if / elif / else` : 조건에 따라 다른 일을 하는 문장 → **처리**
- `print()` : 결과를 보여 주는 함수 → **출력**

## 실습 활동

1. `print()`를 이용해 우리 모둠의 게임 제목 화면(3줄 이상)을 출력해 보세요.
2. 업다운 게임을 3번 해 보고, 가장 적은 횟수로 맞히는 **나만의 전략**을 한 문장으로 적어 보세요.
3. 세 게임에 공통으로 쓰인 요소(반복, 조건, 기록 등)를 찾아 활동지에 적어 보세요.

활동지: [ws01-play-algorithm.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws01-play-algorithm.md)

## 확인 퀴즈

**Q1.** 문제를 해결하기 위한 절차를 순서대로 명확하게 나타낸 것은?

- ① 프로그램
- ② 알고리즘
- ③ 컴파일러
- ④ 운영체제

**Q2.** `print("=" * 3)`의 실행 결과는?

- ① = * 3
- ② ===
- ③ 3
- ④ 오류 발생

**Q3.** 업다운 게임에서 '정답과 비교하여 크다/작다를 판단'하는 것은 IPO 중 무엇인가?

- ① 입력
- ② 처리
- ③ 출력
- ④ 저장

**Q4.** 파이썬에서 주석을 시작하는 기호는?

- ① //
- ② /*
- ③ #
- ④ --

**Q5.** `print("기회는", 7, "번")`의 출력으로 옳은 것은?

- ① 기회는7번
- ② 기회는 7 번
- ③ "기회는" 7 "번"
- ④ 기회는, 7, 번

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 게임 타이틀 화면 출력 (기본)

아래와 똑같이 출력하는 프로그램을 작성하세요. 첫 줄과 마지막 줄은 `=` 20개입니다.

- 입력: 없음
- 출력: 세 줄의 타이틀 화면

예제 입력 1

```text
(입력 없음)
```

예제 출력 1

```text
====================
   UP & DOWN GAME
====================
```

### 문제 2. 플레이어 환영 인사 (도전)

플레이어 이름을 한 줄 입력받아 `○○님, 게임을 시작합니다!`를 출력하세요. (`input()`은 다음 차시에 자세히 배웁니다.)

- 입력: 첫째 줄에 이름이 주어진다.
- 출력: 환영 문구를 출력한다.

예제 입력 1

```text
동균
```

예제 출력 1

```text
동균님, 게임을 시작합니다!
```

예제 입력 2

```text
Alex
```

예제 출력 2

```text
Alex님, 게임을 시작합니다!
```

정답과 해설은 **[부록] 06-1-01. 1차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-01-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 알고리즘 = 문제 해결 절차, 프로그램 = 알고리즘을 코드로 표현한 것
- 모든 게임은 입력 → 처리 → 출력 구조로 분석할 수 있다.
- `print()`는 출력, `#`은 주석, `"문자열" * n`은 반복

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `01_updown_basic.py` | [01_updown_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/01_updown_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/01_updown_basic.py) |
| 소스코드 `02_rps_basic.py` | [02_rps_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/02_rps_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/02_rps_basic.py) |
| 소스코드 `04_memory_basic.py` | [04_memory_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/04_memory_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/04_memory_basic.py) |
| 학습용 PPT | [01-play-algorithm.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/01-play-algorithm.pptx) |
| 학생 활동지 | [ws01-play-algorithm.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws01-play-algorithm.md) |
| 코딩 테스트 1 정답 코드 | [ch01_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch01_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch01_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch01_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch01_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch01_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
