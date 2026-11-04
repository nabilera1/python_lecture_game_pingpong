> **1부 텍스트 게임으로 문제 바라보기** · 4차시 · 6단계 모형: **컴퓨팅 설계**  
> 게임: 업다운 게임 (기본 버전)  
> 핵심 개념: 순서도, 의사코드, while, break, continue, while-else

## 학습 목표

1. 게임 한 판의 흐름을 순서도 또는 의사코드로 설계할 수 있다.
2. while 문과 break, continue를 이용해 반복과 종료 조건을 구현할 수 있다.
3. 업다운 게임 전체 코드를 읽고 각 부분의 역할을 설명할 수 있다.

## 핵심 질문

> **같은 일을 '정답을 맞힐 때까지' 반복하려면 어떻게 설계해야 할까?**

3차시에 만든 판정 코드는 **한 번만** 실행되고 끝납니다. 진짜 게임이 되려면 **기회가 남아 있는 동안 계속 반복**해야 합니다.

코딩을 바로 시작하기보다, 먼저 **순서도**나 **의사코드**로 흐름을 설계하면 '어디서 반복하고, 언제 끝나는지'를 놓치지 않을 수 있습니다.

## 의사코드로 설계하기

의사코드는 프로그래밍 언어처럼 엄격하지 않게, **우리말로 적은 알고리즘**입니다.

```text
정답 ← 1~100 중 무작위 수, 기회 ← 7, 기록 ← 빈 리스트
기회가 0보다 큰 동안 반복:
    입력 ← 사용자 입력
    입력이 숫자가 아니면: "숫자를 입력하세요" 출력 후 처음으로
    기록에 입력 추가, 기회 ← 기회 - 1
    만약 입력 = 정답: "정답" 출력 후 반복 종료
    아니고 입력 < 정답: "UP" 출력, 최솟값 ← 입력 + 1
    아니면: "DOWN" 출력, 최댓값 ← 입력 - 1
반복이 끝까지 돌았으면(정답 못 맞힘): "실패, 정답은 ○○" 출력
```

## 순서도 기호

| 기호 | 모양 | 의미 |
| --- | --- | --- |
| 단말 | 둥근 사각형 | 시작 / 끝 |
| 처리 | 사각형 | 계산, 대입 (기회 ← 기회 - 1) |
| 입출력 | 평행사변형 | 입력받기, 출력하기 |
| 판단 | 마름모 | 조건 검사 (예/아니요로 갈라짐) |
| 흐름선 | 화살표 | 실행 순서 |

마름모(판단)에서 **위로 되돌아가는 화살표**가 생기면 그것이 바로 **반복**입니다.

## while 문과 break, continue

```python
chance = 7
while chance > 0:                # 조건이 참인 동안 반복
    text = input("숫자 > ")
    if not text.isdigit():       # 숫자가 아니면
        print("숫자를 입력하세요!")
        continue                 # 아래를 건너뛰고 반복 처음으로 (기회 유지)
    guess = int(text)
    chance -= 1
    if guess == secret:
        print("정답!")
        break                    # 반복을 즉시 탈출
else:
    print("실패!")               # break 없이 조건이 거짓이 되어 끝났을 때만 실행
```

| 키워드 | 하는 일 |
| --- | --- |
| `while 조건:` | 조건이 참인 동안 반복 |
| `break` | 반복문을 즉시 빠져나감 |
| `continue` | 이번 반복의 나머지를 건너뛰고 다음 반복으로 |
| `while ~ else` | break로 끝나지 **않았을 때만** else 실행 |

**무한 반복 주의!** 조건을 거짓으로 만드는 문장(`chance -= 1`)을 빠뜨리면 기회가 줄지 않아 정답을 맞힐 때까지 끝나지 않습니다. `break`까지 없다면 정말로 영원히 반복됩니다. 이때는 **Ctrl + C**로 멈춥니다.

## 범위 좁히기와 이진 탐색

```python
elif guess < secret:
    low = max(low, guess + 1)     # 정답은 guess 보다 큼 → 최솟값 올리기
else:
    high = min(high, guess - 1)   # 정답은 guess 보다 작음 → 최댓값 내리기
```

