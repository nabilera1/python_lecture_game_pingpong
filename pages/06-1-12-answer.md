> 12차시 **심화: 던전 탈출과 BFS 탐색**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `DIRS["s"] = (1, 0)`일 때 (2, 3)에서 s로 이동하면?

- ① (1, 3)
- ② (3, 3)
- ③ (2, 4)
- ④ (2, 2)

> **정답: ② (3, 3)**  
> 행이 1 커지므로 (3, 3), 아래로 한 칸입니다.

**Q2.** BFS에서 '먼저 넣은 칸을 먼저 꺼내는' 자료구조는?

- ① 스택
- ② 큐
- ③ 딕셔너리
- ④ 튜플

> **정답: ② 큐**  
> 큐(queue)는 줄 서기처럼 선입선출입니다.

**Q3.** 방문한 칸을 기록할 때 집합(set)을 쓰는 이유로 가장 알맞은 것은?

- ① 순서를 기억하려고
- ② 중복 없이 포함 여부를 빠르게 확인하려고
- ③ 값을 바꾸려고
- ④ 정렬하려고

> **정답: ② 중복 없이 포함 여부를 빠르게 확인하려고**  
> set은 중복을 허용하지 않고 `in` 검사가 빠릅니다.

**Q4.** 튜플에 대한 설명으로 옳은 것은?

- ① 값을 바꿀 수 있다
- ② ( )로 만들며 값을 바꿀 수 없다
- ③ { }로 만든다
- ④ 키와 값이 있다

> **정답: ② ( )로 만들며 값을 바꿀 수 없다**  
> 튜플은 변경할 수 없는(immutable) 묶음입니다.

**Q5.** BFS로 처음 출구에 도착했을 때의 거리는?

- ① 최장 거리
- ② 최단 거리
- ③ 평균 거리
- ④ 알 수 없다

> **정답: ② 최단 거리**  
> 가까운 칸부터 방문하므로 처음 도착한 거리가 최단 거리입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. 격자 이동 명령 처리

```python
DIRS = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
R, C = map(int, input().split())
grid = [input() for _ in range(R)]
r, c = 0, 0
for cmd in input().strip():
    nr, nc = r + DIRS[cmd][0], c + DIRS[cmd][1]
    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
        r, c = nr, nc
print(r, c)
```

**해설** 새 위치를 먼저 계산(nr, nc)하고, 갈 수 있을 때만 실제 위치를 바꿉니다. 첫 번째 예에서 w는 지도 밖이라 무시되고, 나머지 명령으로 (2, 2)에 도착합니다.

정답 코드 파일: [ch12_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch12_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch12_test1.py)

## 코딩 테스트 2. BFS 최단 거리

```python
from collections import deque

R, C = map(int, input().split())
grid = [input() for _ in range(R)]
dist = [[-1] * C for _ in range(R)]       # -1 = 아직 방문 안 함
dist[0][0] = 0
queue = deque([(0, 0)])
while queue:
    r, c = queue.popleft()
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "." and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))
print(dist[R - 1][C - 1])
```

**해설** 게임 코드의 `seen` 집합 대신 **거리 표**(2차원 리스트)를 써서 '방문 여부'와 '거리'를 함께 기록했습니다. 이웃 칸의 거리 = 현재 칸 거리 + 1.

정답 코드 파일: [ch12_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch12_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch12_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
