"""12차시 코딩 테스트 1: 격자 이동 명령 처리 (기본) - 정답 예시 코드

첫째 줄에 R C, 다음 R줄에 지도(`.` 길, `#` 벽), 마지막 줄에 명령 문자열(w/a/s/d)이 주어집니다. (0, 0)에서 출발해 명령대로 움직이되, 지도 밖이나 벽이면 그 명령은 무시합니다. 최종 위치를 `행 열`로 출력하세요.
"""

DIRS = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
R, C = map(int, input().split())
grid = [input() for _ in range(R)]
r, c = 0, 0
for cmd in input().strip():
    nr, nc = r + DIRS[cmd][0], c + DIRS[cmd][1]
    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
        r, c = nr, nc
print(r, c)
