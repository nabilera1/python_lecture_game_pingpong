"""14차시 코딩 테스트 2: 가운데 점선 좌표 만들기 (도전) - 정답 예시 코드

화면 높이 H, 점선 한 조각 길이 D, 빈칸 G가 주어집니다. `game.py`의 `draw_center_line()`처럼 y=0부터 시작해 y < H인 동안 조각을 그릴 때, 각 조각의 시작 y와 끝 y를 `시작-끝` 형식으로 한 줄씩 출력하세요. 끝 y는 시작 y + D입니다.
"""

H, D, G = map(int, input().split())
y = 0
while y < H:
    print(f"{y}-{y + D}")
    y += D + G
