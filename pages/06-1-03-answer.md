> 3차시 **규칙 분해와 조건문**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `guess = 30`일 때 `10 <= guess and guess < 30`의 결과는?

- ① True
- ② False
- ③ 30
- ④ 오류

> **정답: ② False**  
> `guess < 30`이 거짓이므로 and 전체가 거짓입니다.

**Q2.** 다음 중 '같다'를 비교하는 연산자는?

- ① =
- ② ==
- ③ ===
- ④ !=

> **정답: ② ==**  
> `=`는 대입, `==`는 비교입니다.

**Q3.** `x = 85`일 때 출력은?

```python
if x >= 70:
    print("C")
elif x >= 80:
    print("B")
else:
    print("E")
```

- ① B
- ② C
- ③ B와 C
- ④ E

> **정답: ② C**  
> 위에서부터 처음 참인 조건(`x >= 70`) 하나만 실행됩니다. 조건 순서가 중요한 이유입니다.

**Q4.** 복잡한 문제를 해결 가능한 작은 문제로 나누는 것은?

- ① 추상화
- ② 분해
- ③ 패턴 인식
- ④ 디버깅

> **정답: ② 분해**  
> 분해(decomposition)입니다.

**Q5.** `(0 - 2) % 3`의 값은? (나: 가위 0, 컴퓨터: 보 2)

- ① -2
- ② 0
- ③ 1
- ④ 2

> **정답: ③ 1**  
> 파이썬에서는 나누는 수(3)가 양수이면 나머지가 항상 0 이상이 되도록 계산하므로 -2 % 3 = 1 → 이김입니다. (-2 = 3 × (-1) + 1)

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ③ |

## 코딩 테스트 1. 업다운 한 번 판정

```python
secret = int(input())
guess = int(input())
if guess == secret:
    print("정답")
elif guess < secret:
    print("UP")
else:
    print("DOWN")
```

**해설** 세 가지 경우가 서로 겹치지 않으므로 if–elif–else 한 묶음으로 처리합니다.

정답 코드 파일: [ch03_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch03_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch03_test1.py)

## 코딩 테스트 2. 가위바위보 한 판 판정

```python
choices = ["가위", "바위", "보"]
me, cpu = input().split()
diff = (choices.index(me) - choices.index(cpu)) % 3
if diff == 0:
    print("비김")
elif diff == 1:
    print("이김")
else:
    print("짐")
```

**해설** if를 9번 쓰는 대신 (나 - 컴퓨터) % 3 이 0, 1, 2 중 무엇인지로 판정합니다. 규칙의 **패턴**을 찾아 수식으로 표현한 것입니다.

정답 코드 파일: [ch03_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch03_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch03_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
