> **3부 함수와 자료구조로 게임 다듬기** · 12차시 · 6단계 모형: **구현**  
> 게임: 던전 탈출 (난이도 상)  
> 핵심 개념: 격자, 튜플, 방향 벡터, BFS, 큐(deque), 집합(set), dataclass, try-except

## 학습 목표

1. 2차원 격자에서 방향 딕셔너리와 튜플로 이동을 구현할 수 있다.
2. BFS(너비 우선 탐색)의 원리를 설명하고 최단 거리 문제에 적용할 수 있다.
3. dataclass와 try–except의 쓰임을 이해할 수 있다.

## 핵심 질문

> **컴퓨터는 미로에서 출구로 가는 길이 있는지 어떻게 알아낼까?**

던전 탈출은 지금까지의 게임 중 가장 복잡합니다. 무작위로 만든 지도에 **출구로 가는 길이 반드시 있도록** 컴퓨터가 미리 검사합니다. 이때 쓰는 알고리즘이 **BFS(너비 우선 탐색)** 입니다.

이번 차시는 심화 내용입니다. 모든 코드를 외우기보다 **격자 이동**과 **BFS의 아이디어**를 이해하는 데 집중하세요.

## 격자와 방향 딕셔너리

```python
SIZE = 7
DIRS = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}   # (행 변화, 열 변화)

pos = (0, 0)                                   # 튜플: (행, 열)
cmd = "d"
r, c = pos[0] + DIRS[cmd][0], pos[1] + DIRS[cmd][1]   # (0, 1) 오른쪽 한 칸

def inside(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE      # 지도 안쪽인가?
```

- 행(r)이 커지면 **아래**, 열(c)이 커지면 **오른쪽**입니다. (핑퐁 게임의 y, x와 같은 원리)
- 바꿀 일이 없는 위치·방향은 **튜플** `( )`로 저장합니다.

## BFS: 가까운 칸부터 퍼져 나가기

```python
from collections import deque

def escapable(grid):
    seen, queue = {(0, 0)}, deque([(0, 0)])   # 방문한 칸(집합), 살펴볼 칸(큐)
    while queue:
        r0, c0 = queue.popleft()              # 먼저 들어온 칸부터 꺼냄
        for dr, dc in DIRS.values():          # 상하좌우
            r, c = r0 + dr, c0 + dc
            if inside(r, c) and grid[r][c] != "#" and (r, c) not in seen:
                seen.add((r, c))
                queue.append((r, c))
    return GOAL in seen                       # 출구를 방문했다면 탈출 가능
```

물에 돌을 던지면 물결이 **가까운 곳부터 동그랗게** 퍼지듯, BFS는 출발점에서 1칸 거리, 2칸 거리 … 순서로 칸을 방문합니다. 그래서 **처음 도착한 순간의 거리가 최단 거리**가 됩니다.

| 자료구조 | 역할 |
| --- | --- |
| 큐 `deque` | 먼저 넣은 것을 먼저 꺼냄 (줄 서기) |
| 집합 `set` | 중복 없이 '방문했는지' 빠르게 확인 |

## dataclass와 try–except 맛보기

```python
@dataclass
class Player:
    hp: int = 30
    gold: int = 0
    potions: int = 1
    def alive(self):
        return self.hp > 0

p = Player()          # 플레이어 객체 생성
p.hp -= 5             # p 의 체력만 줄어듦
```

`Player`는 **플레이어의 정보와 할 수 있는 일을 묶은 설계도**(클래스)입니다. 다음 차시부터 본격적으로 배웁니다.

```python
try:
    main()
except (EOFError, KeyboardInterrupt):     # Ctrl+C 등으로 중단하면
    print("게임을 중단했습니다.")
```

## 코드 흐름 따라가기

프로그램을 실행하면 아래 순서로 함수가 호출되고 값이 오갑니다. 전체 코드를 옆에 띄워 놓고 한 줄씩 따라가 보세요.

