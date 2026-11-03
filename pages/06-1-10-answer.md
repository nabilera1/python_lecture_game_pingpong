> 10차시 **2차원 리스트와 중첩 반복: 판정표와 기록표**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `m = [[1, 2, 3], [4, 5, 6]]`일 때 `m[1][2]`는?

- ① 2
- ② 4
- ③ 6
- ④ 오류

> **정답: ③ 6**  
> 1행(두 번째 줄) 2열(세 번째 칸)의 값은 6입니다.

**Q2.** 위 `m`에서 `len(m)`과 `len(m[0])`은?

- ① 2, 3
- ② 3, 2
- ③ 6, 3
- ④ 2, 2

> **정답: ① 2, 3**  
> 행 2개, 각 행의 칸 3개입니다.

**Q3.** 판정표 `TABLE[나][컴퓨터]`에서 나 보(2), 컴퓨터 가위(0)일 때 값은? (`TABLE = [[0,2,1],[1,0,2],[2,1,0]]`)

- ① 0
- ② 1
- ③ 2
- ④ 오류

> **정답: ③ 2**  
> TABLE[2][0] = 2 → 짐입니다. (보는 가위에게 진다)

**Q4.** 바깥 반복 3번, 안쪽 반복 4번인 중첩 반복에서 안쪽 코드는 몇 번 실행되는가?

- ① 4번
- ② 7번
- ③ 12번
- ④ 3번

> **정답: ③ 12번**  
> 3 × 4 = 12번입니다.

**Q5.** `def f(): return 1, 2` 일 때 `a, b = f()` 후 b의 값은?

- ① 1
- ② 2
- ③ (1, 2)
- ④ 오류

> **정답: ② 2**  
> return 1, 2는 튜플 (1, 2)를 돌려주고, 나눠 받으면 b = 2입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ③ | ① | ③ | ③ | ② |

## 코딩 테스트 1. 행의 합과 열의 합

```python
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
```

**해설** 행의 합은 `sum(row)`로 바로 구하지만, 열의 합은 바깥 반복을 열(c), 안쪽 반복을 행(r)으로 바꿔 `grid[r][c]`를 더합니다. `print(*리스트)`는 값을 공백으로 구분해 출력합니다.

정답 코드 파일: [ch10_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch10_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch10_test1.py)

## 코딩 테스트 2. 지도에서 몬스터 찾기

```python
R, C = map(int, input().split())
grid = [input() for _ in range(R)]
walls = 0
monsters = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == "#":
            walls += 1
        elif grid[r][c] == "M":
            monsters.append((r, c))
print(walls)
for r, c in monsters:
    print(r, c)
```

**해설** 문자열 리스트도 `grid[r][c]`로 2차원처럼 접근할 수 있습니다. 위치는 바꿀 일이 없으므로 튜플 `(r, c)`로 저장했습니다.

정답 코드 파일: [ch10_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch10_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch10_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
