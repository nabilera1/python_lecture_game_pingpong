> 22차시 **게임 시연·발표와 프로젝트 성찰**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 발표에서 가장 강조해야 할 내용은?

- ① 게임의 그래픽
- ② 문제를 분해·설계·테스트한 과정
- ③ 코드의 줄 수
- ④ 개발 시간

> **정답: ② 문제를 분해·설계·테스트한 과정**  
> 이 수업의 목표는 문제 해결 과정입니다.

**Q2.** 동료 피드백으로 가장 알맞은 것은?

- ① 별로예요
- ② 좋아요
- ③ 판정표를 2차원 리스트로 만든 점이 좋아요. 입력 검사가 있으면 더 좋겠어요.
- ④ 제 것이 더 나아요

> **정답: ③ 판정표를 2차원 리스트로 만든 점이 좋아요. 입력 검사가 있으면 더 좋겠어요.**  
> 구체적인 칭찬과 실행 가능한 제안이 도움이 됩니다.

**Q3.** 작품을 공유할 때 하지 말아야 할 것은?

- ① 출처 밝히기
- ② AI 활용 내용 적기
- ③ 코드에 학번과 이름 넣기
- ④ 실행 방법 적기

> **정답: ③ 코드에 학번과 이름 넣기**  
> 개인정보는 공개된 곳에 올리지 않습니다.

**Q4.** 이 수업에서 사용한 6단계 문제 해결 모형의 순서로 옳은 것은?

- ① 구현→설계→발견→테스트→구조화→공유
- ② 문제 발견→문제 구조화→컴퓨팅 설계→구현→테스트 및 개선→공유·확장
- ③ 설계→구현→공유→발견→구조화→테스트
- ④ 발견→구현→테스트→설계→구조화→공유

> **정답: ② 문제 발견→문제 구조화→컴퓨팅 설계→구현→테스트 및 개선→공유·확장**  
> 문제를 찾고, 구조화하고, 설계하고, 구현하고, 테스트하고, 공유합니다.

**Q5.** 핑퐁 게임의 공을 그리는 데 쓴 도형과 충돌 계산에 쓴 도형을 순서대로 고르면?

- ① 원, 원
- ② 원, 사각형
- ③ 사각형, 원
- ④ 사각형, 사각형

> **정답: ② 원, 사각형**  
> 화면에는 ellipse(원)로 그리고, 충돌은 Rect(사각형)로 계산했습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ③ | ③ | ② | ② |

## 코딩 테스트 1. 동료 평가 집계

```python
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
```

**해설** 평가표는 '평가자 × 항목'의 2차원 리스트이고, 항목별 평균은 열의 평균입니다(10차시). `index(min(...))`은 가장 작은 값의 첫 위치를 찾습니다.

정답 코드 파일: [ch22_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch22_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch22_test1.py)

## 코딩 테스트 2. 리그 순위표

```python
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
```

**해설** 딕셔너리로 팀별 승점을 누적하고, `sorted`의 `key`에 (-승점, 이름)을 주어 '승점 내림차순, 이름 오름차순'으로 정렬했습니다. `setdefault`는 키가 없을 때만 기본값을 넣습니다.

정답 코드 파일: [ch22_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch22_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch22_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
