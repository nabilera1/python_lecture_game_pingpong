> **4부 클래스로 만드는 핑퐁 게임** · 15차시 · 6단계 모형: **구현**  
> 게임: 핑퐁 2단계 (step2_paddle_class.py) · paddle.py  
> 핵심 개념: get_pressed, KEYDOWN 이벤트, 딕셔너리 매개변수, Rect.top/bottom, clamp, 캡슐화

## 학습 목표

1. 이벤트 방식 입력과 키 상태 방식 입력의 차이를 설명할 수 있다.
2. 딕셔너리로 조작 키를 전달하여 하나의 클래스로 서로 다른 패들을 만들 수 있다.
3. 경계 처리(clamp)로 객체가 화면 밖으로 나가지 않게 할 수 있다.

## 핵심 질문

> **같은 Paddle 클래스인데 어떻게 왼쪽은 W/S, 오른쪽은 ↑/↓로 움직일까?**

패들은 **키를 누르고 있는 동안** 계속 움직여야 합니다. 반면 R(재시작)이나 ESC(종료)는 **누른 순간 한 번**만 처리하면 됩니다. pygame은 이 두 가지 입력 방식을 모두 제공합니다.

## 두 가지 입력 방식

| 방식 | 코드 | 언제? | 핑퐁 게임 |
| --- | --- | --- | --- |
| 이벤트 | `for event in pygame.event.get():` → `event.type == pygame.KEYDOWN` | 누른 **순간 한 번** | R 재시작, ESC 종료 (`Game.handle_events`) |
| 키 상태 | `pressed = pygame.key.get_pressed()` → `pressed[pygame.K_w]` | 누르고 **있는 동안 계속** | 패들 이동 (`Paddle.handle_input`) |

## handle_input: 자기 키만 보고 움직이기

```python
def handle_input(self, pressed):
    # self.keys 예: {"up": pygame.K_w, "down": pygame.K_s}
    if pressed[self.keys["up"]]:
        self.rect.y -= self.speed      # 위로 = y 감소
    if pressed[self.keys["down"]]:
        self.rect.y += self.speed

    # 경계 처리: 화면 밖으로 넘어가면 끝에 딱 붙이기
    if self.rect.top < 0:
        self.rect.top = 0
    if self.rect.bottom > SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
```

`Game.update()`는 키 상태를 **한 번** 읽어 두 패들에게 똑같이 넘깁니다. 각 패들은 **자기 키만** 확인합니다.

```python
pressed = pygame.key.get_pressed()
self.left_paddle.handle_input(pressed)    # W/S 만 확인
self.right_paddle.handle_input(pressed)   # ↑/↓ 만 확인
```

## Rect의 편리한 속성

```text
           left        right
            │            │
   top ─────┌────────────┐
            │   center   │   rect = pygame.Rect(30, 205, 14, 90)
            │            │   rect.top    = 205
 bottom ────└────────────┘   rect.bottom = 205 + 90 = 295
```

`rect.bottom = 500`처럼 **아래쪽 변의 위치를 대입**하면 pygame이 y를 자동으로 `500 - 90 = 410`으로 계산합니다.

## 좌표 계산 (수학 연계)

```python
# 세로 가운데: 화면 높이의 절반 - 패들 높이의 절반
y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2     # 250 - 45 = 205

# 오른쪽 패들 x: 화면 가로 - 여백 - 패들 두께
x = SCREEN_WIDTH - PADDLE_MARGIN - PADDLE_WIDTH  # 800 - 30 - 14 = 756
```

x는 패들의 **왼쪽 변** 위치이므로 두께만큼 더 빼야 오른쪽 여백이 정확히 30이 됩니다.

## 실습 활동

1. `step2_paddle_class.py`에 세 번째 패들(초록색, I/K 키)을 한 줄로 추가해 보세요.
2. Shift를 누르고 있으면 패들이 2배 빠르게 움직이도록 `handle_input`을 고쳐 보세요. (힌트: `pressed[pygame.K_LSHIFT]`)
3. 패들이 좌우로도 움직이게 하려면 무엇을 추가해야 할까요? 단, 가운데 선을 넘지 못하게!

