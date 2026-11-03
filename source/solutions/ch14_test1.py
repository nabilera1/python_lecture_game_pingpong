"""14차시 코딩 테스트 1: 프레임 이동 시뮬레이션 (기본) - 정답 예시 코드

물체의 처음 y좌표, 프레임당 속도(위로 이동이면 음수), 프레임 수 n이 한 줄에 주어집니다. n프레임 후 y좌표를 출력하되, y는 0 이상 화면 높이 500 이하로 제한(clamp)합니다.
"""

y, speed, n = map(int, input().split())
for _ in range(n):
    y += speed
    if y < 0:
        y = 0
    if y > 500:
        y = 500
print(y)
