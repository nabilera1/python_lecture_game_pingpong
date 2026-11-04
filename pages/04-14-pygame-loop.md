> **4부 클래스로 만드는 핑퐁 게임** · 14차시 · 6단계 모형: **구현**  
> 게임: 핑퐁 1단계 (step1_game_loop.py) · main.py · game.py  
> 핵심 개념: pygame, 게임 루프, 이벤트, FPS, 좌표계, Rect, flip(), Clock

## 학습 목표

1. pygame을 설치하고 창을 띄우는 프로그램을 실행할 수 있다.
2. 게임 루프의 4단계(입력·업데이트·그리기·시간 조절)를 설명할 수 있다.
3. 화면 좌표계와 FPS의 의미를 이해하고 그리기 함수를 사용할 수 있다.

## 핵심 질문

> **그래픽 게임은 어떻게 '멈추지 않고' 계속 움직이는 것처럼 보일까?**

텍스트 게임은 `input()`에서 **사용자를 기다렸습니다.** 그래픽 게임은 기다리지 않고 **1초에 60번** 화면을 새로 그립니다. 그 사이사이에 키보드 상태를 확인할 뿐입니다.

플립북(종이 애니메이션)처럼 **조금 움직이고 → 한 장 그리기**를 아주 빠르게 반복하면 부드럽게 움직이는 것처럼 보입니다. 이 반복 구조를 **게임 루프**라고 합니다.

## pygame 설치와 실행

```bash
pip install pygame          # 또는: pip install -r requirements.txt
python step1_game_loop.py
```

설치 오류가 나면 `python -m pip install pygame`을 시도해 보세요. 학교 컴퓨터는 관리자 권한이 필요할 수 있으니 미리 확인합니다.

## 게임 루프 4단계

```python
pygame.init()
screen = pygame.display.set_mode((800, 500))   # 도화지(창)
clock = pygame.time.Clock()
running = True

while running:
    # (1) 입력: 창 닫기 등 이벤트 확인
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # (2) 업데이트: 눌린 키를 보고 위치 바꾸기
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= speed
    # (3) 그리기: 배경 → 물체 → 화면에 표시
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x, y, 20, 20))
    pygame.display.flip()
    # (4) 시간 조절: 1초에 최대 60번
    clock.tick(60)
pygame.quit()
```

```text
 ┌─▶ (1) 입력 ─▶ (2) 업데이트 ─▶ (3) 그리기 ─▶ (4) 60 FPS 맞추기 ─┐
 └──────────────────── running 이 True 인 동안 ─────────────────────┘
```

거의 모든 게임이 이 **입력 → 업데이트 → 그리기** 구조로 만들어집니다.

## 화면 좌표계

```text
(0, 0) ───────────── x 증가 ─────────▶ (800, 0)
  │
  y 증가 (아래로!)
  │
  ▼
(0, 500)                               (800, 500)
```

- 왼쪽 위가 `(0, 0)`, **아래로 갈수록 y가 커집니다.** (수학 좌표와 반대)
- 그래서 "위로 이동"은 `y -= speed`입니다.
- `pygame.Rect(x, y, 가로, 세로)`는 위치와 크기를 함께 기억하고 `top`, `bottom`, `left`, `right`, `center` 같은 속성을 제공합니다.

## Game 클래스 = 게임 루프를 담은 감독

```python
class Game:
    def run(self):
        while self.running:
            self.handle_events()   # (1) 입력: 창 닫기, ESC, R 키
            self.update()          # (2) 패들·공 이동, 점수 판정
            self.draw()            # (3) 배경 → 점선 → 점수 → 패들 → 공
            self.clock.tick(FPS)   # (4) 60 FPS
        pygame.quit()

# main.py
def main():
    game = Game()   # __init__: 창, 패들 2개, 공, 점수판 준비
    game.run()      # 게임 루프 시작
```

step1에서 한 파일에 모두 적었던 루프를, 핑퐁 완성본에서는 `Game` 클래스의 메서드 3개(`handle_events`·`update`·`draw`)와 이를 반복 호출하는 `run()`으로 **분해**했습니다.

## FPS와 이동 거리 (물리 연계: 속력)

`PADDLE_SPEED = 7`은 **한 프레임에 7픽셀**입니다. 60 FPS이면 1초에 `7 × 60 = 420`픽셀을 움직입니다.