항상 **범위의 가운데 값**을 고르면 한 번에 후보가 절반씩 줄어듭니다.
틀릴 때마다 남은 후보 수가 100 → 50 → 25 → 12 → 6 → 3 → 1 로 줄어들어, 6번 틀려도 7번째에는 후보가 1개만 남습니다. 그래서 **최대 7번**이면 반드시 맞힐 수 있습니다. (2⁷ − 1 = 127 ≥ 100)
이 전략을 **이진 탐색**이라고 합니다. 수학의 거듭제곱·로그와 연결되는 아이디어입니다.

## 실습 활동

1. `01_updown_basic.py`를 실행하고 [입력, 처리, 출력, 반복, 종료] 부분에 각각 다른 색으로 표시해 보세요.
2. 기회를 10번, 범위를 1~1000으로 바꿔 보세요. 이진 탐색으로 최대 몇 번이면 맞힐 수 있을까요?
3. `chance -= 1`을 지우면 어떤 일이 생기는지 예상하고 확인해 보세요. 이어서 `break`도 주석 처리하면 어떻게 될까요? (멈추지 않으면 Ctrl + C)

활동지: [ws04-flowchart-while.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws04-flowchart-while.md)

## 확인 퀴즈

**Q1.** 반복문을 즉시 빠져나오게 하는 키워드는?

- ① continue
- ② break
- ③ pass
- ④ return

**Q2.** 다음 코드의 출력 횟수는?

```python
n = 0
while n < 3:
    print(n)
    n += 1
```

- ① 2번
- ② 3번
- ③ 4번
- ④ 무한 번

**Q3.** 순서도에서 조건을 검사하여 흐름을 나누는 기호는?

- ① 사각형
- ② 평행사변형
- ③ 마름모
- ④ 둥근 사각형

**Q4.** `while ~ else`의 else 블록이 실행되는 경우는?

- ① break로 반복이 끝났을 때
- ② 조건이 거짓이 되어 반복이 끝났을 때
- ③ 항상
- ④ continue를 만났을 때

**Q5.** 1~1000 범위에서 이진 탐색으로 반드시 맞히는 데 필요한 최소 기회는?

- ① 7번
- ② 9번
- ③ 10번
- ④ 100번

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 1부터 n까지의 합 (기본)

정수 n을 입력받아 while 문으로 1부터 n까지의 합을 구해 출력하세요.

- 입력: 첫째 줄에 정수 n (1 ≤ n ≤ 10000)
- 출력: 합을 출력한다.

예제 입력 1

```text
10
```

예제 출력 1

```text
55
```

예제 입력 2

```text
100
```

예제 출력 2

```text
5050
```

### 문제 2. 업다운 기록 판정기 (도전)

첫째 줄에 정답, 둘째 줄에 시도 횟수 n, 다음 n줄에 추측한 수가 주어집니다. 각 추측마다 `UP`, `DOWN`을 출력하고, 맞히면 `정답! k번 만에 성공`을 출력한 뒤 끝냅니다. 끝까지 못 맞히면 `실패! 정답은 ○`를 출력하세요.

- 입력: 정답, n, 그리고 n개의 추측 (한 줄에 하나)
- 출력: 판정 결과

예제 입력 1

```text
37
4
50
25
37
90
```

예제 출력 1

```text
DOWN
UP
정답! 3번 만에 성공
```

예제 입력 2

```text
10
2
50
30
```

예제 출력 2

```text
DOWN
DOWN
실패! 정답은 10
```

정답과 해설은 **[부록] 06-1-04. 4차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-04-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 코딩 전에 의사코드·순서도로 반복과 종료 조건을 먼저 설계
- while 조건: 참인 동안 반복 / break 탈출 / continue 건너뛰기
- while ~ else: break 없이 끝났을 때만 else
- 가운데 값 고르기 = 이진 탐색 → 1~100은 최대 7번

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `01_updown_basic.py` | [01_updown_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/01_updown_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/01_updown_basic.py) |
| 학습용 PPT | [04-flowchart-while.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/04-flowchart-while.pptx) |
| 학생 활동지 | [ws04-flowchart-while.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws04-flowchart-while.md) |
| 코딩 테스트 1 정답 코드 | [ch04_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch04_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch04_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch04_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch04_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch04_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
