"""던전 탈출 (난이도 상) - 12차시: 2차원 격자, 튜플, 딕셔너리, dataclass, BFS, 예외 처리

실행 방법: python 10_dungeon.py
"""

# =====================================================================
# 게임 규칙
#   7 x 7 던전의 왼쪽 위(0, 0)에서 출발해 오른쪽 아래 출구 E 까지 가면 탈출!
#   w(위) a(왼쪽) s(아래) d(오른쪽)로 한 칸씩 이동, q 는 종료.
#   M: 몬스터(전투)  P: 포션  T: 보물  #: 벽  ?: 아직 안 보이는 칸(안개)
#
# 이 게임에서 처음 만나는 개념
#   1) 2차원 격자 grid[r][c] : r = 행(row, 세로 위치), c = 열(column, 가로 위치)
#   2) 튜플 (r, c)           : 위치처럼 "묶어서 다루지만 바꾸지 않을 값"
#   3) dataclass Player      : 플레이어 정보(hp, gold, potions)를 묶은 간단한 클래스
#                              → 13차시 '클래스와 객체'로 이어지는 다리!
#   4) BFS(너비 우선 탐색)    : 출발점에서 가까운 칸부터 차례로 퍼져 나가며
#                              출구까지 길이 있는지 검사하는 알고리즘
#   5) try-except            : Ctrl+C 등으로 강제 종료해도 오류 화면 대신 안내 문구 출력
# =====================================================================

import random
from collections import deque        # deque: 앞에서 꺼내기(popleft)가 빠른 "큐" 자료구조
from dataclasses import dataclass

SIZE = 7                              # 던전 크기 7 x 7
GOAL = (SIZE - 1, SIZE - 1)           # 출구 위치 (6, 6) - 튜플
# 방향 딕셔너리: 키를 누르면 (행 변화량, 열 변화량) 만큼 이동
DIRS = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
MONSTERS = {"슬라임": (6, 2), "고블린": (10, 3), "오크": (15, 5)}   # 이름: (체력, 최대 공격력)


@dataclass
class Player:
    """플레이어의 상태를 한데 묶은 설계도 (값만 적으면 __init__ 이 자동으로 만들어져요)"""
    hp: int = 30
    gold: int = 0
    potions: int = 1

    def alive(self):
        """체력이 남아 있으면 True"""
        return self.hp > 0


def inside(r, c):
    """(r, c)가 던전 안쪽 칸이면 True"""
    # 0 <= r < SIZE : 파이썬은 비교를 이어서 쓸 수 있어요. (0 <= r and r < SIZE)
    return 0 <= r < SIZE and 0 <= c < SIZE


def escapable(grid):
    """BFS로 시작점에서 출구까지 갈 수 있는 지도인지 검사한다."""
    # seen: 이미 가 본 칸들의 "집합(set)" - 중복 없이 빠르게 포함 여부 확인
    # queue: 앞으로 살펴볼 칸 목록 (먼저 넣은 칸을 먼저 꺼냄)
    seen, queue = {(0, 0)}, deque([(0, 0)])
    while queue:                                  # 살펴볼 칸이 남아 있는 동안
        r0, c0 = queue.popleft()                  # 가장 먼저 들어온 칸 꺼내기
        for dr, dc in DIRS.values():              # 상하좌우 4방향 확인
            r, c = r0 + dr, c0 + dc
            if inside(r, c) and grid[r][c] != "#" and (r, c) not in seen:
                seen.add((r, c))
                queue.append((r, c))
    return GOAL in seen                           # 출구에 도달한 적이 있으면 탈출 가능


def make_map():
    """무작위 던전을 만들되, 출구로 가는 길이 있는 지도만 돌려준다"""
    while True:   # 출구로 가는 길이 있는 지도가 나올 때까지 다시 만든다
        # 리스트 컴프리헨션: 한 행(7칸)을 SIZE 번 만들어 2차원 리스트 완성
        # random.choices(글자들, 가중치, k=개수): 가중치 비율로 k개 뽑기 (. 이 가장 많이 나옴)
        grid = [random.choices(".#MPT", [58, 17, 10, 8, 7], k=SIZE) for _ in range(SIZE)]
        grid[0][0], grid[GOAL[0]][GOAL[1]] = ".", "E"
        if escapable(grid):
            return grid


