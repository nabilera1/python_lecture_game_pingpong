"""20차시 코딩 테스트 2: 최고 기록 갱신 기록 (도전) - 정답 예시 코드

첫째 줄에 저장되어 있던 최고 기록 best(없으면 0), 둘째 줄에 이번에 플레이한 점수들이 공백으로 주어집니다. 각 판이 끝날 때마다 최고 기록을 공백으로 구분해 출력하고, 마지막 줄에 기록이 갱신된 횟수를 `갱신 ○회`로 출력하세요.
"""

best = int(input())
history = []
updated = 0
for score in map(int, input().split()):
    if score > best:
        best = score
        updated += 1
    history.append(best)
print(*history)
print(f"갱신 {updated}회")
