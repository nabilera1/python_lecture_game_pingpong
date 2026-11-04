> 18차시 **테스트 케이스로 오류 찾고 개선하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 실행은 되지만 결과가 틀리는 오류는?

- ① 문법 오류
- ② 실행 오류
- ③ 논리 오류
- ④ 입력 오류

> **정답: ③ 논리 오류**  
> 논리 오류는 메시지가 없어서 테스트 케이스로 찾아야 합니다.

**Q2.** 1~100 범위 입력의 '경계값' 테스트로 가장 알맞은 것은?

- ① 50
- ② 1과 100
- ③ abc
- ④ 3.14

> **정답: ② 1과 100**  
> 범위의 양 끝 값이 경계값입니다. 0, 101도 경계 바로 바깥값으로 함께 테스트하면 좋습니다.

**Q3.** `int("abc")`를 실행하면 발생하는 오류는?

- ① SyntaxError
- ② ValueError
- ③ KeyError
- ④ IndexError

> **정답: ② ValueError**  
> 숫자로 바꿀 수 없는 문자열이므로 ValueError입니다.

**Q4.** 테스트 케이스를 작성할 때 가장 먼저 적어야 하는 것은?

- ① 실제 결과
- ② 예상 결과
- ③ 수정 내용
- ④ 통과 여부

> **정답: ② 예상 결과**  
> 실행 전에 예상 결과를 정해야 실제 결과와 비교할 수 있습니다.

**Q5.** 코드를 고친 뒤 이전 테스트를 모두 다시 실행하는 것은?

- ① 단위 테스트
- ② 회귀 테스트
- ③ 부하 테스트
- ④ 사용자 테스트

> **정답: ② 회귀 테스트**  
> 수정이 다른 기능을 망가뜨리지 않았는지 확인하는 회귀 테스트입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ③ | ② | ② | ② | ② |

## 코딩 테스트 1. parse_guess 구현

```python
def parse_guess(text, low, high):
    text = text.strip()
    if not text.isdigit():
        return None
    number = int(text)
    if not (low <= number <= high):
        return None
    return number

low, high = map(int, input().split())
for _ in range(int(input())):
    print(parse_guess(input(), low, high))
```

**해설** 검사 순서가 중요합니다. strip → isdigit → int → 범위 순서로 해야 `int()`에서 ValueError가 나지 않습니다. 빈 문자열의 `isdigit()`은 False입니다. 참고로 `isdigit()`은 ①, ² 같은 특수 숫자도 True라서 `int()`에서 오류가 날 수 있습니다. 더 엄격하게 검사하려면 `isdecimal()`을 쓰거나 `try–except`를 함께 씁니다.

정답 코드 파일: [ch18_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch18_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch18_test1.py)

## 코딩 테스트 2. 안전한 나눗셈 계산기

```python
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ValueError:
        print("오류: 정수가 아님")
    except ZeroDivisionError:
        print("오류: 0으로 나눌 수 없음")
```

**해설** except를 여러 개 두어 오류 종류별로 다르게 처리할 수 있습니다. `-9 // 2`는 -4.5보다 작거나 같은 가장 큰 정수인 -5입니다(내림).

정답 코드 파일: [ch18_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch18_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch18_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
