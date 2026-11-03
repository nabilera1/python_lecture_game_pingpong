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
        if len(ch) != 1 or not ch.isalpha() or ch in guessed:
            print("알파벳 한 글자만, 이미 쓴 글자는 안 돼요!")
        else:
            return ch

wins += play()     # True 는 1, False 는 0 으로 계산된다
```

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