def view(r, c, ch, pos):
    """플레이어 주변 2칸 안만 보이는 안개 효과"""
    # 맨해튼 거리: 가로 차이 + 세로 차이 (격자에서 걸어서 가는 거리)
    near = abs(r - pos[0]) + abs(c - pos[1]) <= 2
    # 중첩 조건 표현식: 내 위치면 "@", 가깝거나 출구면 실제 글자, 아니면 "?"
    return "@" if (r, c) == pos else ch if near or ch == "E" else "?"


def fight(p):
    """몬스터와 턴제 전투를 한다 (p: Player 객체)"""
    # items(): (키, 값) 짝 목록. 값이 튜플이라 (hp, atk) 로 바로 풀어서 받기
    name, (hp, atk) = random.choice(list(MONSTERS.items()))
    print(f"\n[전투] {name} 등장! (HP {hp})")
    while hp > 0 and p.alive():
        act = input("  1)공격 2)포션 3)도망 > ")
        if act == "1":
            dmg = random.randint(3, 8)
            hp -= dmg
            print(f"  공격! {dmg} 피해")
        elif act == "2" and p.potions:            # 포션이 0이면 False 취급
            p.potions -= 1
            p.hp = min(30, p.hp + 12)             # 최대 체력 30을 넘지 않게
            print("  포션 사용! HP +12")
        elif act == "3":
            if random.random() < 0.5:             # random(): 0.0 이상 1.0 미만 → 50% 확률
                print("  도망 성공!")
                return
            print("  도망 실패!")
        else:
            print("  할 수 없는 행동이에요.")
            continue
        if hp > 0:                                # 몬스터가 살아 있으면 반격
            hit = random.randint(1, atk)
            p.hp -= hit
            print(f"  {name}의 반격! {hit} 피해 (내 HP {p.hp})")
    if p.alive():
        reward = random.randint(5, 12)
        p.gold += reward
        print(f"  {name} 처치! 골드 +{reward}")


def main():
    grid, pos, p, steps = make_map(), (0, 0), Player(), 0
    print("=== 던전 탈출 === 출구 E까지 가세요! (이동 w/a/s/d, 종료 q)")
    print("M:몬스터 P:포션 T:보물 #:벽 ?:안개")
    while p.alive():
        # 중첩 반복으로 지도 출력: enumerate 는 (번호, 값)을 함께 꺼내 줘요.
        for r, row in enumerate(grid):
            print(" ".join(view(r, c, ch, pos) for c, ch in enumerate(row)))
        print(f"HP {p.hp} | 골드 {p.gold} | 포션 {p.potions} | 걸음 {steps}")
        cmd = input("> ").strip().lower()
        if cmd == "q":
            break
        if cmd not in DIRS:
            print("w/a/s/d 중에서 입력하세요.")
            continue
        r, c = pos[0] + DIRS[cmd][0], pos[1] + DIRS[cmd][1]   # 이동할 칸 계산
        if not inside(r, c) or grid[r][c] == "#":
            print("막혀 있어요!")
            continue
        pos, steps, cell = (r, c), steps + 1, grid[r][c]
        grid[r][c] = "."                          # 밟은 칸의 아이템/몬스터는 사라짐
        if cell == "M":
            fight(p)
        elif cell == "P":
            p.potions += 1
            print("포션을 주웠다!")
        elif cell == "T":
            gain = random.randint(5, 15)
            p.gold += gain
            print(f"보물 발견! 골드 +{gain}")
        elif cell == "E":
            print(f"\n탈출 성공! 점수: {p.gold * 10 + p.hp * 5 - steps}점")
            return
    print("\n게임 종료..." if p.alive() else "\n쓰러졌습니다... GAME OVER")


if __name__ == "__main__":
    # try-except: 실행 중 오류(예외)가 생기면 프로그램이 멈추는 대신 except 부분을 실행
    try:
        main()
    except (EOFError, KeyboardInterrupt):         # 입력 끝(Ctrl+D/Z) 또는 Ctrl+C
        print("\n게임을 중단했습니다.")
