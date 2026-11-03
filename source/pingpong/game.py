"""게임 전체 흐름을 관리하는 클래스입니다."""

# =====================================================================
# 이 파일(game.py)은 무슨 역할을 할까요?
# ---------------------------------------------------------------------
# 게임 전체를 지휘하는 "감독"이에요.
# 패들(paddle.py), 공(ball.py), 점수판(scoreboard.py)을 불러 모아서
# 언제 움직이고, 언제 점수를 주고, 언제 그릴지 정해 줘요.
#
# Game 클래스의 메서드(할 줄 아는 일)
#   __init__         : 게임 창을 만들고 패들 2개, 공, 점수판을 준비해요.
#   handle_events    : 창 닫기, ESC, R 키처럼 "한 번 누르는" 입력을 처리해요.
#   restart          : 점수와 공을 처음 상태로 되돌려요.
#   update           : 패들과 공을 움직이고, 득점과 승리를 판정해요.
#   draw_center_line : 가운데 점선을 그려요.
#   draw             : 화면 전체를 순서대로 그려요.
#   run              : 위 과정을 게임이 끝날 때까지 계속 반복해요. (게임 루프)
#
# 게임 루프 (run 함수 안, 1초에 60번 반복)
#   +--------------------------------------------------+
#   | (1) handle_events : 키보드/마우스 입력 확인       |
#   | (2) update        : 패들, 공 움직이기 + 점수 판정 |
#   | (3) draw          : 바뀐 모습을 화면에 그리기     |
#   | (4) clock.tick    : 속도 조절 (60 FPS)            |
#   +--------------------------------------------------+
#              ↑                                  |
#              +------ self.running 이 True인 동안 반복
#
# 거의 모든 게임이 이 "입력 → 업데이트 → 그리기" 구조로 만들어져요!
# =====================================================================

# pygame: 게임 만들기 도구 모음 (창 만들기, 그림 그리기, 키보드 입력 등)
import pygame

# 다른 파일에 만들어 둔 설계도(클래스)와 설정값들을 가져와요.
from ball import Ball
# 괄호 ( ) 로 감싸면 가져올 이름이 많을 때 여러 줄로 나눠 쓸 수 있어요.
from constants import (
    BALL_COLOR,
    BLACK,
    FPS,
    GRAY,
    LEFT_COLOR,
    PADDLE_HEIGHT,
    PADDLE_MARGIN,
    PADDLE_WIDTH,
    RIGHT_COLOR,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WIN_SCORE,
)
from paddle import Paddle
from scoreboard import Scoreboard


