> 17차시 **Scoreboard와 Game: 점수·승패·재시작으로 완성하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `bool(None)`의 값은?

- ① True
- ② False
- ③ None
- ④ 0

> **정답: ② False**  
> None은 조건문에서 False처럼 취급됩니다.

**Q2.** 공이 왼쪽 화면 밖으로 나갔을 때 점수를 얻는 쪽은?

- ① 왼쪽
- ② 오른쪽
- ③ 둘 다
- ④ 없음

> **정답: ② 오른쪽**  
> 왼쪽 플레이어가 막지 못했으므로 오른쪽이 득점합니다.

**Q3.** 화면 가로 800, 글자 너비 40일 때 화면 가운데 정렬 x는?

- ① 400
- ② 380
- ③ 360
- ④ 420

> **정답: ② 380**  
> 400 - 40 // 2 = 380입니다.

**Q4.** 승자가 생긴 뒤 화면이 멈추는 이유는?

- ① pygame.quit()이 실행돼서
- ② update()가 승자가 있으면 바로 return해서
- ③ FPS가 0이 돼서
- ④ running이 False가 돼서

> **정답: ② update()가 승자가 있으면 바로 return해서**  
> update 첫 줄에서 승자가 있으면 아무것도 움직이지 않고 끝냅니다. 그리기는 계속되므로 R 키를 기다릴 수 있습니다.

**Q5.** Game 클래스가 공을 직접 계산하지 않고 `self.ball.update()`를 부르는 설계의 장점은?

- ① 코드가 길어진다
- ② 역할이 나뉘어 수정할 곳을 찾기 쉽다
- ③ 실행이 빨라진다
- ④ pygame이 요구한다

> **정답: ② 역할이 나뉘어 수정할 곳을 찾기 쉽다**  
> 역할 분담(캡슐화) 덕분에 공의 규칙은 ball.py에서만 고치면 됩니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. 득점 기록으로 승자 정하기

```python
def winner(left, right, win_score):
    if left >= win_score:
        return "left"
    if right >= win_score:
        return "right"
    return None

W = int(input())
left = right = 0
for ch in input().strip():
    if winner(left, right, W):     # 이미 승자가 있으면 더 이상 득점하지 않음
        break
    if ch == "L":
        left += 1
    else:
        right += 1
result = winner(left, right, W)
if result == "left":
    print("왼쪽 승리")
elif result == "right":
    print("오른쪽 승리")
else:
    print("진행 중")
print(f"{left} : {right}")
```

**해설** Game.update의 첫 줄과 같은 아이디어입니다. 승자가 생긴 뒤의 기록(마지막 RR)은 무시되므로 5 : 2가 됩니다. None을 반환하는 함수를 if 조건에 바로 쓸 수 있습니다.

정답 코드 파일: [ch17_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch17_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch17_test1.py)

## 코딩 테스트 2. 점수판 배치 계산

```python
W, a, b, c = map(int, input().split())
print(W // 4 - a // 2)
print(W * 3 // 4 - b // 2)
print(W // 2 - c // 2)
```

**해설** `W * 3 // 4`는 곱셈을 먼저 하고 몫을 구합니다(왼쪽부터 계산). `W // 4 * 3`과는 W가 4의 배수가 아닐 때 결과가 다를 수 있습니다.

정답 코드 파일: [ch17_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch17_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch17_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
