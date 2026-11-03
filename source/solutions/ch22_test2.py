"""22차시 코딩 테스트 2: 리그 순위표 (도전) - 정답 예시 코드

모둠 대항 핑퐁 리그입니다. 첫째 줄에 경기 수 n, 다음 n줄에 `팀A 점수A 팀B 점수B`가 주어집니다. 이기면 승점 3, 비기면 1, 지면 0입니다. 승점이 높은 순으로, 같으면 팀 이름 사전순으로 `팀 승점`을 출력하세요.
"""

points = {}
for _ in range(int(input())):
    a, sa, b, sb = input().split()
    sa, sb = int(sa), int(sb)
    points.setdefault(a, 0)
    points.setdefault(b, 0)
    if sa > sb:
        points[a] += 3
    elif sa < sb:
        points[b] += 3
    else:
        points[a] += 1
        points[b] += 1
for team, p in sorted(points.items(), key=lambda x: (-x[1], x[0])):
    print(team, p)
