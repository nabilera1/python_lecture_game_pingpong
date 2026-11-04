> **2부 리스트와 반복으로 게임 만들기** · 5차시 · 6단계 모형: **컴퓨팅 설계**  
> 게임: 가위바위보 (기본 버전)  
> 핵심 개념: 리스트, 인덱스, append, in, random.choice, random.randint, % 연산

## 학습 목표

1. 리스트를 만들고 인덱스로 값을 읽고 추가할 수 있다.
2. random 모듈로 무작위 선택을 구현할 수 있다.
3. in 연산자와 나머지 연산으로 입력 검사와 승패 판정을 할 수 있다.

## 핵심 질문

> **여러 개의 값을 하나의 이름으로 다루려면 어떤 자료구조가 필요할까?**

가위바위보에는 **가위, 바위, 보** 세 가지 선택지가 있습니다. 변수 3개(`a = "가위"`, `b = "바위"` ...)로 따로 저장하면 다루기 불편합니다.

**리스트**를 쓰면 여러 값을 **순서대로 한 상자**에 담고, **번호**(인덱스)로 꺼낼 수 있습니다. 이 번호 덕분에 3차시에 본 `(나 - 컴퓨터) % 3` 판정이 가능해집니다.

## 리스트 기본

```python
choices = ["가위", "바위", "보"]
print(choices[0])        # 가위   ← 인덱스는 0부터!
print(choices[-1])       # 보     ← 음수 인덱스는 뒤에서부터
print(len(choices))      # 3
print(choices.index("보"))   # 2  ← 값의 위치 찾기

history = []             # 빈 리스트
history.append(50)       # 맨 뒤에 추가 → [50]
history.append(25)       # → [50, 25]
print("바위" in choices) # True  ← 들어 있는지 확인
```

| 표현 | 의미 |
| --- | --- |
| `리스트[i]` | i번째 값 (0부터 시작) |
| `len(리스트)` | 값의 개수 |
| `리스트.append(값)` | 맨 뒤에 추가 |
| `리스트.index(값)` | 값의 위치 |
| `값 in 리스트` | 들어 있으면 True |
| `max()`, `min()`, `sum()` | 최댓값, 최솟값, 합계 |

## random 모듈

```python
import random

random.randint(1, 100)            # 1 이상 100 이하 정수 (100 포함!)
random.choice(["가위", "바위", "보"])   # 리스트에서 하나 무작위 선택
random.sample("123456789", 3)     # 겹치지 않게 3개 뽑기 → ['4', '7', '1']
random.randrange(3)               # 0, 1, 2 중 하나 (3은 미포함)
```

`import`는 파이썬에 미리 만들어진 **모듈**(도구 상자)을 가져오는 문장입니다.

## 가위바위보 핵심 코드

```python
choices = ["가위", "바위", "보"]
me = com = 0
while me < 2 and com < 2:                 # 둘 다 2승 미만인 동안
    pick = input("가위 / 바위 / 보 > ")
    if pick not in choices:               # 입력 검사
        print("가위, 바위, 보 중에서 입력하세요!")
        continue
    cpu = random.choice(choices)          # 컴퓨터 선택
    diff = (choices.index(pick) - choices.index(cpu)) % 3
    if diff == 0:
        print("비겼어요!")
    elif diff == 1:
        print("이겼다!"); me += 1
    else:
        print("졌다..."); com += 1
print("최종 승리!" if me == 2 else "아쉽게 패배...")
```

- `A if 조건 else B` : 조건이 참이면 A, 거짓이면 B (**조건 표현식**)
- `me = com = 0` : 두 변수에 같은 값을 한 번에 대입

## 왜 % 3 일까? (수학 연계: 경우의 수)

나와 컴퓨터가 각각 3가지를 낼 수 있으므로 전체 경우는 **3 × 3 = 9가지**입니다.
그중 비김 3, 이김 3, 짐 3가지이며, 리스트 순서 `가위 → 바위 → 보`에서 **각 선택은 바로 앞의 것을 이깁니다.** (바위는 가위를, 보는 바위를, 가위는 보를)
그래서 두 번호의 차이를 3으로 나눈 나머지가 1이면 이김, 2이면 짐이 됩니다. 원형(순환) 구조를 나머지 연산으로 표현한 것입니다.

## 실습 활동

1. `02_rps_basic.py`를 '먼저 3승' 하는 규칙으로 바꿔 보세요. 몇 군데를 고쳐야 하나요?
2. 내가 낸 선택을 모두 리스트 `my_picks`에 기록하고, 게임이 끝나면 출력해 보세요.
3. 선택지에 '도마뱀', '스팍'을 추가한 5가지 가위바위보는 `% 5`로 판정할 수 있을까요? 모둠별로 토의해 보세요.

활동지: [ws05-list-random.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws05-list-random.md)

## 확인 퀴즈

**Q1.** `a = [10, 20, 30]`일 때 `a[1]`의 값은?

- ① 10
- ② 20
- ③ 30
- ④ 오류

**Q2.** `random.randint(1, 6)`이 돌려줄 수 **없는** 값은?

- ① 1
- ② 3
- ③ 6
- ④ 7

**Q3.** 빈 리스트 `h = []`에 `h.append(5)`, `h.append(9)`를 실행한 뒤 `len(h)`는?

- ① 0
- ② 1
- ③ 2
- ④ 9

**Q4.** `"보" not in ["가위", "바위", "보"]`의 결과는?

- ① True
- ② False
- ③ "보"
- ④ 오류

**Q5.** `print("승리" if 3 > 5 else "패배")`의 출력은?

- ① 승리
- ② 패배
- ③ True
- ④ False

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 점수 통계 (기본)

게임 점수 여러 개가 한 줄에 공백으로 주어집니다. 최고 점수, 최저 점수, 평균(소수 첫째 자리까지)을 한 줄에 하나씩 출력하세요.

- 입력: 첫째 줄에 정수 점수들이 공백으로 구분되어 주어진다. (1개 이상)
- 출력: 최고, 최저, 평균을 한 줄에 하나씩

예제 입력 1

```text
70 85 90 65 100
```

예제 출력 1

```text
100
65
82.0
```

예제 입력 2

```text
3 4
```

예제 출력 2

```text
4
3
3.5
```

### 문제 2. 가위바위보 전적 계산 (도전)

첫째 줄에 판 수 n, 다음 n줄에 `나 컴퓨터`의 선택이 주어집니다. 나의 승, 패, 무 횟수를 `○승 ○패 ○무` 형식으로 출력하세요.

- 입력: n과 n줄의 선택
- 출력: `승 패 무` 형식

예제 입력 1

```text
4
바위 가위
가위 가위
보 가위
가위 보
```

예제 출력 1

```text
2승 1패 1무
```

정답과 해설은 **[부록] 06-1-05. 5차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-05-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 리스트: 여러 값을 순서대로, 인덱스는 0부터
- append 추가 · index 위치 · in 포함 여부 · len 개수
- random.randint / choice / sample
- 순환 규칙 → 나머지 연산 % 으로 표현

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `02_rps_basic.py` | [02_rps_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/02_rps_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/02_rps_basic.py) |
| 학습용 PPT | [05-list-random.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/05-list-random.pptx) |
| 학생 활동지 | [ws05-list-random.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws05-list-random.md) |
| 코딩 테스트 1 정답 코드 | [ch05_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch05_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch05_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch05_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch05_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch05_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
