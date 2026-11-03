> 14차시 **pygame 게임 루프: 입력 → 업데이트 → 그리기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** pygame 화면 좌표에서 아래로 갈수록 커지는 값은?

- ① x
- ② y
- ③ x와 y 모두
- ④ 없음

> **정답: ② y**  
> 화면 좌표계는 왼쪽 위가 원점이고 아래로 y가 증가합니다.

**Q2.** 게임 루프의 순서로 알맞은 것은?

- ① 그리기 → 입력 → 업데이트
- ② 입력 → 업데이트 → 그리기
- ③ 업데이트 → 그리기 → 입력
- ④ 입력 → 그리기 → 업데이트

> **정답: ② 입력 → 업데이트 → 그리기**  
> 입력을 확인하고, 상태를 바꾸고, 바뀐 모습을 그립니다.

**Q3.** 속도 5픽셀/프레임, 60 FPS일 때 2초 동안 이동 거리는?

- ① 120픽셀
- ② 300픽셀
- ③ 600픽셀
- ④ 10픽셀

> **정답: ③ 600픽셀**  
> 5 × 60 × 2 = 600픽셀입니다.

**Q4.** `pygame.display.flip()`의 역할은?

- ① 화면을 뒤집는다
- ② 그린 그림을 실제 화면에 표시한다
- ③ 창을 닫는다
- ④ 키 입력을 받는다

> **정답: ② 그린 그림을 실제 화면에 표시한다**  
> 보이지 않는 도화지에 그린 결과를 한 번에 화면에 보여 줍니다(깜빡임 방지).

**Q5.** 매 프레임 `screen.fill(BLACK)`을 하는 이유는?

- ① 색을 바꾸려고
- ② 이전 프레임의 그림을 지우려고
- ③ FPS를 맞추려고
- ④ 이벤트를 처리하려고

> **정답: ② 이전 프레임의 그림을 지우려고**  
> 지우지 않으면 움직인 자국이 계속 남습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ③ | ② | ② |

## 코딩 테스트 1. 프레임 이동 시뮬레이션

```python
y, speed, n = map(int, input().split())
for _ in range(n):
    y += speed
    if y < 0:
        y = 0
    if y > 500:
        y = 500
print(y)
```

**해설** 게임 루프의 (2) 업데이트 단계를 n번 반복한 것과 같습니다. 매 프레임마다 경계 검사를 해야 화면 밖으로 나가지 않습니다.

정답 코드 파일: [ch14_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch14_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch14_test1.py)

## 코딩 테스트 2. 가운데 점선 좌표 만들기

```python
H, D, G = map(int, input().split())
y = 0
while y < H:
    print(f"{y}-{y + D}")
    y += D + G
```

**해설** 실제 게임 코드의 `while y < SCREEN_HEIGHT:` 반복과 똑같은 알고리즘입니다. 그래픽 코드도 결국 좌표를 계산하는 반복문입니다.

정답 코드 파일: [ch14_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch14_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch14_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
