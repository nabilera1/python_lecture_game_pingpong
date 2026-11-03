> 20차시 **프로젝트 구현: 설계대로 만들고 기능 확장하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 점진적 구현에 대한 설명으로 옳은 것은?

- ① 모든 기능을 한 번에 작성 후 실행
- ② 작은 기능 하나씩 구현하고 바로 확인
- ③ 테스트는 마지막에 한 번만
- ④ 주석은 쓰지 않는다

> **정답: ② 작은 기능 하나씩 구현하고 바로 확인**  
> 작게 만들고 바로 확인해야 문제 위치를 빨리 찾을 수 있습니다.

**Q2.** `class AIPaddle(Paddle):`의 의미는?

- ① Paddle을 삭제한다
- ② Paddle의 기능을 물려받은 새 클래스
- ③ Paddle 객체를 만든다
- ④ 함수 호출

> **정답: ② Paddle의 기능을 물려받은 새 클래스**  
> 괄호 안의 클래스를 상속합니다.

**Q3.** `abs(-7.5)`의 값은?

- ① -7.5
- ② 7.5
- ③ 7
- ④ -7

> **정답: ② 7.5**  
> 절댓값입니다.

**Q4.** `with open("best.txt", "w") as f:`에서 "w"의 뜻은?

- ① 읽기
- ② 쓰기(덮어쓰기)
- ③ 이어 쓰기
- ④ 삭제

> **정답: ② 쓰기(덮어쓰기)**  
> "r" 읽기, "w" 쓰기, "a" 이어 쓰기입니다.

**Q5.** 프로그램을 다시 실행해도 최고 기록이 남아 있게 하려면?

- ① 전역 변수에 저장
- ② 리스트에 저장
- ③ 파일에 저장
- ④ print로 출력

> **정답: ③ 파일에 저장**  
> 변수는 프로그램 종료와 함께 사라지므로 파일에 저장합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ③ |

## 코딩 테스트 1. 공 가속 시뮬레이션

```python
v, r, m, n = input().split()
v, r, m, n = float(v), float(r), float(m), int(n)
speeds = []
for _ in range(n):
    v = min(v * r, m)
    speeds.append(f"{v:.2f}")
print(" ".join(speeds))
```

**해설** `min(값, 최댓값)`으로 상한을 둡니다. 실수 계산은 오차가 생길 수 있으므로 출력할 때 `:.2f`로 자릿수를 맞춥니다.

정답 코드 파일: [ch20_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch20_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch20_test1.py)

## 코딩 테스트 2. 최고 기록 갱신 기록

```python
best = int(input())
history = []
updated = 0
for score in map(int, input().split()):
    if score > best:
        best = score
        updated += 1
    history.append(best)
print(*history)
print(f"갱신 {updated}회")
```

**해설** 같은 점수(5 → 5)는 갱신이 아니므로 `>`를 씁니다. `>=`로 쓰면 갱신 횟수가 달라지는 **논리 오류**가 됩니다. 실제 게임에서는 best를 파일에서 읽고(load_best) 끝날 때 저장(save_best)합니다.

정답 코드 파일: [ch20_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch20_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch20_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
