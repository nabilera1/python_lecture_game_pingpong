> **2부 리스트와 반복으로 게임 만들기** · 6차시 · 6단계 모형: **컴퓨팅 설계**  
> 게임: 숫자 야구 (기본 버전)  
> 핵심 개념: for, range, 인덱싱, 슬라이싱, list(), join(), random.sample

## 학습 목표

1. for 문과 range()로 정해진 횟수만큼 반복할 수 있다.
2. 문자열과 리스트의 인덱싱·슬라이싱을 활용할 수 있다.
3. 숫자 야구의 스트라이크·볼 판정 알고리즘을 설계하고 구현할 수 있다.

## 핵심 질문

> **세 자리를 하나씩 비교하려면 반복을 어떻게 설계해야 할까?**

숫자 야구는 **같은 비교를 세 자리에 똑같이** 해야 합니다. while 문은 '조건이 참인 동안' 반복하지만, 이번처럼 **횟수가 정해진 반복**에는 **for 문**이 더 잘 어울립니다.

## for 문과 range()

```python
for i in range(3):          # i = 0, 1, 2
    print(i)

for i in range(1, 10, 2):   # 1, 3, 5, 7, 9  (시작, 끝(미포함), 간격)
    print(i, end=" ")

for ch in "PYTHON":         # 문자열의 글자를 하나씩
    print(ch)

for pick in ["가위", "바위", "보"]:   # 리스트의 값을 하나씩
    print(pick)
```

| 형태 | 만들어지는 값 |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 5)` | 2, 3, 4 |
| `range(7, 0, -1)` | 7, 6, 5, 4, 3, 2, 1 |

## 문자열 인덱싱과 슬라이싱

문자열도 리스트처럼 번호로 글자를 꺼낼 수 있습니다.

```python
s = "algorithm"
print(s[0], s[-1])     # a m
print(s[0:4])          # algo   ← 0번부터 4번 앞까지
print(s[4:])           # rithm  ← 4번부터 끝까지
print(list("175"))     # ['1', '7', '5']  문자열 → 글자 리스트
print("".join(['1', '7', '5']))   # 175  글자 리스트 → 문자열
```

슬라이싱 `[시작:끝]`에서 **끝 번호는 포함하지 않습니다.** range와 같은 규칙입니다.

## 스트라이크·볼 판정 알고리즘

```python
answer = random.sample("123456789", 3)    # 예: ['4', '7', '1']
guess = list(input("세 자리 숫자 > "))    # 예: ['1', '7', '5']

strike = ball = 0
for i in range(3):                        # 자리 번호 0, 1, 2
    if guess[i] == answer[i]:
        strike += 1                       # 숫자와 자리가 모두 같음
    elif guess[i] in answer:
        ball += 1                         # 숫자만 같음
print(f"결과: {strike}S {ball}B")         # 결과: 1S 1B
```

| i | guess[i] | answer[i] | 판정 |
| --- | --- | --- | --- |
| 0 | '1' | '4' | '1'은 answer에 있음 → 볼 |
| 1 | '7' | '7' | 같음 → 스트라이크 |
| 2 | '5' | '1' | 없음 → - |

이렇게 **변수 값의 변화를 표로 따라가는 것**을 **추적(trace)** 이라고 합니다. 디버깅의 기본 기술입니다.

## 실습 활동

1. `03_baseball_basic.py`에서 '서로 다른 숫자'가 아닌 입력(예: 112)을 넣으면 어떻게 되는지 확인하고, 막는 방법을 생각해 보세요.
2. 자릿수를 4자리로 바꾸려면 어느 부분을 고쳐야 할까요? 숫자 3을 변수 `DIGITS`로 바꿔 보세요.
3. 구구단 7단을 for 문으로 출력해 보세요.

활동지: [ws06-for-string.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws06-for-string.md)

## 확인 퀴즈

**Q1.** `range(2, 8, 3)`이 만드는 값은?

- ① 2, 5
- ② 2, 5, 8
- ③ 2, 3, 4, 5, 6, 7
- ④ 3, 6

**Q2.** `s = "python"`일 때 `s[1:4]`는?

- ① pyt
- ② yth
- ③ ytho
- ④ tho

**Q3.** 정답 `['3','5','8']`, 추측 `['5','3','8']`의 결과는?

- ① 3S 0B
- ② 1S 2B
- ③ 2S 1B
- ④ 0S 3B

**Q4.** `"-".join(["a", "b", "c"])`의 결과는?

- ① abc
- ② a-b-c
- ③ -a-b-c-
- ④ ['a','b','c']

**Q5.** 정해진 횟수만큼 반복할 때 주로 쓰는 반복문은?

- ① while True
- ② for ~ in range()
- ③ if ~ else
- ④ try ~ except

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 스트라이크·볼 계산기 (기본)

정답 세 자리와 추측 세 자리가 한 줄에 공백으로 주어집니다. 결과를 `○S ○B` 형식으로 출력하세요. (각 수의 숫자는 서로 다르다.)

- 입력: 정답과 추측이 공백으로 구분되어 주어진다. 예: `471 175`
- 출력: `S B` 형식

예제 입력 1

```text
471 175
```

예제 출력 1

```text
1S 1B
```

예제 입력 2

```text
358 538
```

예제 출력 2

```text
1S 2B
```

예제 입력 3

```text
123 456
```

예제 출력 3

```text
0S 0B
```

### 문제 2. 자릿수 합과 거꾸로 읽기 (도전)

숫자로 된 문자열을 입력받아 첫째 줄에 각 자리 숫자의 합, 둘째 줄에 문자열을 거꾸로 뒤집은 결과를 출력하세요.

- 입력: 첫째 줄에 숫자로만 이루어진 문자열 (1~100자리)
- 출력: 자릿수 합, 뒤집은 문자열

예제 입력 1

```text
12345
```

예제 출력 1

```text
15
54321
```

예제 입력 2

```text
9007
```

예제 출력 2

```text
16
7009
```

정답과 해설은 **[부록] 06-1-06. 6차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-06-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- for 변수 in range(...)/문자열/리스트: 정해진 횟수·모든 원소 반복
- range와 슬라이싱 모두 끝 번호는 미포함
- list("175") ↔ "".join(리스트)
- 변수 변화를 표로 따라가기 = 추적(trace)

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `03_baseball_basic.py` | [03_baseball_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/03_baseball_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/03_baseball_basic.py) |
| 학습용 PPT | [06-for-string.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/06-for-string.pptx) |
| 학생 활동지 | [ws06-for-string.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws06-for-string.md) |
| 코딩 테스트 1 정답 코드 | [ch06_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch06_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch06_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch06_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch06_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch06_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
