"""[15차시] 핑퐁 2단계 - Paddle 클래스로 패들 2개 만들기 (한 파일 버전)

실행 방법: python step2_paddle_class.py
목표: 같은 설계도(클래스)로 서로 다른 객체 2개를 만들고, 경계 처리하기
"""

# =====================================================================
# 1단계에서는 x, y 변수로 네모 하나만 움직였어요.
# 패들이 2개가 되면? left_x, left_y, right_x, right_y, left_color ... 변수가 폭발!
# → "패들이 가진 정보(속성) + 패들이 하는 일(메서드)"을 클래스로 묶어요.
#
#   속성(attribute) : self.rect(위치·크기), self.color, self.keys, self.speed
#   메서드(method)  : handle_input(pressed), draw(screen)
# =====================================================================

import pygame

WIDTH, HEIGHT, FPS = 800, 500, 60
BLACK, GRAY = (18, 18, 24), (90, 90, 110)
PADDLE_W, PADDLE_H, PADDLE_SPEED, MARGIN = 14, 90, 7, 30


class Paddle:
    """위아래로 움직이는 직사각형 패들의 설계도"""

    def __init__(self, x, y, color, keys):
        # self = 지금 만들어지는 "바로 그 패들"
        self.rect = pygame.Rect(x, y, PADDLE_W, PADDLE_H)   # 위치+크기를 함께 기억하는 상자
        self.color = color
        self.keys = keys                                     # {"up": 키, "down": 키}
        self.speed = PADDLE_SPEED

    def handle_input(self, pressed):
        """자기 키만 확인해서 움직이고, 화면 밖으로는 못 나가게 막는다"""
        if pressed[self.keys["up"]]:
            self.rect.y -= self.speed
        if pressed[self.keys["down"]]:
            self.rect.y += self.speed
        # 경계 처리 (clamp): 넘어가면 끝에 딱 붙이기
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2단계: Paddle 클래스")
clock = pygame.time.Clock()

# 붕어빵 틀(클래스) 하나로 붕어빵(객체) 두 개 만들기
start_y = HEIGHT // 2 - PADDLE_H // 2
left = Paddle(MARGIN, start_y, (80, 180, 255), {"up": pygame.K_w, "down": pygame.K_s})
right = Paddle(WIDTH - MARGIN - PADDLE_W, start_y, (255, 140, 90),
               {"up": pygame.K_UP, "down": pygame.K_DOWN})

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    left.handle_input(pressed)          # 같은 메서드, 다른 객체 → 각자 자기 키로 움직임
    right.handle_input(pressed)

    screen.fill(BLACK)
    pygame.draw.line(screen, GRAY, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)
    left.draw(screen)
    right.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# [도전] 세 번째 패들(가운데, 초록색, I/K 키)을 한 줄로 추가해 보세요.
