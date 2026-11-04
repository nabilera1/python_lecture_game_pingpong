> **3부 함수와 자료구조로 게임 다듬기** · 9차시 · 6단계 모형: **구현**  
> 게임: 가위바위보 (함수 버전)  
> 핵심 개념: 딕셔너리, 키, 값, keys(), values(), items(), get()

## 학습 목표

1. 딕셔너리를 만들고 키로 값을 읽고 수정할 수 있다.
2. 게임 규칙과 점수를 딕셔너리로 표현하여 조건문을 단순하게 만들 수 있다.
3. 딕셔너리의 keys, values, items를 반복문과 함께 활용할 수 있다.

## 핵심 질문

> **'무엇이 무엇을 이긴다'는 규칙을 if 문 대신 데이터로 적을 수 있을까?**

리스트는 **번호**로 값을 찾습니다. 그런데 "가위가 이기는 상대는?"처럼 **이름으로 찾고 싶을 때**는 **딕셔너리**가 편리합니다.

규칙을 딕셔너리라는 **데이터**로 적어 두면, 규칙이 바뀌어도 데이터만 고치면 됩니다. 이것이 좋은 **모델링**입니다.

## 딕셔너리 기본

```python
BEATS = {"가위": "보", "바위": "가위", "보": "바위"}   # {키: 값}
print(BEATS["가위"])          # 보

score = {"win": 0, "lose": 0}
score["win"] += 1             # 값 수정 → {'win': 1, 'lose': 0}
score["draw"] = 0             # 새 키 추가
print("win" in score)         # True  (키가 있는지)
print(score.get("tie", 0))    # 0     (없으면 기본값)

for key, value in score.items():
    print(key, value)
```

| 리스트 | 딕셔너리 |
| --- | --- |
| `[값, 값, ...]` | `{키: 값, 키: 값, ...}` |
| 번호(0, 1, 2...)로 찾기 | 키(이름)로 찾기 |
| 순서가 중요한 기록 | 이름표가 중요한 정보 |

## 규칙을 데이터로: 판정 함수

```python
CHOICES = ["가위", "바위", "보"]
BEATS = {"가위": "보", "바위": "가위", "보": "바위"}          # 이기는 쪽: 지는 쪽
RESULT_TEXT = {"draw": "비겼어요!", "win": "이겼다!", "lose": "졌다..."}

def judge(me, cpu):
    if me == cpu:
        return "draw"
    return "win" if BEATS[me] == cpu else "lose"
```

`BEATS[me]`는 "내가 낸 것이 이기는 상대"입니다. 그것이 컴퓨터의 선택과 같으면 내가 이깁니다.

## 점수판도 딕셔너리로

```python
def play_match():
    score = {"win": 0, "lose": 0}
    while max(score.values()) < 2:            # 누군가 2승할 때까지
        me, cpu = get_pick(), random.choice(CHOICES)
        result = judge(me, cpu)               # "win" / "lose" / "draw"
        print(f"나: {me} vs 컴퓨터: {cpu} → {RESULT_TEXT[result]}")
        if result != "draw":
            score[result] += 1                # 결과 문자열을 그대로 키로!
    return score["win"] == 2
```

`score[result] += 1` 한 줄이 `if result == "win": ... elif result == "lose": ...`를 대신합니다.

## 코드 흐름 따라가기

프로그램을 실행하면 아래 순서로 함수가 호출되고 값이 오갑니다. 전체 코드를 옆에 띄워 놓고 한 줄씩 따라가 보세요.

| 순서 | 실행되는 곳 | 하는 일 |
| --- | --- | --- |
| 1 | 맨 위 상수 | `CHOICES`(선택지 리스트), `BEATS`(누가 누구를 이기나), `RESULT_TEXT`(결과 문구) 딕셔너리를 만든다. |
| 2 | `main()` | 전적 `wins`, `games`를 0으로 두고 경기를 반복한다. |
| 3 | `main()` → `play_match()` | 점수 딕셔너리 `score = {"win": 0, "lose": 0}`를 만들고, `max(score.values()) < 2`인 동안 라운드를 반복한다. |
| 4 | `play_match()` → `get_pick()` | 가위·바위·보 중 하나가 들어올 때까지 다시 묻고 돌려준다. 컴퓨터는 `random.choice(CHOICES)`. |
| 5 | `play_match()` → `judge(me, cpu)` | 같으면 `"draw"`, `BEATS[me] == cpu`이면 `"win"`, 아니면 `"lose"`. |
| 6 | `play_match()` | `RESULT_TEXT[result]`로 문구를 출력하고, 비김이 아니면 `score[result] += 1`. 누군가 2승하면 반복이 끝나고 `score["win"] == 2`(True/False)를 돌려준다. |
| 7 | `main()` | 결과에 따라 승리/패배를 출력하고 전적을 보여 준 뒤 "또 할까요?"를 묻는다. |

