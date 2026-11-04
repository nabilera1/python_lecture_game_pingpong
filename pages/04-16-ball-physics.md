> **4부 클래스로 만드는 핑퐁 게임** · 16차시 · 6단계 모형: **구현**  
> 게임: 핑퐁 3단계 (step3_ball_bounce.py) · ball.py  
> 핵심 개념: 속도 벡터, 등속 운동, 반사, 부호 반전, 충돌 판정, colliderect, 끼임 방지

## 학습 목표

1. 속도 벡터(vx, vy)로 물체의 등속 운동을 구현할 수 있다.
2. 반사의 원리를 속도 부호 변경으로 모델링할 수 있다.
3. 직사각형 충돌 판정 알고리즘을 설명하고 구현할 수 있다.

## 핵심 질문

> **공이 벽과 패들에 '진짜처럼' 튕기게 하려면 무엇을 계산해야 할까?**

공은 매 프레임 **위치 = 위치 + 속도**로 움직입니다. 벽에 닿으면 **속도의 방향만** 바꾸면 튕기는 것처럼 보입니다. 물리 시간에 배우는 **등속 운동**과 **반사**를 코드로 옮겨 봅니다.

## 속도 벡터와 등속 운동 (물리 연계)

```python
self.vx = BALL_SPEED * direction       # +6 오른쪽 / -6 왼쪽
self.vy = random.choice([-BALL_SPEED, BALL_SPEED])   # 위 또는 아래

def update(self):
    self.rect.x += self.vx              # x 위치 = x + vx
    self.rect.y += self.vy              # y 위치 = y + vy
```

| 물리 | 코드 |
| --- | --- |
| 위치 (x, y) | `self.rect.x`, `self.rect.y` |
| 속도 벡터 (vx, vy) | `self.vx`, `self.vy` |
| 시간 간격 Δt | 1 프레임 (1/60초) |
| 등속 운동 x = x₀ + v·t | 매 프레임 `x += vx` |

`vx`, `vy`의 크기가 같으므로 공은 항상 **45° 대각선**으로 움직입니다.

## 반사 = 부호 바꾸기

```python
if self.rect.top <= 0:                # 위쪽 벽
    self.rect.top = 0                 # 삐져나간 만큼 되돌리기
    self.vy *= -1                     # 세로 방향만 반대로
elif self.rect.bottom >= SCREEN_HEIGHT:
    self.rect.bottom = SCREEN_HEIGHT
    self.vy *= -1
```

```text
   ＼   ／          위/아래 벽: vy → -vy  (vx 는 그대로)
    ＼／            패들(좌/우): vx → -vx  (vy 는 그대로)
 ─────────          입사각 = 반사각, 속력은 그대로
```

왼쪽·오른쪽 벽에서는 튕기지 않습니다. 그쪽으로 나가면 **득점**이기 때문입니다.

## 직사각형 충돌 판정

두 직사각형 A, B가 겹치는 조건은 **가로로도 겹치고, 세로로도 겹치는 것**입니다.

```python
def overlap(a, b):            # a, b = (x, y, w, h)
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah
```

pygame에서는 `self.rect.colliderect(paddle.rect)` 한 줄로 같은 일을 합니다. 이처럼 물체를 감싸는 사각형으로 충돌을 검사하는 방법을 **AABB 충돌 판정**이라고 합니다. 공은 동그랗게 그리지만 계산은 네모로 합니다.

## 끼임 방지: 패들 밖으로 밀어내기

```python
def bounce_paddle(self, paddle):
    if self.rect.colliderect(paddle.rect):
        self.vx *= -1
        if self.vx > 0:                        # 이제 오른쪽으로 = 왼쪽 패들에 맞음
            self.rect.left = paddle.rect.right
        else:                                  # 이제 왼쪽으로 = 오른쪽 패들에 맞음
            self.rect.right = paddle.rect.left
        return True
    return False
```

밀어내지 않으면 다음 프레임에도 겹쳐 있어서 방향이 또 뒤집히고, 공이 패들 안에서 **덜덜 떠는 버그**가 생깁니다. (18차시 테스트에서 직접 확인해 봅니다.)

