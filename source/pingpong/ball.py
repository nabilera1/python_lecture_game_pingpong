"""양쪽 패들 사이를 오가는 공을 담당하는 클래스입니다."""

# =====================================================================
# 이 파일(ball.py)은 무슨 역할을 할까요?
# ---------------------------------------------------------------------
# 화면을 날아다니며 벽과 패들에 튕기는 "공"의 설계도예요.
#
# 공이 할 줄 아는 일 (메서드)
#   __init__      : 공을 처음 만들 때 크기, 속도를 정하고 가운데에 놓아요.
#   reset         : 공을 화면 가운데로 되돌리고, 날아갈 방향을 새로 정해요.
#   update        : 한 프레임만큼 공을 움직이고, 위아래 벽에 닿으면 튕겨요.
#   bounce_paddle : 패들에 부딪혔으면 좌우 방향을 반대로 바꿔요.
#   out_on_left   : 공이 왼쪽 밖으로 나갔나? (그러면 오른쪽 플레이어 득점)
#   out_on_right  : 공이 오른쪽 밖으로 나갔나? (그러면 왼쪽 플레이어 득점)
#   draw          : 화면에 공을 동그랗게 그려요.
#
# 핵심 아이디어: "속도(vx, vy)"
#   vx: 가로(x) 방향 속도.  + 이면 오른쪽, - 이면 왼쪽으로 이동
#   vy: 세로(y) 방향 속도.  + 이면 아래쪽, - 이면 위쪽으로 이동
#   매 프레임마다 "위치 = 위치 + 속도"를 하면 공이 움직여요.
#   튕길 때는 속도에 -1을 곱해서 방향만 반대로 바꿔요.
#   (예: vx = 6 → 튕김 → vx = -6, 오른쪽으로 가던 공이 왼쪽으로!)
# =====================================================================

# random: 무작위(랜덤)로 값을 고를 때 쓰는 도구예요. 공의 처음 방향을 정할 때 써요.
import random

# pygame: 게임 만들기 도구 모음
import pygame

# 설정표(constants.py)에서 공 크기, 공 속도, 화면 크기를 가져옵니다.
from constants import BALL_SIZE, BALL_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Ball:
    """일정한 속도로 움직이며 벽과 패들에 튕기는 공입니다."""

    def __init__(self):
        # 공이 만들어질 때 자동으로 한 번 실행되는 준비 함수예요.
        self.size = BALL_SIZE  # 공 크기(16픽셀)
        # 공도 위치와 크기를 직사각형(Rect)으로 기억해요.
        # 화면에는 동그랗게 그리지만, 계산은 "공을 감싸는 네모 상자"로 해요.
        # 처음 위치는 (0, 0)으로 두고, 바로 아래 reset()에서 가운데로 옮겨요.
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.vx = 0  # x 방향 속도
        self.vy = 0  # y 방향 속도
        # random.choice([-1, 1]): -1과 1 중 하나를 무작위로 골라요.
        # → 첫 공이 왼쪽(-1)으로 갈지 오른쪽(1)으로 갈지 랜덤으로 정해져요.
        self.reset(direction=random.choice([-1, 1]))

    def reset(self, direction=1):
        """공을 화면 가운데로 되돌리고 방향을 다시 정합니다."""
        # direction=1: 값을 따로 안 넣으면 기본값 1(오른쪽)을 쓴다는 뜻이에요.

        # 공의 중심을 화면 정중앙으로 옮겨요.
        # // 는 "몫만 구하는 나눗셈"이에요. (예: 800 // 2 = 400, 7 // 2 = 3)
        # 픽셀 좌표는 정수여야 해서 / 대신 // 를 써요.
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # 가로 속도: 6 x 방향  →  오른쪽이면 +6, 왼쪽이면 -6
        self.vx = BALL_SPEED * direction
        # 세로 속도: 위(-6) 또는 아래(+6) 중 랜덤으로 골라요. 그래서 매번 공이 다르게 날아가요.
        self.vy = random.choice([-BALL_SPEED, BALL_SPEED])

    def update(self):
        """한 프레임만큼 공을 이동시키고, 위아래 벽에 닿으면 튕깁니다."""
        # 1) 위치에 속도를 더해서 공을 움직여요. (1초에 60번 실행됨)
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 2) 위아래 벽에 닿았는지 검사해요.
        if self.rect.top <= 0:
            # 공의 윗부분이 화면 위쪽 끝(0)에 닿거나 넘어갔다면
            self.rect.top = 0   # 화면 밖으로 삐져나간 만큼 다시 안으로 넣고
            self.vy *= -1       # 세로 방향을 반대로! (위로 가던 공 → 아래로)
        elif self.rect.bottom >= SCREEN_HEIGHT:
            # 공의 아랫부분이 화면 아래쪽 끝(500)에 닿거나 넘어갔다면
            self.rect.bottom = SCREEN_HEIGHT
            self.vy *= -1       # 아래로 가던 공 → 위로
        # 참고) 왼쪽, 오른쪽 벽에서는 튕기지 않아요. 그쪽으로 나가면 "점수"가 나니까요!

    def bounce_paddle(self, paddle):
        """패들과 겹쳤는지 확인하고, 겹쳤다면 x 방향을 반대로 바꿉니다."""
        # colliderect: 두 직사각형이 서로 겹쳤는지(충돌했는지) True/False로 알려줘요.
        if self.rect.colliderect(paddle.rect):
            # 부딪혔다면 가로 방향을 반대로 바꿔요. (패들에 맞고 되돌아감)
            self.vx *= -1

            # 패들 안쪽에 공이 끼지 않도록 살짝 밀어 줍니다.
            # (안 밀어 주면 다음 프레임에도 계속 겹쳐 있어서 방향이 계속 뒤집히며 덜덜 떨 수 있어요.)
            if self.vx > 0:
                # 이제 오른쪽으로 가야 한다 = 왼쪽 패들에 맞았다
                # → 공의 왼쪽 면을 패들의 오른쪽 면에 딱 붙여요.
                self.rect.left = paddle.rect.right
            else:
                # 이제 왼쪽으로 가야 한다 = 오른쪽 패들에 맞았다
                # → 공의 오른쪽 면을 패들의 왼쪽 면에 딱 붙여요.
                self.rect.right = paddle.rect.left
            return True   # "부딪혔어요"라고 알려줌
        return False      # "안 부딪혔어요"라고 알려줌

    def out_on_left(self):
        """왼쪽 바깥으로 나갔는지 확인합니다. (오른쪽 플레이어 득점)"""
        # 공의 오른쪽 끝까지 화면 왼쪽(0)보다 더 왼쪽에 있으면 = 완전히 나감
        # 비교식(<)의 결과인 True 또는 False를 그대로 돌려줘요.
        return self.rect.right < 0

    def out_on_right(self):
        """오른쪽 바깥으로 나갔는지 확인합니다. (왼쪽 플레이어 득점)"""
        # 공의 왼쪽 끝까지 화면 오른쪽(800)보다 더 오른쪽에 있으면 = 완전히 나감
        return self.rect.left > SCREEN_WIDTH

    def draw(self, screen, color):
        """화면에 공을 원으로 그립니다."""
        # ellipse: 타원을 그리는 함수예요.
        # 정사각형(16 x 16) 안에 타원을 그리면 동그란 원이 돼요.
        pygame.draw.ellipse(screen, color, self.rect)