| 순서 | 실행되는 곳 | 하는 일 |
| --- | --- | --- |
| 1 | 맨 아래 `try: main()` | 실행 중 Ctrl+C 등으로 끊으면 `except`에서 안내 문구를 출력한다. |
| 2 | `main()` → `make_map()` | 가중치를 준 무작위 글자로 7×7 지도(2차원 리스트)를 만들고, `escapable()`(BFS)이 True가 나올 때까지 다시 만든다. |
| 3 | `main()` | `pos = (0, 0)`, `p = Player()`(hp 30, gold 0, potions 1), `steps = 0`으로 시작한다. |
| 4 | `main()` 반복 | 중첩 반복과 `view()`로 지도를 출력한다. 내 위치는 `@`, 2칸 밖은 `?`(안개). |
| 5 | `main()` 반복 | 명령을 입력받아 `DIRS[cmd]`만큼 이동할 칸을 계산하고, `inside()`와 벽(`#`)을 검사한다. |
| 6 | `main()` 반복 | 밟은 칸에 따라 `M` → `fight(p)`, `P` → 포션 +1, `T` → 골드, `E` → 점수 출력 후 `return`. |
| 7 | `fight(p)` | 몬스터와 턴제 전투. 공격·포션·도망을 고르고, 이기면 골드를 얻는다. `p`는 객체라서 함수 안에서 바꾼 hp·gold가 그대로 유지된다. |

| 함수 | 받는 값 | 돌려주는 값 |
| --- | --- | --- |
| `inside(r, c)` | 행, 열 | 지도 안이면 True |
| `escapable(grid)` | 지도 | 출구까지 길이 있으면 True |
| `make_map()` | 없음 | 탈출 가능한 지도 |
| `view(r, c, ch, pos)` | 칸 위치, 글자, 내 위치 | 화면에 보일 글자 |
| `fight(p)` | Player 객체 | 없음 (p의 값을 바꿈) |

## 실행 예시

`10_dungeon.py`를 실행했을 때의 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. (무작위 값이 있어 실행할 때마다 결과가 달라집니다.)

```text
=== 던전 탈출 === 출구 E까지 가세요! (이동 w/a/s/d, 종료 q)
M:몬스터 P:포션 T:보물 #:벽 ?:안개
@ . P ? ? ? ?
. # ? ? ? ? ?
# ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? E
HP 30 | 골드 0 | 포션 1 | 걸음 0
> d
. @ P . ? ? ?
. # M ? ? ? ?
? . ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? E
HP 30 | 골드 0 | 포션 1 | 걸음 1
> x
w/a/s/d 중에서 입력하세요.
. @ P . ? ? ?
. # M ? ? ? ?
? . ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? E
HP 30 | 골드 0 | 포션 1 | 걸음 1
> s
막혀 있어요!
. @ P . ? ? ?
. # M ? ? ? ?
? . ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? E
HP 30 | 골드 0 | 포션 1 | 걸음 1
> d
포션을 주웠다!
. . @ . . ? ?
? # M . ? ? ?
? ? T ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? E
HP 30 | 골드 0 | 포션 2 | 걸음 2
> s

[전투] 오크 등장! (HP 15)
  1)공격 2)포션 3)도망 > 1
  공격! 3 피해
  오크의 반격! 2 피해 (내 HP 28)
  1)공격 2)포션 3)도망 > 1
  공격! 4 피해
  오크의 반격! 1 피해 (내 HP 27)
  1)공격 2)포션 3)도망 > 1
  공격! 6 피해
  오크의 반격! 4 피해 (내 HP 23)
  1)공격 2)포션 3)도망 > 1
  공격! 8 피해
  오크 처치! 골드 +11
? . . . ? ? ?
. # @ . . ? ?
? . T T ? ? ?
? ? . ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? ?
? ? ? ? ? ? E
HP 23 | 골드 11 | 포션 2 | 걸음 3
> q

게임 종료...
```

## 전체 코드

지금까지 조각으로 살펴본 코드를 하나로 합친 **전체 프로그램**입니다. 아래 순서로 바로 실행할 수 있습니다.

