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

`Player`는 **플레이어의 정보와 할 수 있는 일을 묶은 설계도(클래스)**입니다. 다음 차시부터 본격적으로 배웁니다.

```python
try:
    main()
except (EOFError, KeyboardInterrupt):     # Ctrl+C 등으로 중단하면
    print("게임을 중단했습니다.")
```

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
