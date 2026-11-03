> 2차시 **게임 데이터 추상화: 변수·자료형·입력**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 문제의 핵심 요소만 남기고 불필요한 부분을 제거하는 과정은?

- ① 분해
- ② 추상화
- ③ 자동화
- ④ 일반화

> **정답: ② 추상화**  
> 핵심만 남기는 것이 추상화, 큰 문제를 작은 문제로 나누는 것이 분해입니다.

**Q2.** `x = input()`에 `10`을 입력했을 때 `x`의 자료형은?

- ① int
- ② float
- ③ str
- ④ bool

> **정답: ③ str**  
> `input()`은 항상 문자열(str)을 돌려줍니다.

**Q3.** `17 // 5`와 `17 % 5`의 결과를 순서대로 고르면?

- ① 3, 2
- ② 3.4, 2
- ③ 2, 3
- ④ 3, 3

> **정답: ① 3, 2**  
> 17 = 5 × 3 + 2 이므로 몫은 3, 나머지는 2입니다.

**Q4.** 변수 이름으로 사용할 수 **없는** 것은?

- ① best_score
- ② _chance
- ③ 2player
- ④ lowValue

> **정답: ③ 2player**  
> 변수 이름은 숫자로 시작할 수 없습니다.

**Q5.** `chance = 7` 다음에 `chance -= 2`를 실행하면 chance의 값은?

- ① 7
- ② 5
- ③ -2
- ④ 9

> **정답: ② 5**  
> `chance -= 2`는 `chance = chance - 2`와 같습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ③ | ① | ③ | ② |

## 코딩 테스트 1. 두 수의 사칙연산

```python
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a // b)
print(a % b)
```

**해설** `input().split()`은 공백으로 나눈 문자열 리스트를 만들고, `map(int, ...)`는 각각을 정수로 바꿉니다.

정답 코드 파일: [ch02_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch02_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch02_test1.py)

## 코딩 테스트 2. 플레이 시간 변환

```python
sec = int(input())
print(f"{sec // 60}분 {sec % 60}초")
```

**해설** 60으로 나눈 몫이 분, 나머지가 초입니다. f-문자열 `f"{식}"`을 쓰면 계산 결과를 문자열 안에 바로 넣을 수 있습니다.

정답 코드 파일: [ch02_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch02_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch02_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
