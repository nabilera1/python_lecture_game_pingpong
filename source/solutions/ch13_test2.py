"""13차시 코딩 테스트 2: 두 객체를 따로 관리하기 (도전) - 정답 예시 코드

이름과 점수를 가진 `Team` 클래스를 만들고 `add_point()` 메서드를 구현하세요. 첫째 줄에 두 팀 이름, 둘째 줄에 득점한 팀 이름들이 공백으로 주어질 때, 두 팀의 `이름 점수`를 한 줄씩 출력하고 마지막 줄에 승자(같으면 `무승부`)를 출력하세요.
"""

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

names = input().split()
teams = {name: Team(name) for name in names}    # 이름 → Team 객체
for who in input().split():
    teams[who].add_point()
a, b = teams[names[0]], teams[names[1]]
print(a.name, a.score)
print(b.name, b.score)
if a.score == b.score:
    print("무승부")
else:
    print(a.name if a.score > b.score else b.name)