| 값 | 의미 | 단위 |
| --- | --- | --- |
| 속도 | 한 프레임 동안의 이동 거리 | 픽셀/프레임 |
| FPS | 1초 동안의 프레임 수 | 프레임/초 |
| 속도 × FPS | 1초 동안의 이동 거리 (속력) | 픽셀/초 |

`clock.tick(FPS)`가 없으면 빠른 컴퓨터에서는 게임이 너무 빨라지고, 느린 컴퓨터에서는 느려집니다.

## 실습 활동

1. `step1_game_loop.py`에서 네모가 화면 밖으로 나가지 않게 if 문 4개를 추가해 보세요.
2. `clock.tick(60)`을 `clock.tick(10)`으로 바꿔 보고 차이를 설명해 보세요.
3. `screen.fill(BLACK)`을 지우면 어떤 일이 생기나요? 왜 그럴까요?

활동지: [ws14-pygame-loop.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws14-pygame-loop.md)

## 확인 퀴즈

**Q1.** pygame 화면 좌표에서 아래로 갈수록 커지는 값은?

- ① x
- ② y
- ③ x와 y 모두
- ④ 없음

**Q2.** 게임 루프의 순서로 알맞은 것은?

- ① 그리기 → 입력 → 업데이트
- ② 입력 → 업데이트 → 그리기
- ③ 업데이트 → 그리기 → 입력
- ④ 입력 → 그리기 → 업데이트

**Q3.** 속도 5픽셀/프레임, 60 FPS일 때 2초 동안 이동 거리는?

- ① 120픽셀
- ② 300픽셀
- ③ 600픽셀
- ④ 10픽셀

**Q4.** `pygame.display.flip()`의 역할은?

- ① 화면을 뒤집는다
- ② 그린 그림을 실제 화면에 표시한다
- ③ 창을 닫는다
- ④ 키 입력을 받는다

**Q5.** 매 프레임 `screen.fill(BLACK)`을 하는 이유는?

- ① 색을 바꾸려고
- ② 이전 프레임의 그림을 지우려고
- ③ FPS를 맞추려고
- ④ 이벤트를 처리하려고

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 프레임 이동 시뮬레이션 (기본)

물체의 처음 y좌표, 프레임당 속도(위로 이동이면 음수), 프레임 수 n이 한 줄에 주어집니다. n프레임 후 y좌표를 출력하되, y는 0 이상 화면 높이 500 이하로 제한(clamp)합니다.

- 입력: y speed n
- 출력: 최종 y

예제 입력 1

```text
250 7 10
```

예제 출력 1

```text
320
```

예제 입력 2

```text
100 -7 30
```

예제 출력 2

```text
0
```

예제 입력 3

```text
480 5 10
```

예제 출력 3

```text
500
```

### 문제 2. 가운데 점선 좌표 만들기 (도전)

화면 높이 H, 점선 한 조각 길이 D, 빈칸 G가 주어집니다. `game.py`의 `draw_center_line()`처럼 y=0부터 시작해 y < H인 동안 조각을 그릴 때, 각 조각의 시작 y와 끝 y를 `시작-끝` 형식으로 한 줄씩 출력하세요. 끝 y는 시작 y + D입니다.

- 입력: H D G
- 출력: 각 조각의 시작-끝

예제 입력 1

```text
100 16 12
```

예제 출력 1

```text
0-16
28-44
56-72
84-100
```

예제 입력 2

```text
30 10 10
```

예제 출력 2

```text
0-10
20-30
```

정답과 해설은 **[부록] 06-1-14. 14차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-14-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 게임 루프: 입력 → 업데이트 → 그리기 → 시간 조절
- 화면 좌표: 왼쪽 위 (0,0), 아래로 y 증가
- 속도(픽셀/프레임) × FPS = 1초 이동 거리
- Game.run() = 루프, main.py = 시작 버튼

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `step1_game_loop.py` | [step1_game_loop.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/steps/step1_game_loop.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/steps/step1_game_loop.py) |
| 소스코드 `main.py` | [main.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/main.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/main.py) |
| 소스코드 `game.py` | [game.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/game.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/game.py) |
| 소스코드 `constants.py` | [constants.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/constants.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/constants.py) |
| 소스코드 `requirements.txt` | [requirements.txt 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/requirements.txt) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/requirements.txt) |
| 학습용 PPT | [14-pygame-loop.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/14-pygame-loop.pptx) |
| 학생 활동지 | [ws14-pygame-loop.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws14-pygame-loop.md) |
| 코딩 테스트 1 정답 코드 | [ch14_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch14_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch14_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch14_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch14_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch14_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