**딕셔너리 3개가 하는 일**

| 딕셔너리 | 키 → 값 | 덕분에 사라진 코드 |
| --- | --- | --- |
| `BEATS` | 내 선택 → 내가 이기는 상대 | 승패를 따지는 if 문 여러 개 |
| `RESULT_TEXT` | 결과 코드 → 출력 문구 | 결과마다 print 하는 if 문 |
| `score` | 결과 코드 → 횟수 | 승·패 점수를 따로 올리는 if 문 |

## 실행 예시

`06_rps_func.py`를 실행했을 때의 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. (무작위 값이 있어 실행할 때마다 결과가 달라집니다.)

```text
=== 가위바위보 === 먼저 2승 하면 이깁니다!
가위 / 바위 / 보 > 가위
나: 가위  vs  컴퓨터: 가위  →  비겼어요!
현재 점수  나 0 : 0 컴퓨터
가위 / 바위 / 보 > 바위
나: 바위  vs  컴퓨터: 보  →  졌다...
현재 점수  나 0 : 1 컴퓨터
가위 / 바위 / 보 > 보
나: 보  vs  컴퓨터: 보  →  비겼어요!
현재 점수  나 0 : 1 컴퓨터
가위 / 바위 / 보 > 보
나: 보  vs  컴퓨터: 가위  →  졌다...
현재 점수  나 0 : 2 컴퓨터
아쉽게 패배...
전적: 1경기 0승
또 할까요? (y/n) > n
```

## 전체 코드

지금까지 조각으로 살펴본 코드를 하나로 합친 **전체 프로그램**입니다. 아래 순서로 바로 실행할 수 있습니다.

