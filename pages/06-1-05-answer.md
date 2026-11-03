> 5차시 **리스트와 random: 가위바위보**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `a = [10, 20, 30]`일 때 `a[1]`의 값은?

- ① 10
- ② 20
- ③ 30
- ④ 오류

> **정답: ② 20**  
> 인덱스는 0부터 시작하므로 a[1]은 두 번째 값입니다.

**Q2.** `random.randint(1, 6)`이 돌려줄 수 **없는** 값은?

- ① 1
- ② 3
- ③ 6
- ④ 7

> **정답: ④ 7**  
> randint는 양 끝을 모두 포함하는 1~6 사이 정수입니다.

**Q3.** 빈 리스트 `h = []`에 `h.append(5)`, `h.append(9)`를 실행한 뒤 `len(h)`는?

- ① 0
- ② 1
- ③ 2
- ④ 9

> **정답: ③ 2**  
> 두 번 추가했으므로 2입니다.

**Q4.** `"보" not in ["가위", "바위", "보"]`의 결과는?

- ① True
- ② False
- ③ "보"
- ④ 오류

> **정답: ② False**  
> "보"가 리스트에 있으므로 not in은 False입니다.

**Q5.** `print("승리" if 3 > 5 else "패배")`의 출력은?

- ① 승리
- ② 패배
- ③ True
- ④ False

> **정답: ② 패배**  
> 조건 3 > 5가 거짓이므로 else 쪽 값이 선택됩니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ④ | ③ | ② | ② |

## 코딩 테스트 1. 점수 통계

```python
scores = list(map(int, input().split()))
print(max(scores))
print(min(scores))
print(f"{sum(scores) / len(scores):.1f}")
```

**해설** 리스트에는 `max`, `min`, `sum`, `len` 함수를 바로 쓸 수 있습니다. `:.1f`는 소수 첫째 자리까지 표시하는 형식 지정입니다.

정답 코드 파일: [ch05_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch05_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch05_test1.py)

## 코딩 테스트 2. 가위바위보 전적 계산

```python
choices = ["가위", "바위", "보"]
n = int(input())
result = [0, 0, 0]              # [무, 승, 패] 개수 : 인덱스가 곧 diff 값
for _ in range(n):
    me, cpu = input().split()
    diff = (choices.index(me) - choices.index(cpu)) % 3
    result[diff] += 1
print(f"{result[1]}승 {result[2]}패 {result[0]}무")
```

**해설** diff 값(0, 1, 2)을 그대로 리스트 인덱스로 사용하면 if 문 없이 개수를 셀 수 있습니다. `for _ in range(n)`은 n번 반복합니다(다음 차시).

정답 코드 파일: [ch05_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch05_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch05_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
