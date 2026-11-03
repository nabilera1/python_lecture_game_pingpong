"""플레이어가 움직이는 막대(패들)를 담당하는 클래스입니다."""

# =====================================================================
# 이 파일(paddle.py)은 무슨 역할을 할까요?
# ---------------------------------------------------------------------
# 플레이어가 키보드로 위아래로 움직이는 "막대(패들)"의 설계도예요.
#
# 패들이 할 줄 아는 일 (= 메서드, 클래스 안의 함수)
#   __init__     : 처음 만들어질 때 위치, 색, 조작 키를 정해요.
#   handle_input : 눌린 키를 보고 위나 아래로 움직여요. (화면 밖으로는 못 나감)
#   draw         : 화면에 자기 모습을 그려요.
#
# 같은 설계도(Paddle 클래스)로 패들을 2개 만들어요.
#   - 왼쪽 패들 : 하늘색, W/S 키
#   - 오른쪽 패들: 주황색, ↑/↓ 키
#   설계도는 하나인데 위치, 색, 키만 다르게 넣어서 서로 다른 패들이 되는 거예요.
#   (붕어빵 틀 하나로 팥 붕어빵, 슈크림 붕어빵을 만드는 것과 비슷해요.)
# =====================================================================

# pygame: 파이썬으로 게임을 만들 때 쓰는 도구 모음(라이브러리)이에요.
import pygame

# constants.py(설정표)에서 패들 크기, 속도, 화면 높이를 가져옵니다.
from constants import (
    PADDLE_HEIGHT,
    PADDLE_SPEED,
    PADDLE_WIDTH,
    SCREEN_HEIGHT,
)


# class: "설계도"를 만든다는 뜻이에요. 이 설계도 이름은 Paddle입니다.
class Paddle:
    """위아래로 움직이는 직사각형 패들입니다."""

    # __init__: 패들이 새로 만들어질 때 "자동으로" 한 번 실행되는 준비 함수예요.
    # self: "만들어지는 패들 자기 자신"을 가리켜요.
    #       self.color 는 "이 패들의 색", self.speed 는 "이 패들의 속도"라는 뜻이에요.
    def __init__(self, x, y, color, keys):
        # x, y: 패들 왼쪽 위 모서리 좌표
        # keys: {"up": 키, "down": 키} 형태로 조작 키를 받습니다.
        #
        # 참고) 게임 화면의 좌표는 수학 좌표와 조금 달라요!
        #   - 왼쪽 위 모서리가 (0, 0)
        #   - 오른쪽으로 갈수록 x가 커지고
        #   - "아래"로 갈수록 y가 커져요. (수학과 반대!)

        # pygame.Rect: 직사각형(Rectangle) 정보를 담는 상자예요.
        # (x좌표, y좌표, 가로, 세로)를 넣으면 위치와 크기를 함께 기억해요.
        # 나중에 공과 부딪혔는지 확인할 때도 이 Rect를 사용해요.
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color    # 패들 색을 기억해 둡니다.
        self.keys = keys      # 위/아래 조작 키를 기억해 둡니다.
        self.speed = PADDLE_SPEED  # 한 프레임에 움직일 거리(7픽셀)

    def handle_input(self, pressed):
        """키보드가 눌린 상태에 따라 패들을 위아래로 움직입니다."""
        # pressed: 키보드의 모든 키가 "지금 눌려 있는지"를 담은 목록이에요.
        #          pressed[키] 가 True면 그 키를 누르고 있다는 뜻이에요.
        # self.keys["up"]: 이 패들의 "위" 키 (왼쪽 패들이면 W, 오른쪽이면 ↑)

        # "위" 키를 누르고 있으면 → y를 줄여서 위로 이동 (화면은 위쪽이 y가 작아요)
        if pressed[self.keys["up"]]:
            self.rect.y -= self.speed   # self.rect.y = self.rect.y - self.speed 와 같아요.
        # "아래" 키를 누르고 있으면 → y를 늘려서 아래로 이동
        if pressed[self.keys["down"]]:
            self.rect.y += self.speed

        # 화면 밖으로 나가지 않도록 위치를 제한합니다.
        # rect.top: 패들의 윗변 y좌표 / rect.bottom: 패들의 아랫변 y좌표
        if self.rect.top < 0:
            # 윗변이 화면 위쪽(0)을 넘어가면 → 딱 0에 붙여 둡니다.
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            # 아랫변이 화면 아래쪽(500)을 넘어가면 → 딱 500에 붙여 둡니다.
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        """화면에 패들을 그립니다."""
        # pygame.draw.rect(어디에, 무슨 색으로, 어떤 직사각형을)
        # border_radius=6: 모서리를 6픽셀만큼 둥글게 깎아서 부드럽게 보이게 해요.
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)
