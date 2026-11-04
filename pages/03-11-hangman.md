> **3부 함수와 자료구조로 게임 다듬기** · 11차시 · 6단계 모형: **구현**  
> 게임: 영단어 행맨 (난이도 중)  
> 핵심 개념: 종합, all(), 제너레이터 표현식, isalpha, bool 연산, 기능 추가

## 학습 목표

1. 딕셔너리·리스트·함수·반복·조건을 종합하여 게임을 구현할 수 있다.
2. 제너레이터 표현식과 all() 함수로 '모두 만족하는지'를 검사할 수 있다.
3. 기존 게임에 새 기능을 설계하고 추가할 수 있다.

## 핵심 질문

> **지금까지 배운 도구를 모두 모으면 어떤 게임을 만들 수 있을까?**

행맨은 단어의 글자를 하나씩 맞혀 가는 게임입니다. **딕셔너리**(단어:뜻), **리스트**(말한 글자), **함수**(화면·입력·한 판), **반복과 조건**이 모두 들어 있어 지금까지 배운 내용을 정리하기에 좋습니다.

## 구조 한눈에 보기

| 부분 | 코드 | 사용한 개념 |
| --- | --- | --- |
| 단어 데이터 | `WORDS = {"python": "파이썬", ...}` | 딕셔너리 |
| 상태 출력 | `show(word, guessed, lives)` | 함수, 문자열 join, 반복 연산 |
| 입력 검사 | `ask_letter(guessed)` | while True, or 조건, isalpha |
| 한 판 진행 | `play()` | while, all(), return True/False |
| 전적 관리 | 맨 아래 반복 | bool을 숫자로 더하기 |

## 보드 만들기: 제너레이터 표현식

```python
def show(word, guessed, lives):
    board = " ".join(ch if ch in guessed else "_" for ch in word)
    print(f"{board}   목숨: {'♥' * lives}{'♡' * (6 - lives)}")
```

`ch if ch in guessed else "_" for ch in word`는 "단어의 각 글자에 대해, 맞힌 글자면 그대로, 아니면 `_`"라는 뜻입니다. 아래 반복문과 같은 일을 한 줄로 쓴 것입니다.

```python
parts = []
for ch in word:
    parts.append(ch if ch in guessed else "_")
board = " ".join(parts)
```

## ♥ ♡ 같은 특수 문자 입력하기

`'♥' * lives`처럼 코드 안에 **특수 문자**를 직접 쓰려면 키보드로 입력하는 방법을 알아야 합니다.

### 방법 1. 한글 자음 + 한자 키 (윈도우, 가장 쉬움)

1. 한/영 키로 **한글 입력 상태**로 바꿉니다.
2. 따옴표 안에서 자음 **ㅁ**을 입력합니다.
3. 키보드 오른쪽 아래 **한자** 키(또는 오른쪽 Ctrl)를 누르면 특수 문자 목록이 나타납니다.
4. **Tab** 키로 전체 목록을 펼친 뒤 ♥(검은 하트)와 ♡(흰 하트)를 고르고 Enter를 누릅니다.

| 자음 + 한자 | 나오는 기호 (일부) |
| --- | --- |
| ㅁ | ♥ ♡ ★ ☆ ● ○ ■ □ ◆ ◇ ← → ↑ ↓ |
| ㅂ | ─ │ ┌ ┐ └ ┘ ├ ┤ (선 그리기) |
| ㅇ | ① ② ③ ⓐ ⓑ (원 숫자·문자) |
| ㄷ | + − × ÷ ≤ ≥ ≠ (수학 기호) |

### 방법 2. 맥(macOS)

**Control + Command + Space**를 누르면 문자 뷰어가 열립니다. 검색 칸에 '하트' 또는 'heart'를 입력해 고릅니다.

### 방법 3. 유니코드 번호로 쓰기 (어느 컴퓨터에서나)

키보드로 입력하기 어려우면 파이썬의 **유니코드 이스케이프** `\u번호`를 씁니다. 화면에는 똑같이 보입니다.

```python
print("\u2665" * 3 + "\u2661" * 3)   # ♥♥♥♡♡♡
HEART, EMPTY = "\u2665", "\u2661"
print(f"목숨: {HEART * 4}{EMPTY * 2}")   # 목숨: ♥♥♥♥♡♡
```

| 기호 | 유니코드 | 기호 | 유니코드 |
| --- | --- | --- | --- |
| ♥ | `\u2665` | ♡ | `\u2661` |
| ★ | `\u2605` | ☆ | `\u2606` |
| ↑ | `\u2191` | ↓ | `\u2193` |
| ← | `\u2190` | → | `\u2192` |

