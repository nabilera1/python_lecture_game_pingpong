> **3부 함수와 자료구조로 게임 다듬기** · 8차시 · 6단계 모형: **구현**  
> 게임: 업다운 (함수 버전) · 기억력 게임 (함수 버전)  
> 핵심 개념: def, 매개변수, 인수, return, 기본값, main(), __name__, 리팩터링

## 학습 목표

1. def로 함수를 정의하고 호출할 수 있다.
2. 매개변수와 반환값(return)의 역할을 설명할 수 있다.
3. 기존 코드를 기능별 함수와 main() 구조로 리팩터링할 수 있다.

## 핵심 질문

> **분해한 '작은 문제'를 코드에서도 따로따로 다루려면 어떻게 해야 할까?**

3차시에 업다운 게임을 **입력받기·판정하기·한 판 진행하기**로 분해했습니다. 지금까지의 코드는 그 부분들이 한 덩어리로 섞여 있었습니다.

**함수**를 쓰면 하위 문제 하나를 **이름 붙은 코드 묶음** 하나로 만들 수 있습니다. 동작은 그대로 두고 구조만 더 좋게 고치는 것을 **리팩터링**이라고 합니다.

## 함수의 모양

```python
def judge(guess, secret):            # def 함수이름(매개변수):
    """'correct' / 'up' / 'down' 중 하나를 돌려준다"""   # 함수 설명(독스트링)
    if guess == secret:
        return "correct"             # return: 값을 돌려주고 함수 끝
    return "up" if guess < secret else "down"

result = judge(30, 50)               # 호출: 30, 50 은 인수(argument)
print(result)                        # up
```

| 용어 | 뜻 | 예 |
| --- | --- | --- |
| 정의 | 함수를 만드는 것 | `def judge(...):` |
| 호출 | 함수를 실행하는 것 | `judge(30, 50)` |
| 매개변수 | 함수가 받는 값의 이름 | `guess`, `secret` |
| 인수 | 호출할 때 실제로 넘기는 값 | `30`, `50` |
| 반환값 | 함수가 돌려주는 결과 | `"up"` |

## 업다운 함수 설계표

| 함수 | 매개변수 | 반환값 | 하는 일 |
| --- | --- | --- | --- |
| `read_number` | low, high, chance | 정수 | 숫자가 들어올 때까지 다시 묻기 |
| `judge` | guess, secret | "correct"/"up"/"down" | 판정하기 |
| `play` | 없음 | 맞힌 횟수 (실패 0) | 한 판 진행 |
| `main` | 없음 | 없음 | 여러 판 반복, 최고 기록 |

```python
def read_number(low, high, chance):
    while True:
        text = input(f"[{low}~{high}] 남은 기회 {chance}회 > ")
        if text.isdigit():
            return int(text)          # return 이 while True 의 출구
        print("숫자를 입력하세요!")
```

`return`을 만나면 **반복 중이라도 함수가 즉시 끝납니다.** 그래서 `while True` 안의 `return`은 break의 역할도 합니다.

## 기본값 매개변수와 main() 구조

```python
def show_sequence(seq, base=1.0):   # base 를 안 주면 1.0 사용
    time.sleep(base + len(seq) * 0.5)

show_sequence(seq)          # base = 1.0
show_sequence(seq, 2.0)     # base = 2.0 (더 쉬운 난이도)

def main():
    ...                     # 프로그램 전체 흐름

if __name__ == "__main__":  # 이 파일을 직접 실행할 때만
    main()
```

`if __name__ == "__main__":`을 쓰면 다른 파일에서 `import`로 함수만 가져다 쓸 때 게임이 갑자기 실행되지 않습니다. 핑퐁 게임의 `main.py`에서도 똑같은 구조를 보게 됩니다.

## 지역 변수와 전역 변수

함수 안에서 만든 변수는 **함수 안에서만** 쓸 수 있습니다(지역 변수). 함수끼리 값을 주고받을 때는 **매개변수로 받고 return으로 돌려주는 것**이 원칙입니다.

```python
def play():
    secret = random.randint(1, 100)   # play 안에서만 존재
    ...
    return len(history)

tries = play()       # 결과는 return 으로 받아 온다
# print(secret)      # 오류! secret 은 play 밖에서는 없다
```

## 코드 흐름 따라가기