1. 코드 블록 전체를 복사합니다. (위키독스 코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### 06_rps_func.py

```python
"""가위바위보 (함수 버전) - 9차시: 딕셔너리, 함수, 반환값, main() 구조

실행 방법: python 06_rps_func.py
"""

# =====================================================================
# 딕셔너리(dictionary)란?
#   {키: 값} 짝을 모아 둔 자료구조예요. "이름표를 붙인 사물함"과 비슷해요.
#   BEATS["가위"] → "보"   : 가위가 이기는 상대는 보
#   score["win"] += 1      : "win" 사물함의 숫자를 1 올림
#
# 리스트는 "번호(인덱스)"로, 딕셔너리는 "이름(키)"으로 값을 찾아요.
# 규칙(누가 누구를 이기나)을 데이터로 적어 두면 if 문이 훨씬 짧아져요!
# =====================================================================

import random

CHOICES = ["가위", "바위", "보"]
BEATS = {"가위": "보", "바위": "가위", "보": "바위"}          # 이기는 쪽: 지는 쪽
RESULT_TEXT = {"draw": "비겼어요!", "win": "이겼다!", "lose": "졌다..."}

def get_pick():
    """올바른 선택이 입력될 때까지 다시 물어본다"""
    while True:
        pick = input("가위 / 바위 / 보 > ")
        if pick in CHOICES:
            return pick
        print("가위, 바위, 보 중에서 입력하세요!")

def judge(me, cpu):
    """'draw' / 'win' / 'lose' 중 하나를 돌려준다"""
    if me == cpu:
        return "draw"
    # BEATS[me] : 내가 낸 것이 이기는 상대. 그게 컴퓨터가 낸 것과 같으면 내가 이김
    return "win" if BEATS[me] == cpu else "lose"

def play_match():
    """먼저 2승 하면 끝나는 한 경기. 내가 이기면 True를 돌려준다"""
    score = {"win": 0, "lose": 0}
    # score.values() → 딕셔너리의 값들만 모음 (예: 1, 0). max 로 가장 큰 값 확인
    while max(score.values()) < 2:
        me, cpu = get_pick(), random.choice(CHOICES)
        result = judge(me, cpu)
        print(f"나: {me}  vs  컴퓨터: {cpu}  →  {RESULT_TEXT[result]}")
        if result != "draw":
            score[result] += 1          # 결과 문자열을 그대로 키로 사용!
        print(f"현재 점수  나 {score['win']} : {score['lose']} 컴퓨터")
    return score["win"] == 2            # 비교식의 결과(True/False)를 그대로 반환

def main():
    print("=== 가위바위보 === 먼저 2승 하면 이깁니다!")
    wins = games = 0
    while True:
        games += 1
        if play_match():
            wins += 1
            print("최종 승리!")
        else:
            print("아쉽게 패배...")
        print(f"전적: {games}경기 {wins}승")
        if input("또 할까요? (y/n) > ") != "y":
            break

if __name__ == "__main__":
    main()
```

파일 받기: [06_rps_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/06_rps_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/06_rps_func.py)

## 실습 활동

1. `BEATS`에 '도마뱀', '스팍'을 추가하려면 딕셔너리를 어떻게 바꿔야 할까요? (각 선택이 이기는 상대가 2개 → 값을 리스트로!)
2. `RESULT_TEXT`의 문구를 우리 모둠만의 문구로 바꿔 보세요.
3. 내가 낸 선택의 횟수를 세는 딕셔너리 `count = {"가위": 0, "바위": 0, "보": 0}`를 추가하고 경기 후 출력해 보세요.

활동지: [ws09-dictionary.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws09-dictionary.md)

## 확인 퀴즈

**Q1.** `d = {"a": 1, "b": 2}`일 때 `d["b"]`는?

- ① 1
- ② 2
- ③ "b"
- ④ 오류

**Q2.** 딕셔너리에 없는 키를 `d["z"]`로 읽으면?

- ① None
- ② 0
- ③ KeyError 오류
- ④ 빈 문자열

**Q3.** `BEATS = {"가위": "보", ...}`에서 `BEATS["가위"] == "보"`가 뜻하는 것은?

- ① 가위가 보에게 진다
- ② 가위가 보를 이긴다
- ③ 비긴다
- ④ 알 수 없다

**Q4.** `score = {"win": 1, "lose": 2}`일 때 `max(score.values())`는?

- ① win
- ② lose
- ③ 1
- ④ 2

**Q5.** 딕셔너리의 (키, 값) 쌍을 함께 반복하는 메서드는?

- ① keys()
- ② values()
- ③ items()
- ④ pairs()

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 선택 횟수 세기 (기본)

한 줄에 여러 개의 선택(가위/바위/보)이 공백으로 주어집니다. 가위, 바위, 보 순서로 각각 몇 번 나왔는지 출력하세요.

- 입력: 첫째 줄에 선택들
- 출력: `가위 ○` `바위 ○` `보 ○` 세 줄

예제 입력 1

```text
가위 바위 가위 보 가위
```

예제 출력 1

```text
가위 3
바위 1
보 1
```

예제 입력 2

```text
보
```

예제 출력 2

```text
가위 0
바위 0
보 1
```

### 문제 2. 딕셔너리 판정으로 먼저 2승 (도전)

`BEATS` 딕셔너리로 판정하세요. 첫째 줄에 최대 판 수 n, 다음 줄부터 최대 n줄에 `나 컴퓨터`의 선택이 한 줄씩 주어집니다. 누군가 먼저 2승을 하면 즉시 멈추고 `승리` 또는 `패배`와 `나 ○ : ○ 컴퓨터`를 출력합니다. n판이 끝날 때까지 2승이 없으면 `미정`과 점수를 출력하세요.

- 입력: n, 그리고 최대 n줄의 선택
- 출력: 결과와 점수

예제 입력 1

```text
5
가위 보
바위 보
보 바위
가위 가위
바위 가위
```

예제 출력 1

```text
승리
나 2 : 1 컴퓨터
```

예제 입력 2

```text
2
가위 가위
보 가위
```

예제 출력 2

```text
미정
나 0 : 1 컴퓨터
```

정답과 해설은 **[부록] 06-1-09. 9차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-09-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 딕셔너리 {키: 값} → 이름으로 찾기
- 규칙(BEATS)·문구(RESULT_TEXT)·점수(score)를 데이터로
- 없는 키는 KeyError → in 검사 또는 get()
- items()로 키와 값을 함께 반복

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `06_rps_func.py` | [06_rps_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/06_rps_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/06_rps_func.py) |
| 학습용 PPT | [09-dictionary.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/09-dictionary.pptx) |
| 학생 활동지 | [ws09-dictionary.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws09-dictionary.md) |
| 코딩 테스트 1 정답 코드 | [ch09_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch09_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch09_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch09_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch09_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch09_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