### 방법 4. 복사해서 붙여 넣기

이 페이지의 ♥ ♡ 를 드래그해 복사(Ctrl + C)한 뒤 코드에 붙여 넣어도 됩니다.

특수 문자가 □나 ?로 보이면 편집기나 터미널 글꼴이 그 문자를 지원하지 않는 것입니다. IDLE은 **Options → Configure IDLE**에서 글꼴을 '맑은 고딕'이나 'D2Coding'으로 바꿔 보세요. 특수 문자 대신 `"*"`, `"-"`처럼 키보드에 있는 문자를 써도 게임은 똑같이 동작합니다.

## 모두 맞혔나? all()

```python
if all(ch in guessed for ch in word):   # 모든 글자가 guessed 안에 있으면
    print("성공!")
    return True
```

| 함수 | 의미 | 예 |
| --- | --- | --- |
| `all(조건들)` | 모두 참이면 True | `all(x > 0 for x in [1, 2, 3])` → True |
| `any(조건들)` | 하나라도 참이면 True | `any(x > 2 for x in [1, 2, 3])` → True |

## 입력 검사와 bool 더하기

```python
def ask_letter(guessed):
    while True:
        ch = input("알파벳 한 글자 > ").lower()
        if len(ch) != 1 or not (ch.isascii() and ch.isalpha()) or ch in guessed:
            print("알파벳 한 글자만, 이미 쓴 글자는 안 돼요!")
        else:
            return ch

wins += play()     # True 는 1, False 는 0 으로 계산된다
```

`isalpha()`는 **한글도 True**입니다. 한글 자판 상태에서 a를 누르면 'ㅁ'이 들어가는데, `isalpha()`만 검사하면 이 글자를 받아들여 목숨이 줄어듭니다. 그래서 `isascii()`(영문·숫자·기호 같은 기본 문자인가?)와 **함께** 검사해 영어 알파벳만 받습니다.

```python
print("a".isalpha(), "ㅁ".isalpha())                       # True True
print("ㅁ".isascii() and "ㅁ".isalpha())                    # False → 다시 입력
```

## 코드 흐름 따라가기

프로그램을 실행하면 아래 순서로 함수가 호출되고 값이 오갑니다. 전체 코드를 옆에 띄워 놓고 한 줄씩 따라가 보세요.

| 순서 | 실행되는 곳 | 하는 일 |
| --- | --- | --- |
| 1 | 맨 아래 `if __name__ == "__main__":` | `wins`, `games`를 0으로 두고 여러 판을 반복한다. |
| 2 | `play()` | `random.choice(list(WORDS))`로 단어(키)를 고르고 뜻(값)을 힌트로 보여 준다. `guessed = []`, `lives = 6`. |
| 3 | `play()` → `show(word, guessed, lives)` | 맞힌 글자만 보이는 보드와 ♥ 목숨, 사용한 글자를 출력한다. |
| 4 | `play()` | `all(ch in guessed for ch in word)` — 모든 글자를 맞혔으면 `return True`. |
| 5 | `play()` → `ask_letter(guessed)` | 알파벳 한 글자이고 처음 쓰는 글자일 때만 돌려준다. |
| 6 | `play()` | 글자를 `guessed`에 추가하고, 단어에 없으면 `lives -= 1`. 목숨이 0이 되면 반복이 끝나고 `return False`. |
| 7 | 맨 아래 반복 | `wins += play()` — True는 1, False는 0으로 더해진다. 전적을 출력하고 "또 할까요?"를 묻는다. |

## 실행 예시

`09_hangman.py`를 실행했을 때의 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. (무작위 값이 있어 실행할 때마다 결과가 달라집니다.)