## 실습 활동

1. `step3_ball_bounce.py`에서 패들에 맞을 때마다 공이 10%씩 빨라지게 해 보세요. 최대 속도도 정해 보세요.
2. `ball.py`의 `bounce_paddle`에서 밀어내기 코드 두 줄을 주석 처리하고 무슨 일이 생기는지 관찰하세요.
3. 패들의 어느 부분에 맞았는지(위·가운데·아래)에 따라 vy를 바꾸는 아이디어를 설계해 보세요.

활동지: [ws16-ball-physics.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws16-ball-physics.md)

## 확인 퀴즈

**Q1.** vx = 6, vy = -6인 공은 어느 방향으로 움직이는가?

- ① 오른쪽 아래
- ② 오른쪽 위
- ③ 왼쪽 위
- ④ 왼쪽 아래

**Q2.** 공이 위쪽 벽에 닿았을 때 바꿔야 하는 값은?

- ① vx만
- ② vy만
- ③ vx와 vy
- ④ 위치만

**Q3.** `a.colliderect(b)`가 True가 되려면?

- ① 가로로만 겹치면 된다
- ② 세로로만 겹치면 된다
- ③ 가로와 세로 모두 겹쳐야 한다
- ④ 같은 크기여야 한다

**Q4.** bounce_paddle에서 공을 패들 밖으로 밀어내는 이유는?

- ① 공을 빠르게 하려고
- ② 다음 프레임에 또 충돌해 방향이 다시 뒤집히는 것을 막으려고
- ③ 점수를 주려고
- ④ 화면을 지우려고

**Q5.** 공의 x축 방향 속력(픽셀/초)은? (vx=6, vy=6, 60 FPS)

- ① 6
- ② 60
- ③ 360
- ④ 720

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 벽에 튕기는 공 (1차원) (기본)

공의 처음 top y, 세로 속도 vy, 공 크기 size, 화면 높이 H, 프레임 수 n이 주어집니다. 매 프레임 `y += vy` 후, top이 0 이하이면 top을 0으로 하고 vy를 반대로, bottom(y+size)이 H 이상이면 bottom을 H로 하고 vy를 반대로 합니다. n프레임 후 `y vy`를 출력하세요.

- 입력: y vy size H n
- 출력: 최종 y와 vy

예제 입력 1

```text
10 -6 16 500 3
```

예제 출력 1

```text
6 6
```

예제 입력 2

```text
470 6 16 500 4
```

예제 출력 2

```text
478 -6
```

### 문제 2. 사각형 충돌 판정 (도전)

각 줄에 두 사각형 `x1 y1 w1 h1 x2 y2 w2 h2`가 주어집니다. 첫째 줄의 n개 테스트마다 두 사각형이 겹치면 `충돌`, 아니면 `통과`를 출력하세요. 변이 딱 맞닿기만 한 경우는 겹치지 않은 것으로 봅니다.

- 입력: n, n줄의 사각형 쌍
- 출력: 충돌/통과

예제 입력 1

```text
3
0 0 10 10 5 5 10 10
0 0 10 10 10 0 5 5
30 205 14 90 40 240 16 16
```

예제 출력 1

```text
충돌
통과
충돌
```

정답과 해설은 **[부록] 06-1-16. 16차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-16-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 위치 = 위치 + 속도 (등속 운동)
- 반사 = 부호 바꾸기: 위/아래 벽 vy, 패들 vx
- AABB 충돌: 가로·세로 모두 겹치면 충돌
- 충돌 후 밀어내기로 끼임 버그 방지

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `step3_ball_bounce.py` | [step3_ball_bounce.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/steps/step3_ball_bounce.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/steps/step3_ball_bounce.py) |
| 소스코드 `ball.py` | [ball.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/ball.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/ball.py) |
| 학습용 PPT | [16-ball-physics.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/16-ball-physics.pptx) |
| 학생 활동지 | [ws16-ball-physics.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws16-ball-physics.md) |
| 코딩 테스트 1 정답 코드 | [ch16_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch16_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch16_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch16_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch16_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch16_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
