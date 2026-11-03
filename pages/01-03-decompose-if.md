> **1부 텍스트 게임으로 문제 바라보기** · 3차시 · 6단계 모형: **문제 구조화**  
> 게임: 업다운 판정 · 가위바위보 판정  
> 핵심 개념: 분해, 비교 연산자, 논리 연산자, if, elif, else

## 학습 목표

1. 게임 규칙을 작은 하위 문제로 분해하여 분해 트리로 나타낼 수 있다.
2. 비교 연산자와 논리 연산자의 결과(True/False)를 설명할 수 있다.
3. if–elif–else 문으로 여러 경우를 판정하는 프로그램을 작성할 수 있다.

## 핵심 질문

> **게임 규칙을 어떤 작은 문제로 나누어야 컴퓨터가 판단할 수 있을까?**

큰 문제는 한 번에 풀기 어렵습니다. 업다운 게임도 **① 정답 정하기 ② 숫자 입력받기 ③ 판정하기 ④ 기회 줄이기 ⑤ 끝났는지 확인하기**처럼 작은 문제로 나누면 하나씩 해결할 수 있습니다. 이것을 **분해**라고 합니다.

오늘은 그중 가장 중요한 ③ **판정하기**를 조건문으로 만들어 봅니다.

## 분해 트리 그리기

```text
업다운 게임
├── 준비하기 : 정답 고르기, 기회 7번, 범위 1~100
├── 한 번 시도하기
│   ├── 숫자 입력받기 (숫자가 맞는지 검사)
│   ├── 판정하기 : 정답 / UP / DOWN      ← 오늘의 주제
│   └── 기회 1 줄이기, 범위 좁히기
└── 끝내기 : 정답이면 성공, 기회가 0이면 실패
```

하위 문제 하나하나가 나중에 **코드 몇 줄** 또는 **함수 하나**가 됩니다.

## 비교 연산자와 논리 연산자

비교의 결과는 항상 `True`(참) 또는 `False`(거짓)입니다.

| 연산자 | 의미 | 예시 (`guess = 30`, `secret = 50`) | 결과 |
| --- | --- | --- | --- |
| `==` | 같다 | `guess == secret` | `False` |
| `!=` | 다르다 | `guess != secret` | `True` |
| `<` `>` | 작다 / 크다 | `guess < secret` | `True` |
| `<=` `>=` | 작거나 같다 / 크거나 같다 | `guess >= 30` | `True` |

| 논리 연산자 | 의미 | 예시 | 결과 |
| --- | --- | --- | --- |
| `and` | 둘 다 참이면 참 | `1 <= guess and guess <= 100` | `True` |
| `or` | 하나라도 참이면 참 | `guess < 1 or guess > 100` | `False` |
| `not` | 참↔거짓 반대 | `not True` | `False` |

파이썬은 `1 <= guess <= 100`처럼 비교를 이어 쓸 수도 있습니다. `=`(대입)와 `==`(비교)를 헷갈리지 마세요!

## if – elif – else

```python
guess = int(input("숫자 > "))
secret = 50

if guess == secret:          # ① 먼저 검사
    print("정답!")
elif guess < secret:         # ② ①이 거짓일 때만 검사
    print("UP! 더 큰 수예요.")
else:                        # ③ 위의 모든 조건이 거짓이면
    print("DOWN! 더 작은 수예요.")
```

- 위에서부터 차례로 검사하고, **처음으로 참인 블록 하나만** 실행합니다.
- 조건 뒤에는 반드시 콜론 `:`, 실행할 문장은 **들여쓰기(공백 4칸)** 합니다.

## 가위바위보 판정을 수학으로

가위바위보 승패를 `if`로 모두 따지면 9가지 경우가 필요합니다. 리스트 번호와 **나머지 연산**을 쓰면 한 줄로 판정할 수 있습니다. (다음 시간에 자세히!)

```python
choices = ["가위", "바위", "보"]          # 번호 0, 1, 2
diff = (choices.index(pick) - choices.index(cpu)) % 3
# diff 가 0 → 비김, 1 → 이김, 2 → 짐
```