```text

힌트(뜻): 컴퓨터  /  글자 수: 8

_ _ _ _ _ _ _ _   목숨: ♥♥♥♥♥♥   사용: 
알파벳 한 글자 > e

_ _ _ _ _ _ e _   목숨: ♥♥♥♥♥♥   사용: e
알파벳 한 글자 > a

_ _ _ _ _ _ e _   목숨: ♥♥♥♥♥♡   사용: e a
알파벳 한 글자 > o

_ o _ _ _ _ e _   목숨: ♥♥♥♥♥♡   사용: e a o
알파벳 한 글자 > i

_ o _ _ _ _ e _   목숨: ♥♥♥♥♡♡   사용: e a o i
알파벳 한 글자 > t

_ o _ _ _ t e _   목숨: ♥♥♥♥♡♡   사용: e a o i t
알파벳 한 글자 > n

_ o _ _ _ t e _   목숨: ♥♥♥♡♡♡   사용: e a o i t n
알파벳 한 글자 > r

_ o _ _ _ t e r   목숨: ♥♥♥♡♡♡   사용: e a o i t n r
알파벳 한 글자 > s

_ o _ _ _ t e r   목숨: ♥♥♡♡♡♡   사용: e a o i t n r s
알파벳 한 글자 > c

c o _ _ _ t e r   목숨: ♥♥♡♡♡♡   사용: e a o i t n r s c
알파벳 한 글자 > l

c o _ _ _ t e r   목숨: ♥♡♡♡♡♡   사용: e a o i t n r s c l
알파벳 한 글자 > u

c o _ _ u t e r   목숨: ♥♡♡♡♡♡   사용: e a o i t n r s c l u
알파벳 한 글자 > p

c o _ p u t e r   목숨: ♥♡♡♡♡♡   사용: e a o i t n r s c l u p
알파벳 한 글자 > m

c o m p u t e r   목숨: ♥♡♡♡♡♡   사용: e a o i t n r s c l u p m
성공! 정답: computer
전적: 1판 1승
또 할까요? (y/n) > n
```

## 전체 코드

지금까지 조각으로 살펴본 코드를 하나로 합친 **전체 프로그램**입니다. 아래 순서로 바로 실행할 수 있습니다.

