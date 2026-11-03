"""10차시 코딩 테스트 2: 지도에서 몬스터 찾기 (도전) - 정답 예시 코드

첫째 줄에 행 수 R과 열 수 C, 다음 R줄에 지도가 주어집니다. `#`(벽)의 개수를 첫째 줄에 출력하고, 이어서 `M`(몬스터)의 위치를 위에서부터, 같은 행은 왼쪽부터 `행 열` 형식으로 한 줄씩 출력하세요.
"""

R, C = map(int, input().split())
grid = [input() for _ in range(R)]
walls = 0
monsters = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == "#":
            walls += 1
        elif grid[r][c] == "M":
            monsters.append((r, c))
print(walls)
for r, c in monsters:
    print(r, c)
