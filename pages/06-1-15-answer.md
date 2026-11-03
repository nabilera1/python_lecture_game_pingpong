> 15차시 **Paddle 클래스: 키 입력과 경계 처리**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 키를 누르고 있는 동안 계속 움직이게 하려면 어떤 방식을 써야 하는가?

- ① KEYDOWN 이벤트
- ② pygame.key.get_pressed()
- ③ input()
- ④ pygame.QUIT

> **정답: ② pygame.key.get_pressed()**  
> get_pressed는 매 프레임 현재 눌린 키 상태를 돌려줍니다.

**Q2.** `rect = pygame.Rect(30, 205, 14, 90)`일 때 `rect.bottom`은?

- ① 205
- ② 219
- ③ 295
- ④ 90

> **정답: ③ 295**  
> bottom = y + 높이 = 205 + 90 = 295입니다.

**Q3.** 왼쪽·오른쪽 패들이 같은 클래스인데 다른 키로 움직이는 이유는?

- ① 클래스가 2개라서
- ② 객체를 만들 때 keys 딕셔너리를 다르게 넘겨서
- ③ pygame이 자동으로 정해서
- ④ 전역 변수 때문

> **정답: ② 객체를 만들 때 keys 딕셔너리를 다르게 넘겨서**  
> `keys` 속성에 각자 다른 키를 저장했기 때문입니다.

**Q4.** 패들의 경계 처리 코드 `if self.rect.top < 0: self.rect.top = 0`의 의미는?

- ① 패들을 맨 아래로 보낸다
- ② 윗변이 화면 위로 넘어가면 0에 붙인다
- ③ 패들을 지운다
- ④ 속도를 0으로 만든다

> **정답: ② 윗변이 화면 위로 넘어가면 0에 붙인다**  
> 화면 밖으로 나간 만큼 되돌려 놓는 클램프입니다.

**Q5.** 화면 높이 500, 패들 높이 90일 때 패들 y의 최댓값은?

- ① 500
- ② 410
- ③ 455
- ④ 90

> **정답: ② 410**  
> bottom ≤ 500 이므로 y ≤ 500 - 90 = 410입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ③ | ② | ② | ② |

## 코딩 테스트 1. clamp 함수

```python
def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

low, high = map(int, input().split())
values = map(int, input().split())
print(*[clamp(v, low, high) for v in values])
```

**해설** `max(low, min(value, high))` 한 줄로도 쓸 수 있습니다. 게임에서 '범위 안에 가두기'는 매우 자주 쓰는 패턴입니다.

정답 코드 파일: [ch15_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch15_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch15_test1.py)

## 코딩 테스트 2. 패들 이동 기록

```python
H, PH, S, Y = map(int, input().split())
top = Y
result = []
for key in input().strip():
    if key in "UB":
        top -= S
    if key in "DB":
        top += S
    top = max(0, min(top, H - PH))
    result.append(top)
print(*result)
```

**해설** 실제 `handle_input`처럼 위·아래를 **각각 if로** 검사하므로 둘 다 누르면(B) 제자리입니다. 매 프레임 이동 뒤에 경계를 검사합니다.

정답 코드 파일: [ch15_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch15_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch15_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
