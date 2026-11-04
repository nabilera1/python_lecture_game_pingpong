> 16차시 **Ball 클래스: 속도 벡터·반사·충돌**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** vx = 6, vy = -6인 공은 어느 방향으로 움직이는가?

- ① 오른쪽 아래
- ② 오른쪽 위
- ③ 왼쪽 위
- ④ 왼쪽 아래

> **정답: ② 오른쪽 위**  
> x 증가는 오른쪽, y 감소는 위쪽입니다.

**Q2.** 공이 위쪽 벽에 닿았을 때 바꿔야 하는 값은?

- ① vx만
- ② vy만
- ③ vx와 vy
- ④ 위치만

> **정답: ② vy만**  
> 위/아래 벽에서는 세로 속도의 부호만 바꿉니다.

**Q3.** `a.colliderect(b)`가 True가 되려면?

- ① 가로로만 겹치면 된다
- ② 세로로만 겹치면 된다
- ③ 가로와 세로 모두 겹쳐야 한다
- ④ 같은 크기여야 한다

> **정답: ③ 가로와 세로 모두 겹쳐야 한다**  
> 두 축에서 모두 겹쳐야 사각형이 겹칩니다.

**Q4.** bounce_paddle에서 공을 패들 밖으로 밀어내는 이유는?

- ① 공을 빠르게 하려고
- ② 다음 프레임에 또 충돌해 방향이 다시 뒤집히는 것을 막으려고
- ③ 점수를 주려고
- ④ 화면을 지우려고

> **정답: ② 다음 프레임에 또 충돌해 방향이 다시 뒤집히는 것을 막으려고**  
> 겹친 상태가 계속되면 매 프레임 방향이 뒤집혀 끼임 버그가 생깁니다.

**Q5.** 공의 x축 방향 속력(픽셀/초)은? (vx=6, vy=6, 60 FPS)

- ① 6
- ② 60
- ③ 360
- ④ 720

> **정답: ③ 360**  
> x축 방향으로 6 × 60 = 360픽셀/초입니다. (실제로는 대각선으로 움직이므로 전체 속력은 6√2 × 60 ≈ 509픽셀/초)

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ③ | ② | ③ |

## 코딩 테스트 1. 벽에 튕기는 공 (1차원)

```python
y, vy, size, H, n = map(int, input().split())
for _ in range(n):
    y += vy
    if y <= 0:
        y = 0
        vy *= -1
    elif y + size >= H:
        y = H - size
        vy *= -1
print(y, vy)
```

**해설** 첫 예를 추적하면 10 → 4 → -2(위쪽 벽: y=0, vy=+6) → 6 입니다. 공의 bottom은 `y + size`이므로 아래쪽 벽 검사에 공 크기를 꼭 더해야 합니다.

정답 코드 파일: [ch16_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch16_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch16_test1.py)

## 코딩 테스트 2. 사각형 충돌 판정

```python
def overlap(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah

for _ in range(int(input())):
    v = list(map(int, input().split()))
    print("충돌" if overlap(v[:4], v[4:]) else "통과")
```

**해설** 부등호에 `=`를 넣지 않았기 때문에 변이 맞닿은 경우(10 = 10)는 False입니다. pygame의 colliderect도 같은 규칙입니다. 세 번째 예는 실제 왼쪽 패들과 공의 위치입니다.

정답 코드 파일: [ch16_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch16_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch16_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
