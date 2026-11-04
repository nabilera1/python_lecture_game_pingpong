> **1부 텍스트 게임으로 문제 바라보기** · 2차시 · 6단계 모형: **문제 구조화**  
> 게임: 업다운 게임의 데이터 찾기  
> 핵심 개념: 추상화, 변수, 자료형, input(), 형 변환, 산술 연산자

## 학습 목표

1. 게임에 꼭 필요한 데이터를 골라내는 추상화를 할 수 있다.
2. 변수에 값을 저장하고, 정수·실수·문자열·불 자료형을 구분할 수 있다.
3. input()으로 입력받고 int()로 형 변환하여 계산할 수 있다.

## 핵심 질문

> **게임을 만들려면 컴퓨터가 무엇을 '기억'하고 있어야 할까?**

업다운 게임을 하는 동안 컴퓨터는 무엇을 기억하고 있어야 할까요? **정답 숫자, 남은 기회, 지금까지 입력한 숫자, 정답이 있을 수 있는 범위** 정도면 충분합니다. 화면 색깔이나 효과음은 규칙과 상관없으니 빼도 됩니다.

이처럼 문제에서 **핵심만 남기고 불필요한 것은 버리는 것**을 **추상화**라고 합니다. 추상화로 골라낸 데이터는 프로그램에서 **변수**에 저장합니다.

## 변수: 이름표를 붙인 상자

변수는 값을 저장하는 **이름표 붙은 상자**입니다. `=`는 "같다"가 아니라 **오른쪽 값을 왼쪽 상자에 넣어라(대입)** 라는 뜻입니다.

```python
secret = 37          # 정답
chance = 7           # 남은 기회
low, high = 1, 100   # 범위 (한 번에 두 변수에 대입)
chance = chance - 1  # 기존 값에서 1을 빼서 다시 저장 → 6
chance -= 1          # 위와 같은 뜻의 줄임 표현 → 5
```

변수 이름 규칙: 영문자·숫자·`_` 사용, 숫자로 시작 불가, 대소문자 구분, 예약어(`if`, `for` 등) 사용 불가

## 자료형: 값의 종류

| 자료형 | 예시 | 게임 속 사용 |
| --- | --- | --- |
| 정수 `int` | `7`, `-3`, `100` | 남은 기회, 점수 |
| 실수 `float` | `1.5`, `0.5` | 기억력 게임의 대기 시간 |
| 문자열 `str` | `"가위"`, `"UP!"` | 선택, 안내 문구 |
| 불 `bool` | `True`, `False` | 게임 진행 중인가? |

`type()` 함수로 자료형을 확인할 수 있습니다.

```python
print(type(7))       # <class 'int'>
print(type("7"))     # <class 'str'>  ← 따옴표가 있으면 문자열!
```

## input()과 형 변환

`input()`으로 받은 값은 **항상 문자열**입니다. 숫자로 계산하려면 `int()`로 바꿔야 합니다.

```python
text = input("숫자 > ")   # 50 을 입력하면 text 는 "50" (문자열)
guess = int(text)         # 50 (정수)
print(guess + 1)          # 51
print(text + "1")         # "501"  ← 문자열끼리 + 는 이어 붙이기!
```

입력 한 줄에 여러 값이 있을 때는 `split()`으로 나눕니다.

```python
a, b = map(int, input().split())   # "3 5" → a=3, b=5
```

## 산술 연산자

| 연산자 | 의미 | 예시 | 결과 |
| --- | --- | --- | --- |
| `+` `-` `*` | 더하기·빼기·곱하기 | `7 * 3` | `21` |
| `/` | 나누기 (결과는 실수) | `7 / 2` | `3.5` |
| `//` | 몫 | `7 // 2` | `3` |
| `%` | 나머지 | `7 % 2` | `1` |
| `**` | 거듭제곱 | `2 ** 7` | `128` |

핑퐁 게임에서 화면 가운데를 구할 때 `800 // 2 = 400`처럼 몫 연산을 씁니다. 픽셀 좌표는 정수여야 하기 때문입니다.

## 실습 활동

1. 업다운 게임에 필요한 데이터 4가지를 변수 이름과 자료형으로 정리해 보세요.
2. `print("3" * 3)`과 `print(3 * 3)`의 결과를 예상한 뒤 실행해 비교해 보세요.
3. `2 ** 7`의 값을 구하고, 업다운 게임의 기회가 왜 7번인지 추측해 보세요. (힌트: 범위를 매번 절반으로 줄이면? 7번이면 최대 2⁷ − 1 = 127개 중에서 찾을 수 있습니다.)

활동지: [ws02-variables-input.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws02-variables-input.md)

## 확인 퀴즈

**Q1.** 문제의 핵심 요소만 남기고 불필요한 부분을 제거하는 과정은?

- ① 분해
- ② 추상화
- ③ 자동화
- ④ 일반화

**Q2.** `x = input()`에 `10`을 입력했을 때 `x`의 자료형은?

- ① int
- ② float
- ③ str
- ④ bool

**Q3.** `17 // 5`와 `17 % 5`의 결과를 순서대로 고르면?

- ① 3, 2
- ② 3.4, 2
- ③ 2, 3
- ④ 3, 3

**Q4.** 변수 이름으로 사용할 수 **없는** 것은?

- ① best_score
- ② _chance
- ③ 2player
- ④ lowValue

**Q5.** `chance = 7` 다음에 `chance -= 2`를 실행하면 chance의 값은?

- ① 7
- ② 5
- ③ -2
- ④ 9

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 두 수의 사칙연산 (기본)

두 정수 a, b를 한 줄에 입력받아 합, 차, 몫, 나머지를 한 줄에 하나씩 출력하세요. (b는 0이 아니다.)

- 입력: 첫째 줄에 정수 a, b가 공백으로 구분되어 주어진다.
- 출력: a+b, a-b, a//b, a%b 를 한 줄에 하나씩 출력한다.

예제 입력 1

```text
17 5
```

예제 출력 1

```text
22
12
3
2
```

예제 입력 2

```text
100 7
```

예제 출력 2

```text
107
93
14
2
```

### 문제 2. 플레이 시간 변환 (도전)

게임 플레이 시간(초)을 입력받아 `○분 ○초` 형식으로 출력하세요.

- 입력: 첫째 줄에 0 이상의 정수 초가 주어진다.
- 출력: `분 초` 형식으로 출력한다.

예제 입력 1

```text
135
```

예제 출력 1

```text
2분 15초
```

예제 입력 2

```text
59
```

예제 출력 2

```text
0분 59초
```

예제 입력 3

```text
3600
```

예제 출력 3

```text
60분 0초
```

정답과 해설은 **[부록] 06-1-02. 2차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-02-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 추상화: 게임에 꼭 필요한 데이터(정답, 기회, 범위, 기록)만 골라낸다.
- 변수 = 이름 붙은 상자, `=`는 대입
- `input()`은 항상 문자열 → 계산하려면 `int()`
- `//` 몫, `%` 나머지, `**` 거듭제곱

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `01_updown_basic.py` | [01_updown_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/01_updown_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/01_updown_basic.py) |
| 학습용 PPT | [02-variables-input.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/02-variables-input.pptx) |
| 학생 활동지 | [ws02-variables-input.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws02-variables-input.md) |
| 코딩 테스트 1 정답 코드 | [ch02_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch02_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch02_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch02_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch02_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch02_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