활동지: [ws15-paddle.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws15-paddle.md)

## 확인 퀴즈

**Q1.** 키를 누르고 있는 동안 계속 움직이게 하려면 어떤 방식을 써야 하는가?

- ① KEYDOWN 이벤트
- ② pygame.key.get_pressed()
- ③ input()
- ④ pygame.QUIT

**Q2.** `rect = pygame.Rect(30, 205, 14, 90)`일 때 `rect.bottom`은?

- ① 205
- ② 219
- ③ 295
- ④ 90

**Q3.** 왼쪽·오른쪽 패들이 같은 클래스인데 다른 키로 움직이는 이유는?

- ① 클래스가 2개라서
- ② 객체를 만들 때 keys 딕셔너리를 다르게 넘겨서
- ③ pygame이 자동으로 정해서
- ④ 전역 변수 때문

**Q4.** 패들의 경계 처리 코드 `if self.rect.top < 0: self.rect.top = 0`의 의미는?

- ① 패들을 맨 아래로 보낸다
- ② 윗변이 화면 위로 넘어가면 0에 붙인다
- ③ 패들을 지운다
- ④ 속도를 0으로 만든다

**Q5.** 화면 높이 500, 패들 높이 90일 때 패들 y의 최댓값은?

- ① 500
- ② 410
- ③ 455
- ④ 90

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. clamp 함수 (기본)

`clamp(value, low, high)` 함수를 만드세요. value가 low보다 작으면 low, high보다 크면 high, 아니면 value를 돌려줍니다. 첫째 줄에 low high, 둘째 줄에 값들이 공백으로 주어질 때 각 결과를 공백으로 구분해 출력하세요.

- 입력: low high, 값들
- 출력: clamp 결과들

예제 입력 1

```text
0 410
-20 205 500 410 0
```

예제 출력 1

```text
0 205 410 410 0
```

### 문제 2. 패들 이동 기록 (도전)

화면 높이 H, 패들 높이 PH, 속도 S, 처음 top 좌표 Y가 첫째 줄에 주어지고, 둘째 줄에 프레임마다 눌린 키가 문자열로 주어집니다. (`U` 위, `D` 아래, `N` 없음, `B` 위아래 동시) 각 프레임 후 top 좌표를 공백으로 구분해 출력하세요. 한 프레임에서는 위·아래 이동을 모두 먼저 적용한 뒤 마지막에 한 번만 top을 0 이상 H-PH 이하로 제한합니다. (그래서 B는 항상 제자리입니다.)

- 입력: H PH S Y, 키 문자열
- 출력: 프레임별 top 좌표

예제 입력 1

```text
500 90 7 205
UUNDB
```

예제 출력 1

```text
198 191 191 198 198
```

예제 입력 2

```text
100 90 7 5
UDD
```

예제 출력 2

```text
0 7 10
```

정답과 해설은 **[부록] 06-1-15. 15차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-15-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 이벤트(KEYDOWN) = 누른 순간 한 번 / get_pressed = 누르는 동안 계속
- keys 딕셔너리로 객체마다 다른 조작 키
- 경계 처리(clamp): rect.top ≥ 0, rect.bottom ≤ 화면 높이
- 좌표 계산: 가운데 = 화면/2 - 크기/2

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `step2_paddle_class.py` | [step2_paddle_class.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/steps/step2_paddle_class.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/steps/step2_paddle_class.py) |
| 소스코드 `paddle.py` | [paddle.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/paddle.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/paddle.py) |
| 학습용 PPT | [15-paddle.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/15-paddle.pptx) |
| 학생 활동지 | [ws15-paddle.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws15-paddle.md) |
| 코딩 테스트 1 정답 코드 | [ch15_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch15_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch15_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch15_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch15_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch15_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