프로그램을 실행하면 아래 순서로 함수가 호출되고 값이 오갑니다. 전체 코드를 옆에 띄워 놓고 한 줄씩 따라가 보세요.

| 순서 | 실행되는 곳 | 하는 일 |
| --- | --- | --- |
| 1 | 맨 아래 `if __name__ == "__main__":` | 파일을 직접 실행했으므로 `main()`을 호출한다. |
| 2 | `main()` | 제목을 출력하고 `best = 0`(최고 기록 없음)으로 시작해 `while True`로 여러 판을 반복한다. |
| 3 | `main()` → `play()` | 한 판 시작. `secret`(정답), `low`·`high`(범위), `history`(기록)를 준비한다. |
| 4 | `play()` → `read_number(low, high, chance)` | 숫자가 들어올 때까지 다시 묻고, 정수를 **돌려받는다(return)**. `abc`처럼 잘못 넣으면 기회가 줄지 않는다. |
| 5 | `play()` → `judge(guess, secret)` | 판정 결과 `"correct"`/`"up"`/`"down"` 중 하나를 돌려받는다. |
| 6 | `play()` | `"correct"`이면 `return len(history)`로 시도 횟수를 돌려주며 함수가 끝난다. `"up"`/`"down"`이면 범위를 좁히고 다음 기회로 넘어간다. 7번 모두 틀리면 `return 0`. |
| 7 | `main()` | 돌려받은 `tries`로 최고 기록을 갱신하고, "또 할까요?"에 `y`가 아니면 `break`로 끝낸다. |

```text
main()
 └─ play()                     ← 한 판 (맞힌 횟수 반환)
     ├─ read_number(...)       ← 올바른 정수 반환
     └─ judge(guess, secret)   ← "correct" / "up" / "down" 반환
```

함수마다 **받는 값**(매개변수)과 **돌려주는 값**(반환값)이 정해져 있어서, 함수끼리는 이 값만 주고받습니다. 그래서 `judge()`만 따로 떼어 시험해 볼 수도 있습니다.

## 실행 예시

`05_updown_func.py`를 실행했을 때의 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. (무작위 값이 있어 실행할 때마다 결과가 달라집니다.)

```text
=== 업다운 === 1~100 사이의 숫자를 7번 안에 맞히세요!
[1~100] 남은 기회 7회 > abc
숫자를 입력하세요!
[1~100] 남은 기회 7회 > 50
DOWN! 더 작은 수예요.
[1~49] 남은 기회 6회 > 25
UP! 더 큰 수예요.
[26~49] 남은 기회 5회 > 37
UP! 더 큰 수예요.
[38~49] 남은 기회 4회 > 43
DOWN! 더 작은 수예요.
[38~42] 남은 기회 3회 > 40
UP! 더 큰 수예요.
[41~42] 남은 기회 2회 > 41
UP! 더 큰 수예요.
[42~42] 남은 기회 1회 > 42
정답! 7번 만에 맞혔어요. 기록: [50, 25, 37, 43, 40, 41, 42]
최고 기록: 7번
또 할까요? (y/n) > n
```

## 전체 코드

지금까지 조각으로 살펴본 코드를 하나로 합친 **전체 프로그램**입니다. 아래 순서로 바로 실행할 수 있습니다.

