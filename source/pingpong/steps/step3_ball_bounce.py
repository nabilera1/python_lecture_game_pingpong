"""[16차시] 핑퐁 3단계 - Ball 클래스: 속도 벡터, 벽 반사, 패들 충돌 (한 파일 버전)

실행 방법: python step3_ball_bounce.py
목표: "위치 = 위치 + 속도", "튕기기 = 속도 x (-1)" 를 코드로 구현하기
"""

# =====================================================================
# 물리·수학 연계
#   속도 벡터 (vx, vy) : 한 프레임 동안 x 로 vx, y 로 vy 만큼 이동
#   반사의 법칙         : 위/아래 벽 → vy 부호만 반대, 패들 → vx 부호만 반대
#                        (입사각 = 반사각, 속력은 그대로)
#   충돌 검사           : 두 직사각형이 겹치는가? → Rect.colliderect()
#
# 아직 점수는 없어요. 공이 좌우로 나가면 그냥 가운데에서 다시 출발해요.
# 완성본은 ../ 폴더의 모듈 버전(main.py, game.py, ball.py ...)을 보세요.
# =====================================================================

import random

import pygame

WIDTH, HEIGHT, FPS = 800, 500, 60
BLACK, YELLOW, BLUE, ORANGE = (18, 18, 24), (255, 230, 80), (80, 180, 255), (255, 140, 90)
BALL_SIZE, BALL_SPEED = 16, 6


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
        self.vx = self.vy = 0
        self.reset(random.choice([-1, 1]))

    def reset(self, direction=1):
        """가운데로 옮기고 속도를 새로 정한다"""
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vx = BALL_SPEED * direction
        self.vy = random.choice([-BALL_SPEED, BALL_SPEED])

    def update(self):
        """위치 = 위치 + 속도, 위/아래 벽에서 반사"""
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1
            # 벽 안쪽으로 되돌려 놓기 (안 하면 벽에 끼어서 떨 수 있어요)
            self.rect.top = max(self.rect.top, 0)
            self.rect.bottom = min(self.rect.bottom, HEIGHT)

    def bounce_paddle(self, paddle_rect):
        """패들과 겹치면 x 방향을 반대로, 패들 밖으로 살짝 밀어내기"""
        if self.rect.colliderect(paddle_rect):
            self.vx *= -1
            if self.vx > 0:                       # 오른쪽으로 가게 됨 = 왼쪽 패들에 맞음
                self.rect.left = paddle_rect.right
            else:
                self.rect.right = paddle_rect.left

    def draw(self, screen):
        pygame.draw.ellipse(screen, YELLOW, self.rect)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3단계: Ball 반사와 충돌")
clock = pygame.time.Clock()

ball = Ball()
# 이번 단계에서는 Paddle 클래스 대신 Rect 두 개로 충돌만 확인 (W/S, ↑/↓ 로 움직일 수 있음)
left = pygame.Rect(30, 205, 14, 90)
right = pygame.Rect(756, 205, 14, 90)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    left.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 7       # True=1, False=0 을 이용한 한 줄 이동
    right.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 7
    left.clamp_ip(screen.get_rect())                          # clamp_ip: 화면 안으로 가두기
    right.clamp_ip(screen.get_rect())

    ball.update()
    ball.bounce_paddle(left)
    ball.bounce_paddle(right)
    if ball.rect.right < 0 or ball.rect.left > WIDTH:          # 화면 밖 → 다시 출발
        ball.reset(random.choice([-1, 1]))

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, left, border_radius=6)
    pygame.draw.rect(screen, ORANGE, right, border_radius=6)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# [도전] 패들에 맞을 때마다 공이 10%씩 빨라지게 하려면? (힌트: self.vx *= -1.1)
