"""10차시 코딩 테스트 1: 행의 합과 열의 합 (기본) - 정답 예시 코드

3 × 3 점수표가 세 줄에 걸쳐 주어집니다. 첫째 줄에 각 행의 합, 둘째 줄에 각 열의 합을 공백으로 구분해 출력하세요.
"""

grid = [list(map(int, input().split())) for _ in range(3)]
row_sums = [sum(row) for row in grid]
col_sums = []
for c in range(3):
    total = 0
    for r in range(3):
        total += grid[r][c]
    col_sums.append(total)
print(*row_sums)
print(*col_sums)
