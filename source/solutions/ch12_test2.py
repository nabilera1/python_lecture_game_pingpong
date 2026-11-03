"""12차시 코딩 테스트 2: BFS 최단 거리 (도전) - 정답 예시 코드

첫째 줄에 R C, 다음 R줄에 미로가 주어집니다. (0, 0)에서 (R-1, C-1)까지 상하좌우로 이동할 때 최소 이동 횟수를 출력하세요. 갈 수 없으면 -1을 출력합니다. 출발점과 도착점은 항상 `.`입니다.
"""

from collections import deque

R, C = map(int, input().split())
grid = [input() for _ in range(R)]
dist = [[-1] * C for _ in range(R)]       # -1 = 아직 방문 안 함
dist[0][0] = 0
queue = deque([(0, 0)])
while queue:
    r, c = queue.popleft()
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "." and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))
print(dist[R - 1][C - 1])
