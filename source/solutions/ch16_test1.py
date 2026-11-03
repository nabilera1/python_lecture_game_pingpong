"""16차시 코딩 테스트 1: 벽에 튕기는 공 (1차원) (기본) - 정답 예시 코드

공의 처음 top y, 세로 속도 vy, 공 크기 size, 화면 높이 H, 프레임 수 n이 주어집니다. 매 프레임 `y += vy` 후, top이 0 이하이면 top을 0으로 하고 vy를 반대로, bottom(y+size)이 H 이상이면 bottom을 H로 하고 vy를 반대로 합니다. n프레임 후 `y vy`를 출력하세요.
"""

y, vy, size, H, n = map(int, input().split())
for _ in range(n):
    y += vy
    if y <= 0:
        y = 0
        vy *= -1
    elif y + size >= H:
        y = H - size
        vy *= -1
print(y, vy)