class Game:
    """화면, 패들, 공, 점수를 모아 한 판의 게임을 진행합니다."""

    # -----------------------------------------------------------------
    # 게임 준비 (main.py에서 Game()을 실행하면 자동으로 호출됨)
    # -----------------------------------------------------------------
    def __init__(self):
        pygame.init()   # pygame을 사용할 준비를 해요. (게임기 전원 켜기)
        pygame.display.set_caption("클래스 기반 핑퐁")   # 창 맨 위 제목 표시줄에 나올 글자
        # 가로 800, 세로 500 크기의 게임 창을 만들어요.
        # self.screen 은 앞으로 모든 그림을 그릴 "도화지" 역할을 해요.
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Clock: 게임 속도를 일정하게 맞춰 주는 "시계"예요.
        # 이게 없으면 빠른 컴퓨터에서는 게임이 너무 빨라지고, 느린 컴퓨터에서는 느려져요.
        self.clock = pygame.time.Clock()
        # running: 게임이 계속 돌아가야 하는지 기억하는 스위치예요.
        # True면 계속, False가 되면 게임 루프가 멈추고 게임이 끝나요.
        self.running = True

        # 왼쪽 패들: W(위), S(아래)
        # Paddle 설계도로 왼쪽 패들을 만들어요.
        #   x: 화면 왼쪽에서 30픽셀(PADDLE_MARGIN) 떨어진 곳
        #   y: 세로 가운데에 오도록 계산
        #      "화면 높이의 절반(250) - 패들 높이의 절반(45) = 205"
        #      → 패들의 윗변이 205에 있으면 패들의 한가운데가 화면 가운데(250)에 와요.
        self.left_paddle = Paddle(
            x=PADDLE_MARGIN,
            y=SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,
            color=LEFT_COLOR,
            # 딕셔너리(dictionary): {"이름": 값} 형태로 짝을 지어 저장해요.
            # "up" 키는 W, "down" 키는 S 라고 짝지어 패들에게 알려줘요.
            keys={"up": pygame.K_w, "down": pygame.K_s},
        )
        # 오른쪽 패들: 위 화살표, 아래 화살표
        #   x: "화면 가로(800) - 여백(30) - 패들 두께(14) = 756"
        #      → 패들의 오른쪽 면이 화면 오른쪽 끝에서 정확히 30픽셀 떨어지게 돼요.
        #      (x는 패들의 "왼쪽" 면 위치라서 두께만큼 더 빼 줘야 해요.)
        self.right_paddle = Paddle(
            x=SCREEN_WIDTH - PADDLE_MARGIN - PADDLE_WIDTH,
            y=SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,
            color=RIGHT_COLOR,
            keys={"up": pygame.K_UP, "down": pygame.K_DOWN},
        )

        self.ball = Ball()              # 공 만들기 (화면 가운데에서 시작)
        self.scoreboard = Scoreboard()  # 점수판 만들기 (0 : 0)
        self.message = "먼저 5점을 내면 승리합니다."   # 화면 가운데에 보여줄 안내 문구

    # -----------------------------------------------------------------
    # (1) 입력 처리
    # -----------------------------------------------------------------
    def handle_events(self):
        """창 닫기, R 키 재시작 같은 한 번 누르는 입력을 처리합니다."""
        # 이벤트(event): 사용자가 한 행동(키를 누름, 창 닫기 버튼 클릭 등)이에요.
        # pygame.event.get(): 지난 프레임 이후 생긴 이벤트를 목록으로 모두 가져와요.
        # for 문으로 하나씩 꺼내서 어떤 이벤트인지 확인해요.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 창의 X(닫기) 버튼을 눌렀다면 → 스위치를 꺼서 게임 종료
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # 키보드 키를 "누른 순간"이라면 → 어떤 키인지 확인
                if event.key == pygame.K_ESCAPE:
                    # ESC 키 → 게임 종료
                    self.running = False
                elif event.key == pygame.K_r:
                    # R 키 → 처음부터 다시 시작
                    self.restart()
        # 참고) 패들 이동(W/S, ↑/↓)은 여기서 처리하지 않아요.
        #   패들은 키를 "누르고 있는 동안" 계속 움직여야 하므로
        #   update()에서 pygame.key.get_pressed()로 따로 확인해요.

    def restart(self):
        """점수와 공 위치를 처음 상태로 되돌립니다."""
        self.scoreboard.reset()   # 점수를 0 : 0으로
        self.ball.reset()         # 공을 화면 가운데로
        self.message = "새 게임을 시작합니다."

    # -----------------------------------------------------------------
    # (2) 상태 업데이트 (움직이기 + 판정)
    # -----------------------------------------------------------------
    def update(self):
        """승자가 아직 없을 때만 패들과 공을 움직입니다."""
        # 이미 승자가 있으면 아무것도 움직이지 않고 바로 함수를 끝내요. (return)
        # winner()는 "left"/"right"(True처럼 취급) 또는 None(False처럼 취급)을 돌려줘요.
        # → 게임이 끝나면 화면이 멈춘 채로 R 키를 기다리게 돼요.
        if self.scoreboard.winner(WIN_SCORE):
            return

        # 지금 이 순간 눌려 있는 모든 키 상태를 가져와서 양쪽 패들에게 전달해요.
        # 각 패들은 자기 키(W/S 또는 ↑/↓)만 확인해서 움직여요.
        pressed = pygame.key.get_pressed()
        self.left_paddle.handle_input(pressed)
        self.right_paddle.handle_input(pressed)

        # 공을 한 칸 움직이고(위아래 벽 튕김 포함),
        # 양쪽 패들에 부딪혔는지 확인해서 튕겨 보내요.
        self.ball.update()
        self.ball.bounce_paddle(self.left_paddle)
        self.ball.bounce_paddle(self.right_paddle)

        # 공이 화면 밖으로 나가면 상대방이 점수를 얻습니다.
        if self.ball.out_on_left():
            # 왼쪽으로 나감 = 왼쪽 플레이어가 못 막음 → 오른쪽 +1점
            self.scoreboard.add_point("right")
            # 공을 가운데로 되돌리고 오른쪽(1)으로 보내요. (점수 잃은 쪽 반대편으로 출발)
            self.ball.reset(direction=1)
        elif self.ball.out_on_right():
            # 오른쪽으로 나감 = 오른쪽 플레이어가 못 막음 → 왼쪽 +1점
            self.scoreboard.add_point("left")
            self.ball.reset(direction=-1)   # 왼쪽(-1)으로 출발

        # 이번 득점으로 승자가 생겼는지 확인하고, 생겼다면 안내 문구를 바꿔요.
        winner = self.scoreboard.winner(WIN_SCORE)
        if winner == "left":
            self.message = "왼쪽 플레이어 승리!  R 키로 다시 시작"
        elif winner == "right":
            self.message = "오른쪽 플레이어 승리!  R 키로 다시 시작"

    # -----------------------------------------------------------------
    # (3) 화면 그리기
    # -----------------------------------------------------------------
    def draw_center_line(self):
        """경기장을 좌우로 나누는 점선을 그립니다."""
        dash_height = 16   # 점선 한 조각의 길이
        gap = 12           # 조각과 조각 사이 빈칸
        x = SCREEN_WIDTH // 2   # 화면 가로 정가운데(400)
        y = 0                   # 맨 위에서부터 시작
        # while 문: 조건이 참인 동안 계속 반복해요.
        # y가 화면 아래 끝(500)에 닿을 때까지 "선 조각 그리기 → 아래로 이동"을 반복
        while y < SCREEN_HEIGHT:
            # (x, y)에서 (x, y + 16)까지 회색, 두께 3짜리 선을 그려요.
            pygame.draw.line(self.screen, GRAY, (x, y), (x, y + dash_height), 3)
            y += dash_height + gap   # 다음 조각 위치로: 16 + 12 = 28픽셀 아래

    def draw(self):
        """배경, 점수, 패들, 공을 순서대로 그립니다."""
        # 그리는 "순서"가 중요해요! 나중에 그린 것이 위에 덮여서 보여요. (그림 위에 스티커 붙이기)
        self.screen.fill(BLACK)   # 1) 화면 전체를 배경색으로 칠해서 지난 프레임 그림을 지워요.
        self.draw_center_line()   # 2) 가운데 점선
        self.scoreboard.draw(self.screen, self.message)   # 3) 점수와 안내 문구
        self.left_paddle.draw(self.screen)    # 4) 왼쪽 패들
        self.right_paddle.draw(self.screen)   # 5) 오른쪽 패들
        self.ball.draw(self.screen, BALL_COLOR)   # 6) 공 (맨 위에 보이도록 마지막에)
        # 지금까지는 "보이지 않는 도화지"에 그린 거예요.
        # flip()을 해야 완성된 그림이 실제 화면에 한 번에 나타나요. (깜빡임 방지)
        pygame.display.flip()

    # -----------------------------------------------------------------
    # 게임 루프: main.py에서 game.run()을 부르면 여기서 게임이 돌아가요.
    # -----------------------------------------------------------------
    def run(self):
        """게임이 끝날 때까지 '입력 → 업데이트 → 그리기'를 반복합니다."""
        # self.running 이 True인 동안 계속 반복 (ESC나 창 닫기를 하면 False가 됨)
        while self.running:
            self.handle_events()   # (1) 입력 확인
            self.update()          # (2) 움직이기 + 점수 판정
            self.draw()            # (3) 화면 그리기
            # (4) 1초에 최대 60번(FPS)만 반복하도록 필요한 만큼 잠깐 기다려요.
            self.clock.tick(FPS)
        # 반복이 끝나면(게임 종료) pygame을 정리하고 창을 닫아요.
        pygame.quit()
