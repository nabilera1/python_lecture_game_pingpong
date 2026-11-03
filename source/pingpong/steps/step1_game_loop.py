"""[14차시] 핑퐁 1단계 - pygame 창 띄우기와 게임 루프 (클래스 없이 한 파일)

실행 방법: pip install pygame  →  python step1_game_loop.py
목표: "입력 → 업데이트 → 그리기 → 시간 맞추기" 반복 구조(게임 루프)를 직접 눈으로 확인하기
"""

# =====================================================================
# 텍스트 게임과 무엇이 다를까요?
#   텍스트 게임: input() 에서 멈춰 "사용자를 기다림" → 입력이 와야 다음 줄 실행
#   그래픽 게임: 기다리지 않고 1초에 60번 화면을 새로 그림 → 그 사이에 키 상태만 확인
#
# 이번 단계에서 화면에 나오는 것
#   - 어두운 배경, 가운데 점선
#   - 방향키로 움직이는 네모 하나 (아직 클래스 없이 변수 x, y 로만!)
# =====================================================================

import pygame

# 설정값 (다음 단계부터는 constants.py 로 옮겨요)
WIDTH, HEIGHT = 800, 500
FPS = 60
BLACK, GRAY, BLUE = (18, 18, 24), (90, 90, 110), (80, 180, 255)

pygame.init()                                         # pygame 준비
screen = pygame.display.set_mode((WIDTH, HEIGHT))     # 800 x 500 창(도화지)
pygame.display.set_caption("1단계: 게임 루프")
clock = pygame.time.Clock()                           # 속도 조절용 시계

x, y = 400, 250        # 네모의 위치 (화면 좌표: 왼쪽 위가 (0,0), 아래로 갈수록 y 증가!)
speed = 5              # 한 프레임에 움직이는 거리(픽셀)
running = True

while running:                                        # ===== 게임 루프 =====
    # (1) 입력: 창 닫기 버튼 확인
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # (2) 업데이트: 지금 눌려 있는 키를 보고 위치 바꾸기
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= speed
    if pressed[pygame.K_RIGHT]:
        x += speed
    if pressed[pygame.K_UP]:
        y -= speed                                    # 위로 = y 감소
    if pressed[pygame.K_DOWN]:
        y += speed

    # (3) 그리기: 배경 → 점선 → 네모 순서 (나중에 그린 것이 위에 보임)
    screen.fill(BLACK)
    for dash_y in range(0, HEIGHT, 28):               # 0, 28, 56, ... 간격으로 선 조각
        pygame.draw.line(screen, GRAY, (WIDTH // 2, dash_y), (WIDTH // 2, dash_y + 16), 3)
    pygame.draw.rect(screen, BLUE, (x, y, 20, 20))
    pygame.display.flip()                             # 완성된 그림을 실제 화면에 표시

    # (4) 시간 맞추기: 1초에 최대 60번만 반복
    clock.tick(FPS)

pygame.quit()

# [도전] 네모가 화면 밖으로 나가지 않게 하려면 어떤 if 문이 필요할까요?