1. 코드 블록 전체를 복사합니다. (위키독스 코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### 10_dungeon.py

```python
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
```

파일 받기: [10_dungeon.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/10_dungeon.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/10_dungeon.py)

## 실습 활동

1. `10_dungeon.py`를 실행하고, 안개 범위(2칸)를 3칸으로 바꿔 보세요.
2. `SIZE`를 9로 키워 보세요. 어떤 부분이 자동으로 함께 바뀌나요?
3. 종이에 5 × 5 미로를 그리고, BFS로 각 칸의 거리 숫자를 직접 적어 보세요.

활동지: [ws12-dungeon-bfs.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws12-dungeon-bfs.md)

## 확인 퀴즈

**Q1.** `DIRS["s"] = (1, 0)`일 때 (2, 3)에서 s로 이동하면?

- ① (1, 3)
- ② (3, 3)
- ③ (2, 4)
- ④ (2, 2)

**Q2.** BFS에서 '먼저 넣은 칸을 먼저 꺼내는' 자료구조는?

- ① 스택
- ② 큐
- ③ 딕셔너리
- ④ 튜플

**Q3.** 방문한 칸을 기록할 때 집합(set)을 쓰는 이유로 가장 알맞은 것은?

- ① 순서를 기억하려고
- ② 중복 없이 포함 여부를 빠르게 확인하려고
- ③ 값을 바꾸려고
- ④ 정렬하려고

**Q4.** 튜플에 대한 설명으로 옳은 것은?

- ① 값을 바꿀 수 있다
- ② ( )로 만들며 값을 바꿀 수 없다
- ③ { }로 만든다
- ④ 키와 값이 있다

**Q5.** BFS로 처음 출구에 도착했을 때의 거리는?

- ① 최장 거리
- ② 최단 거리
- ③ 평균 거리
- ④ 알 수 없다

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 격자 이동 명령 처리 (기본)

첫째 줄에 R C, 다음 R줄에 지도(`.` 길, `#` 벽), 마지막 줄에 명령 문자열(w/a/s/d)이 주어집니다. (0, 0)에서 출발해 명령대로 움직이되, 지도 밖이나 벽이면 그 명령은 무시합니다. 최종 위치를 `행 열`로 출력하세요.

- 입력: R C, 지도, 명령
- 출력: 최종 위치

예제 입력 1

```text
3 3
..#
.#.
...
dwassdd
```

예제 출력 1

```text
2 2
```

예제 입력 2

```text
2 2
.#
..
wadd
```

예제 출력 2

```text
0 0
```

### 문제 2. BFS 최단 거리 (도전)

첫째 줄에 R C, 다음 R줄에 미로가 주어집니다. (0, 0)에서 (R-1, C-1)까지 상하좌우로 이동할 때 최소 이동 횟수를 출력하세요. 갈 수 없으면 -1을 출력합니다. 출발점과 도착점은 항상 `.`입니다.

- 입력: R C, 미로
- 출력: 최소 이동 횟수 또는 -1

예제 입력 1

```text
3 3
..#
#..
#..
```

예제 출력 1

```text
4
```

예제 입력 2

```text
2 2
.#
#.
```

예제 출력 2

```text
-1
```

정답과 해설은 **[부록] 06-1-12. 12차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-12-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 격자 이동 = 위치 튜플 + 방향 딕셔너리
- BFS: 큐로 가까운 칸부터 → 최단 거리
- 집합(set)으로 방문 여부 확인
- dataclass → 다음 차시 클래스로 연결

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `10_dungeon.py` | [10_dungeon.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/10_dungeon.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/10_dungeon.py) |
| 학습용 PPT | [12-dungeon-bfs.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/12-dungeon-bfs.pptx) |
| 학생 활동지 | [ws12-dungeon-bfs.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws12-dungeon-bfs.md) |
| 코딩 테스트 1 정답 코드 | [ch12_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch12_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch12_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch12_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch12_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch12_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
