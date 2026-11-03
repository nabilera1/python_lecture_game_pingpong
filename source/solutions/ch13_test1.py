"""13차시 코딩 테스트 1: Player 클래스 명령 처리 (기본) - 정답 예시 코드

hp(최대 30)를 가진 `Player` 클래스를 만들고 `damage(n)`, `heal(n)` 메서드를 구현하세요. hp는 0 미만, 30 초과가 될 수 없습니다. 첫째 줄에 명령 개수 n, 다음 n줄에 `damage 숫자` 또는 `heal 숫자`가 주어집니다. 모든 명령 후 hp를 출력하고, 0이면 둘째 줄에 `GAME OVER`를 출력하세요.
"""

class Player:
    def __init__(self, hp=30):
        self.hp = hp

    def damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def heal(self, amount):
        self.hp = min(30, self.hp + amount)

p = Player()
for _ in range(int(input())):
    cmd, value = input().split()
    if cmd == "damage":
        p.damage(int(value))
    else:
        p.heal(int(value))
print(p.hp)
if p.hp == 0:
    print("GAME OVER")