1. 코드 블록 전체를 복사합니다. (위키독스 코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### 05_updown_func.py

```python
"""업다운 게임 (함수 버전) - 8차시: 함수 정의·호출, 매개변수, 반환값, main() 구조

실행 방법: python 05_updown_func.py
"""

# =====================================================================
# 01_updown_basic.py 와 무엇이 달라졌을까요?
# ---------------------------------------------------------------------
# 같은 게임을 "기능별 함수"로 나누었어요. (문제 분해 → 함수 하나 = 작은 문제 하나)
#
#   read_number(low, high, chance) : 숫자가 들어올 때까지 다시 묻고 정수로 돌려줌
#   judge(guess, secret)           : "correct" / "up" / "down" 판정 결과를 돌려줌
#   play()                         : 한 판 진행, 맞힌 횟수(실패 시 0)를 돌려줌
#   main()                         : 여러 판 반복 + 최고 기록 관리
#
# 함수로 나누면 좋은 점
#   1) 이름만 봐도 무슨 일을 하는지 알 수 있어요. (가독성)
#   2) judge() 처럼 작은 함수는 따로 테스트하기 쉬워요. (테스트 용이성)
#   3) 같은 코드를 여러 번 쓰지 않아도 돼요. (재사용)
# =====================================================================

import random

MAX_CHANCE = 7          # 대문자 이름 = 바뀌지 않는 값(상수)이라는 약속

def read_number(low, high, chance):
    """숫자가 입력될 때까지 다시 물어보고, 정수로 바꿔 돌려준다"""
    # low, high, chance 는 "매개변수": 함수를 부를 때 넘겨받는 값이에요.
    while True:
        text = input(f"[{low}~{high}] 남은 기회 {chance}회 > ")
        if text.isdigit():
            return int(text)        # return: 값을 돌려주고 함수를 즉시 끝냄 (반복도 끝!)
        print("숫자를 입력하세요!")

def judge(guess, secret):
    """'correct' / 'up' / 'down' 중 하나를 돌려준다"""
    if guess == secret:
        return "correct"
    # 조건 표현식으로 두 경우를 한 줄에
    return "up" if guess < secret else "down"

def play():
    """한 판을 진행하고, 맞힌 횟수를 돌려준다 (실패하면 0)"""
    secret = random.randint(1, 100)
    low, high, history = 1, 100, []

    # range(7, 0, -1) → 7, 6, 5, 4, 3, 2, 1  (시작, 끝(포함 안 함), 간격)
    for chance in range(MAX_CHANCE, 0, -1):
        guess = read_number(low, high, chance)    # 함수 호출 → 돌려받은 값을 guess 에 저장
        history.append(guess)
        result = judge(guess, secret)
        if result == "correct":
            print(f"정답! {len(history)}번 만에 맞혔어요. 기록: {history}")
            return len(history)
        if result == "up":
            print("UP! 더 큰 수예요.")
            low = max(low, guess + 1)       # 범위를 좁혀 간다
        else:
            print("DOWN! 더 작은 수예요.")
            high = min(high, guess - 1)
    print(f"실패! 정답은 {secret}, 기록: {history}")
    return 0

def main():
    print("=== 업다운 === 1~100 사이의 숫자를 7번 안에 맞히세요!")
    best = 0                                # 가장 적은 시도 횟수 기록 (0 = 아직 기록 없음)
    while True:
        tries = play()
        # tries 가 0이 아니고(성공), 처음 기록이거나 더 적은 횟수면 최고 기록 갱신
        if tries and (best == 0 or tries < best):
            best = tries
        print(f"최고 기록: {best}번" if best else "아직 성공 기록이 없어요.")
        if input("또 할까요? (y/n) > ") != "y":
            break

# 이 파일을 직접 실행할 때만 main() 을 호출 (다른 파일에서 import 할 때는 실행 안 됨)
if __name__ == "__main__":
    main()
```

파일 받기: [05_updown_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/05_updown_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/05_updown_func.py)

### 07_memory_func.py

```python
"""기억력 게임 (함수 버전) - 8차시 추가 예제: 매개변수 기본값, 반환값, main() 구조

실행 방법: python 07_memory_func.py
"""

# =====================================================================
#   show_sequence(seq, base=1.0) : 숫자를 보여 주고 지움 (base 를 안 주면 1.0초 사용)
#   ask_sequence()               : 입력을 글자 리스트로 바꿔 돌려줌
#   play()                       : 한 판 진행 → 성공 라운드 수 반환
#   main()                       : 여러 판 반복 + 최고 기록
# =====================================================================

import random
import time

def show_sequence(seq, base=1.0):
    """숫자를 잠깐 보여 준 뒤 화면을 지운다 (숫자가 많을수록 오래 보여 줌)"""
    # base=1.0 : "기본값이 있는 매개변수". show_sequence(seq) 처럼 생략 가능
    print(f"\n[{len(seq)}라운드] 기억하세요:", " ".join(seq))
    time.sleep(base + len(seq) * 0.5)
    print("\n" * 40)

def ask_sequence():
    """입력한 글자를 한 글자씩 나눈 리스트로 돌려준다"""
    text = input("방금 본 숫자를 붙여서 입력 > ")
    return list(text.replace(" ", ""))

def play():
    """한 판을 진행하고, 성공한 라운드 수를 돌려준다"""
    seq, level = [], 0
    while True:
        seq.append(random.choice("123456789"))
        show_sequence(seq)
        if ask_sequence() != seq:               # 리스트끼리 비교
            print("틀렸어요! 정답은", "".join(seq))
            return level                        # return 이 무한 반복을 끝내는 출구
        level += 1
        print("정답! 다음 라운드로!")

def main():
    print("=== 기억력 게임 === 화면에 나온 숫자를 기억해서 입력하세요!")
    best = 0
    while True:
        level = play()
        best = max(best, level)                 # 최고 기록 = 지금까지 중 가장 큰 값
        print(f"이번 기록: {level}라운드 / 최고 기록: {best}라운드")
        if input("또 할까요? (y/n) > ") != "y":
            break

if __name__ == "__main__":
    main()
```

파일 받기: [07_memory_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/07_memory_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/07_memory_func.py)

## 실습 활동

1. `05_updown_func.py`의 `judge()`만 따로 호출해 보세요. `judge(1, 1)`, `judge(99, 1)`의 결과는?
2. `play()`에 매개변수 `max_chance=7`을 추가해 난이도(쉬움 10회, 어려움 5회)를 고를 수 있게 해 보세요.
3. 기억력 게임의 `show_sequence(seq, base)`를 이용해 난이도 선택 기능을 추가해 보세요.

활동지: [ws08-function.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws08-function.md)

## 확인 퀴즈

**Q1.** 함수를 정의할 때 사용하는 키워드는?

- ① func
- ② def
- ③ function
- ④ define

**Q2.** 다음 코드의 출력은?

```python
def f(a, b=10):
    return a + b
print(f(5), f(5, 1))
```

- ① 15 15
- ② 15 6
- ③ 5 6
- ④ 오류

**Q3.** `return` 문에 대한 설명으로 옳지 **않은** 것은?

- ① 값을 돌려준다
- ② 함수를 즉시 끝낸다
- ③ 반복문 안에서도 쓸 수 있다
- ④ 함수 밖에서도 쓸 수 있다

**Q4.** `judge(guess, secret)`에서 guess, secret을 무엇이라 하는가?

- ① 인수
- ② 매개변수
- ③ 반환값
- ④ 전역 변수

**Q5.** `if __name__ == "__main__":`의 역할은?

- ① 오류를 막는다
- ② 파일을 직접 실행할 때만 아래 코드를 실행한다
- ③ main 함수를 정의한다
- ④ 모듈을 설치한다

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. judge 함수 만들기 (기본)

`judge(guess, secret)` 함수를 만들어 정답이면 `correct`, guess가 작으면 `up`, 크면 `down`을 반환하게 하세요. 첫째 줄에 정답, 둘째 줄에 n, 다음 n줄의 추측마다 judge 결과를 출력합니다.

- 입력: 정답, n, n개의 추측
- 출력: 각 추측에 대한 judge 결과

예제 입력 1

```text
50
3
30
70
50
```

예제 출력 1

```text
up
down
correct
```

### 문제 2. 입력 검사 함수 (도전)

`is_valid(text, low, high)` 함수를 만드세요. text가 숫자로만 되어 있고 low 이상 high 이하이면 True, 아니면 False를 반환합니다. 첫째 줄에 low high, 둘째 줄에 n, 다음 n줄의 문자열마다 결과를 출력하세요.

- 입력: low high, n, n줄의 문자열
- 출력: 각 줄의 True/False

예제 입력 1

```text
1 100
5
50
150
abc
1
-3
```

예제 출력 1

```text
True
False
False
True
False
```

정답과 해설은 **[부록] 06-1-08. 8차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-08-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 함수 = 하위 문제 하나를 이름 붙인 코드 묶음
- 매개변수로 받고, return으로 돌려준다
- 기본값 매개변수로 난이도 같은 옵션을 쉽게
- main() + if __name__ == "__main__": 구조

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `05_updown_func.py` | [05_updown_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/05_updown_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/05_updown_func.py) |
| 소스코드 `07_memory_func.py` | [07_memory_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/07_memory_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/07_memory_func.py) |
| 학습용 PPT | [08-function.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/08-function.pptx) |
| 학생 활동지 | [ws08-function.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws08-function.md) |
| 코딩 테스트 1 정답 코드 | [ch08_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch08_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch08_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch08_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch08_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch08_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
