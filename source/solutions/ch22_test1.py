"""22차시 코딩 테스트 1: 동료 평가 집계 (기본) - 정답 예시 코드

첫째 줄에 평가자 수 n, 다음 n줄에 5개 항목의 별점(1~3)이 공백으로 주어집니다. 항목별 평균을 소수 첫째 자리까지 공백으로 구분해 출력하고, 둘째 줄에 평균이 가장 낮은 항목 번호(1부터, 같으면 앞 번호)를 `보완 항목: ○`으로 출력하세요.
"""

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]   # 2차원 리스트
avgs = []
for c in range(5):
    total = 0
    for r in range(n):
        total += table[r][c]
    avgs.append(total / n)
print(" ".join(f"{a:.1f}" for a in avgs))
print(f"보완 항목: {avgs.index(min(avgs)) + 1}")