1. 코드 블록 전체를 복사합니다. (위키독스 코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### 09_hangman.py

```python
"""영단어 행맨 (난이도 중) - 11차시: 딕셔너리, 리스트, 함수, 제너레이터 표현식, all()

실행 방법: python 09_hangman.py
"""

# =====================================================================
# 게임 규칙
#   컴퓨터가 영단어 하나를 고르고, 뜻(힌트)과 글자 수만 알려 줘요.
#   알파벳을 하나씩 말해서 단어를 완성하면 성공!
#   단어에 없는 글자를 말할 때마다 목숨(♥)이 1개씩 줄어요. 6개를 다 잃으면 실패.
#
# 배운 내용 총정리 (종합 차시)
#   딕셔너리 WORDS  : {영단어: 뜻}
#   리스트 guessed  : 지금까지 말한 글자들
#   함수 show / ask_letter / play : 화면 출력 / 입력 검사 / 한 판 진행
#   all(...)        : 괄호 안의 조건이 "모두" 참이면 True → 모든 글자를 맞혔는지 확인
# =====================================================================

import random

WORDS = {"computer": "컴퓨터", "algorithm": "알고리즘", "variable": "변수",
         "python": "파이썬", "internet": "인터넷", "function": "함수"}   # 영단어: 뜻(힌트)

def show(word, guessed, lives):
    """현재 상태(맞힌 글자, 목숨, 사용한 글자)를 보여 준다"""
    # 단어의 각 글자 ch 에 대해: 맞힌 글자면 그대로, 아니면 "_" → 공백으로 이어 붙임
    # 예) word="python", guessed=['p','o'] → "p _ _ _ o _"
    board = " ".join(ch if ch in guessed else "_" for ch in word)
    # 문자열 * 정수 → 반복. '♥' * 4 → '♥♥♥♥'
    # ♥(검은 하트)·♡(흰 하트) 입력 방법
    #   - 윈도우: 한글 입력 상태에서 ㅁ 을 치고 [한자] 키 → Tab 으로 목록 펼치기 → ♥, ♡ 선택
    #   - 맥: Control + Command + Space → 문자 뷰어에서 '하트' 검색
    #   - 어디서나: 유니코드로 '\u2665'(♥), '\u2661'(♡) 라고 써도 똑같이 출력돼요.
    print(f"\n{board}   목숨: {'♥' * lives}{'♡' * (6 - lives)}   사용: {' '.join(guessed)}")

def ask_letter(guessed):
    """알파벳 한 글자이고, 아직 쓰지 않은 글자일 때만 돌려준다"""
    while True:
        ch = input("알파벳 한 글자 > ").lower()       # 대문자로 입력해도 소문자로 통일
        # 세 가지 중 하나라도 해당하면(or) 다시 입력: 길이가 1이 아님 / 영어 알파벳이 아님 / 이미 씀
        # isalpha()는 한글('ㅁ')도 True 라서 isascii()와 함께 검사해야 영어 알파벳만 받아요.
        #   (한글 자판 상태에서 a 를 누르면 'ㅁ'이 입력돼요!)
        if len(ch) != 1 or not (ch.isascii() and ch.isalpha()) or ch in guessed:
            print("알파벳 한 글자만, 이미 쓴 글자는 안 돼요!")
        else:
            return ch

def play():
    """한 판을 진행하고 성공하면 True, 실패하면 False 를 돌려준다"""
    word = random.choice(list(WORDS))          # list(딕셔너리) → 키 목록. 그중 무작위 선택
    guessed, lives = [], 6
    print(f"\n힌트(뜻): {WORDS[word]}  /  글자 수: {len(word)}")
    while lives > 0:
        show(word, guessed, lives)
        if all(ch in guessed for ch in word):  # 단어의 모든 글자가 guessed 안에 있으면 성공
            print("성공! 정답:", word)
            return True
        ch = ask_letter(guessed)
        guessed.append(ch)
        if ch not in word:                     # 문자열에도 in 을 쓸 수 있어요: 'y' in 'python' → True
            lives -= 1
    print("실패... 정답은", word)
    return False

# 프로그램 시작 ----------------------------------------------------------
if __name__ == "__main__":
    wins = games = 0
    while True:
        games += 1
        wins += play()          # True 는 1, False 는 0 으로 계산돼요! (성공하면 +1)
        print(f"전적: {games}판 {wins}승")
        if input("또 할까요? (y/n) > ") != "y":
            break
```

파일 받기: [09_hangman.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/09_hangman.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/09_hangman.py)

## 실습 활동

1. `WORDS`에 정보 교과 용어 5개를 추가해 보세요. (예: "loop": "반복")
2. 목숨이 2개 이하일 때 단어의 첫 글자를 힌트로 보여 주는 기능을 추가해 보세요.
3. 전적을 딕셔너리 `{"win": 0, "lose": 0}`로 바꿔 보세요.

활동지: [ws11-hangman.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws11-hangman.md)

## 확인 퀴즈

**Q1.** `all([True, False, True])`의 결과는?

- ① True
- ② False
- ③ 2
- ④ 오류

**Q2.** word="cat", guessed=['a']일 때 `" ".join(ch if ch in guessed else "_" for ch in word)`는?

- ① _ a _
- ② c a t
- ③ a
- ④ _ _ _

**Q3.** `3 + True + False`의 값은?

- ① 3
- ② 4
- ③ 5
- ④ 오류

**Q4.** `"A".isalpha() and len("A") == 1`의 결과는?

- ① True
- ② False
- ③ "A"
- ④ 1

**Q5.** 행맨의 `ask_letter`가 다시 입력을 요구하는 경우가 **아닌** 것은?

- ① "ab"
- ② "3"
- ③ 이미 쓴 글자
- ④ 처음 쓰는 "k"

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 행맨 보드 출력 (기본)

첫째 줄에 단어, 둘째 줄에 지금까지 말한 글자들이 공백으로 주어집니다. 맞힌 글자는 그대로, 아닌 글자는 `_`로 바꿔 공백으로 구분해 출력하세요. 둘째 줄이 빈 줄이면 아무 글자도 말하지 않은 것입니다.

- 입력: 단어, 말한 글자들
- 출력: 보드

예제 입력 1

```text
python
p o z
```

예제 출력 1

```text
p _ _ _ o _
```

예제 입력 2

```text
loop
o
```

예제 출력 2

```text
_ o o _
```

### 문제 2. 행맨 한 판 시뮬레이션 (도전)

첫째 줄에 단어, 둘째 줄에 순서대로 말한 글자들이 공백으로 주어집니다. 목숨은 6개이며, 단어에 없는 글자를 말하면 1 줄어듭니다. 단어를 완성하면 `성공 ○`(남은 목숨), 목숨이 0이 되면 `실패`를 출력하고 그 즉시 끝냅니다. 글자를 다 말해도 끝나지 않으면 `진행 중 ○`(남은 목숨)을 출력하세요.

- 입력: 단어, 글자들
- 출력: 결과

예제 입력 1

```text
cat
x c a y t
```

예제 출력 1

```text
성공 4
```

예제 입력 2

```text
dog
a b c e f h
```

예제 출력 2

```text
실패
```

예제 입력 3

```text
tree
t e
```

예제 출력 3

```text
진행 중 6
```

정답과 해설은 **[부록] 06-1-11. 11차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-11-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 행맨 = 딕셔너리 + 리스트 + 함수 + 반복 + 조건의 종합
- 제너레이터 표현식으로 보드를 한 줄에
- all() 모두 참 / any() 하나라도 참
- True = 1, False = 0

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `09_hangman.py` | [09_hangman.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/09_hangman.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/09_hangman.py) |
| 학습용 PPT | [11-hangman.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/11-hangman.pptx) |
| 학생 활동지 | [ws11-hangman.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws11-hangman.md) |
| 코딩 테스트 1 정답 코드 | [ch11_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch11_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch11_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch11_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch11_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch11_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
