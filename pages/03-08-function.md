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
