> **4부 클래스로 만드는 핑퐁 게임** · 17차시 · 6단계 모형: **구현**  
> 게임: 핑퐁 완성본 (main.py · game.py · scoreboard.py)  
> 핵심 개념: Scoreboard, None, 승패 판정, 가운데 정렬, render/blit, 객체 협력, import

## 학습 목표

1. 득점과 승패 판정 알고리즘을 구현하고 None을 활용할 수 있다.
2. 글자를 화면 가운데에 정렬하는 좌표를 계산할 수 있다.
3. 여러 클래스가 협력하는 프로그램의 구조(모듈·객체 관계)를 설명할 수 있다.

## 핵심 질문

> **여러 객체가 각자 맡은 일을 하면서 하나의 게임이 되려면 누가 무엇을 지휘해야 할까?**

패들과 공이 움직이게 되었으니, 이제 **점수를 매기고 승자를 정하고, R 키로 다시 시작**하는 기능을 더해 게임을 완성합니다. 이 일은 점수판(`Scoreboard`)과 감독(`Game`)이 나누어 맡습니다.

## Scoreboard: 점수를 기억하고 승자를 알려 주기

```python
class Scoreboard:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0

    def add_point(self, side):
        if side == "left":
            self.left_score += 1
        elif side == "right":
            self.right_score += 1

    def winner(self, win_score):
        if self.left_score >= win_score:
            return "left"
        if self.right_score >= win_score:
            return "right"
        return None              # 아직 승자 없음
```

`None`은 "아무것도 없음"을 뜻하는 특별한 값이고, if 문에서는 **False처럼** 취급됩니다. 그래서 `if self.scoreboard.winner(WIN_SCORE):`로 "승자가 있으면"을 간단히 쓸 수 있습니다.

## Game.update: 득점과 승패 판정

```python
def update(self):
    if self.scoreboard.winner(WIN_SCORE):     # 승자가 있으면 아무것도 움직이지 않음
        return
    ...                                       # 패들 이동, 공 이동, 튕기기
    if self.ball.out_on_left():               # 왼쪽으로 나감 → 오른쪽 득점
        self.scoreboard.add_point("right")
        self.ball.reset(direction=1)          # 오른쪽으로 다시 출발
    elif self.ball.out_on_right():
        self.scoreboard.add_point("left")
        self.ball.reset(direction=-1)

    winner = self.scoreboard.winner(WIN_SCORE)
    if winner == "left":
        self.message = "왼쪽 플레이어 승리!  R 키로 다시 시작"
    elif winner == "right":
        self.message = "오른쪽 플레이어 승리!  R 키로 다시 시작"
```

## 글자 가운데 정렬 (수학 연계)

```python
left_text = self.font.render(str(self.left_score), True, WHITE)   # 글자 → 그림
x = SCREEN_WIDTH // 4 - left_text.get_width() // 2                # 1/4 지점 - 글자 너비 절반
screen.blit(left_text, (x, 20))                                   # 그림 붙이기
```

| 위치 | 중심 x | 계산 (글자 너비 30일 때) |
| --- | --- | --- |
| 왼쪽 점수 | 800 // 4 = 200 | 200 - 15 = 185 |
| 오른쪽 점수 | 800 * 3 // 4 = 600 | 600 - 15 = 585 |
| 안내 문구 | 800 // 2 = 400 | 400 - (너비 // 2) |

`blit`은 그림의 **왼쪽 위** 좌표를 받으므로 '중심 - 너비의 절반'을 해야 가운데에 옵니다.

안내 문구 `"왼쪽: W / S    오른쪽: ↑ / ↓    재시작: R"`의 화살표 ↑ ↓는 키보드에 없는 특수 문자입니다. 한글 상태에서 **ㅁ + 한자 키**를 눌러 고르거나, `"\u2191"`(↑), `"\u2193"`(↓)처럼 유니코드로 쓸 수 있습니다. (11차시 '특수 문자 입력하기' 참고)

## 객체들의 협력 구조

```text
main.py ──▶ Game()  ──▶ run()  : 게임 루프
              │
              ├── left_paddle  : Paddle  (W/S)
              ├── right_paddle : Paddle  (↑/↓)
              ├── ball         : Ball
              └── scoreboard   : Scoreboard
                         ▲
        constants.py ────┘ (모든 파일이 설정값을 가져다 씀)
```