| 나 \ 컴퓨터 | 가위(0) | 바위(1) | 보(2) |
| --- | --- | --- | --- |
| 가위(0) | 0 비김 | 2 짐 | 1 이김 |
| 바위(1) | 1 이김 | 0 비김 | 2 짐 |
| 보(2) | 2 짐 | 1 이김 | 0 비김 |

## 실습 활동

1. 우리 모둠 게임의 분해 트리를 활동지에 그려 보세요.
2. 점수를 입력받아 90 이상 A, 80 이상 B, 70 이상 C, 60 이상 D, 나머지 E를 출력해 보세요.
3. 위 판정 표에서 (나 - 컴퓨터) % 3 값이 맞는지 3칸 이상 직접 계산해 확인해 보세요.

활동지: [ws03-decompose-if.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws03-decompose-if.md)

## 확인 퀴즈

**Q1.** `guess = 30`일 때 `10 <= guess and guess < 30`의 결과는?

- ① True
- ② False
- ③ 30
- ④ 오류

**Q2.** 다음 중 '같다'를 비교하는 연산자는?

- ① =
- ② ==
- ③ ===
- ④ !=

**Q3.** `x = 85`일 때 출력은?

```python
if x >= 70:
    print("C")
elif x >= 80:
    print("B")
else:
    print("E")
```

- ① B
- ② C
- ③ B와 C
- ④ E

**Q4.** 복잡한 문제를 해결 가능한 작은 문제로 나누는 것은?

- ① 추상화
- ② 분해
- ③ 패턴 인식
- ④ 디버깅

**Q5.** `(0 - 2) % 3`의 값은? (나: 가위 0, 컴퓨터: 보 2)

- ① -2
- ② 0
- ③ 1
- ④ 2

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 업다운 한 번 판정 (기본)

정답 secret과 추측 guess를 입력받아 같으면 `정답`, guess가 작으면 `UP`, 크면 `DOWN`을 출력하세요.

- 입력: 첫째 줄에 secret, 둘째 줄에 guess (1~100 정수)
- 출력: 판정 결과를 출력한다.

예제 입력 1

```text
50
30
```

예제 출력 1

```text
UP
```

예제 입력 2

```text
50
70
```

예제 출력 2

```text
DOWN
```

예제 입력 3

```text
42
42
```

예제 출력 3

```text
정답
```

### 문제 2. 가위바위보 한 판 판정 (도전)

나와 컴퓨터의 선택(가위/바위/보)을 한 줄에 입력받아 나를 기준으로 `이김`, `짐`, `비김`을 출력하세요.

- 입력: 첫째 줄에 나의 선택과 컴퓨터의 선택이 공백으로 구분되어 주어진다.
- 출력: 결과를 출력한다.

예제 입력 1

```text
바위 가위
```

예제 출력 1

```text
이김
```

예제 입력 2

```text
가위 바위
```

예제 출력 2

```text
짐
```

예제 입력 3

```text
보 보
```

예제 출력 3

```text
비김
```

정답과 해설은 **[부록] 06-1-03. 3차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-03-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 분해: 게임 = 준비 + 시도(입력·판정·갱신) + 종료
- 비교·논리 연산의 결과는 True / False
- if–elif–else: 위에서부터 처음 참인 블록 하나만 실행
- 콜론 : 과 들여쓰기 4칸은 필수

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `01_updown_basic.py` | [01_updown_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/01_updown_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/01_updown_basic.py) |
| 소스코드 `02_rps_basic.py` | [02_rps_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/02_rps_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/02_rps_basic.py) |
| 학습용 PPT | [03-decompose-if.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/03-decompose-if.pptx) |
| 학생 활동지 | [ws03-decompose-if.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws03-decompose-if.md) |
| 코딩 테스트 1 정답 코드 | [ch03_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch03_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch03_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch03_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch03_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch03_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