`Game`은 직접 공을 움직이지 않습니다. `self.ball.update()`처럼 **각 객체에게 일을 시킬 뿐**입니다. 이렇게 역할을 나누면 공의 움직임을 바꾸고 싶을 때 `ball.py`만 보면 됩니다.

## 실습 활동

1. `WIN_SCORE`를 3으로 바꾸고 안내 문구 `"먼저 5점을 내면 승리합니다."`도 자동으로 바뀌게 f-문자열로 고쳐 보세요.
2. 득점할 때마다 화면 가운데에 `왼쪽 득점!` 문구가 잠깐 보이게 해 보세요.
3. 핑퐁 게임의 클래스 구조도를 활동지에 그려 보세요. (어떤 객체가 어떤 객체를 가지고 있는가?)

활동지: [ws17-scoreboard-game.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws17-scoreboard-game.md)

## 확인 퀴즈

**Q1.** `bool(None)`의 값은?

- ① True
- ② False
- ③ None
- ④ 0

**Q2.** 공이 왼쪽 화면 밖으로 나갔을 때 점수를 얻는 쪽은?

- ① 왼쪽
- ② 오른쪽
- ③ 둘 다
- ④ 없음

**Q3.** 화면 가로 800, 글자 너비 40일 때 화면 가운데 정렬 x는?

- ① 400
- ② 380
- ③ 360
- ④ 420

**Q4.** 승자가 생긴 뒤 화면이 멈추는 이유는?

- ① pygame.quit()이 실행돼서
- ② update()가 승자가 있으면 바로 return해서
- ③ FPS가 0이 돼서
- ④ running이 False가 돼서

**Q5.** Game 클래스가 공을 직접 계산하지 않고 `self.ball.update()`를 부르는 설계의 장점은?

- ① 코드가 길어진다
- ② 역할이 나뉘어 수정할 곳을 찾기 쉽다
- ③ 실행이 빨라진다
- ④ pygame이 요구한다

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 득점 기록으로 승자 정하기 (기본)

첫째 줄에 승리 점수 W, 둘째 줄에 득점 기록(`L` 왼쪽 득점, `R` 오른쪽 득점) 문자열이 주어집니다. 누군가 W점에 도달하면 그 즉시 기록 읽기를 멈추고 `왼쪽 승리` 또는 `오른쪽 승리`와 최종 점수 `○ : ○`를 출력하세요. 끝까지 승자가 없으면 `진행 중`과 점수를 출력하세요.

- 입력: W, 득점 기록
- 출력: 결과와 점수

예제 입력 1

```text
5
LLRLRLLRR
```

예제 출력 1

```text
왼쪽 승리
5 : 2
```

예제 입력 2

```text
3
LRLR
```

예제 출력 2

```text
진행 중
2 : 2
```

### 문제 2. 점수판 배치 계산 (도전)

화면 가로 W와 왼쪽 점수 글자 너비 a, 오른쪽 점수 글자 너비 b, 안내 문구 너비 c가 주어집니다. scoreboard.py와 같은 방식으로 왼쪽 점수(1/4 지점), 오른쪽 점수(3/4 지점), 안내 문구(가운데)의 x 좌표를 한 줄씩 출력하세요. 나눗셈은 모두 몫(//)을 사용합니다.

- 입력: W a b c
- 출력: 세 x 좌표

예제 입력 1

```text
800 30 30 300
```

예제 출력 1

```text
185
585
250
```

예제 입력 2

```text
1000 25 51 333
```

예제 출력 2

```text
238
725
334
```

정답과 해설은 **[부록] 06-1-17. 17차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-17-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- Scoreboard: 점수 기억, winner()는 승자 또는 None
- Game.update: 이동 → 충돌 → 득점 → 승패 판정
- 가운데 정렬 x = 중심 - 너비 // 2
- Game은 지휘만, 일은 각 객체가 (역할 분담)

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `scoreboard.py` | [scoreboard.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/scoreboard.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/scoreboard.py) |
| 소스코드 `game.py` | [game.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/game.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/game.py) |
| 소스코드 `main.py` | [main.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/main.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/main.py) |
| 학습용 PPT | [17-scoreboard-game.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/17-scoreboard-game.pptx) |
| 학생 활동지 | [ws17-scoreboard-game.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws17-scoreboard-game.md) |
| 코딩 테스트 1 정답 코드 | [ch17_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch17_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch17_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch17_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch17_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch17_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
