> 8차시 **함수로 나누기: 업다운·기억력 게임 함수 버전**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 함수를 정의할 때 사용하는 키워드는?

- ① func
- ② def
- ③ function
- ④ define

> **정답: ② def**  
> 파이썬은 `def`로 함수를 정의합니다.

**Q2.** 다음 코드의 출력은?

```python
def f(a, b=10):
    return a + b
print(f(5), f(5, 1))
```

- ① 15 15
- ② 15 6
- ③ 5 6
- ④ 오류

> **정답: ② 15 6**  
> b를 생략하면 기본값 10, 넘기면 그 값을 씁니다.

**Q3.** `return` 문에 대한 설명으로 옳지 **않은** 것은?

- ① 값을 돌려준다
- ② 함수를 즉시 끝낸다
- ③ 반복문 안에서도 쓸 수 있다
- ④ 함수 밖에서도 쓸 수 있다

> **정답: ④ 함수 밖에서도 쓸 수 있다**  
> return은 함수 안에서만 쓸 수 있습니다.

**Q4.** `judge(guess, secret)`에서 guess, secret을 무엇이라 하는가?

- ① 인수
- ② 매개변수
- ③ 반환값
- ④ 전역 변수

> **정답: ② 매개변수**  
> 정의할 때의 이름은 매개변수, 호출할 때 넣는 실제 값은 인수입니다.

**Q5.** `if __name__ == "__main__":`의 역할은?

- ① 오류를 막는다
- ② 파일을 직접 실행할 때만 아래 코드를 실행한다
- ③ main 함수를 정의한다
- ④ 모듈을 설치한다

> **정답: ② 파일을 직접 실행할 때만 아래 코드를 실행한다**  
> import될 때는 __name__이 파일 이름이므로 실행되지 않습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ④ | ② | ② |

## 코딩 테스트 1. judge 함수 만들기

```python
def judge(guess, secret):
    if guess == secret:
        return "correct"
    return "up" if guess < secret else "down"

secret = int(input())
n = int(input())
for _ in range(n):
    print(judge(int(input()), secret))
```

**해설** 판정 로직을 함수로 분리하면 입력 방식이 바뀌어도(키보드, 파일, 자동 테스트) 함수는 그대로 재사용할 수 있습니다.

정답 코드 파일: [ch08_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch08_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch08_test1.py)

## 코딩 테스트 2. 입력 검사 함수

```python
def is_valid(text, low, high):
    if not text.isdigit():
        return False
    return low <= int(text) <= high

low, high = map(int, input().split())
n = int(input())
for _ in range(n):
    print(is_valid(input(), low, high))
```

**해설** 숫자인지 먼저 검사한 뒤 int로 바꿔야 `int("abc")` 오류가 나지 않습니다. 검사 순서도 알고리즘의 일부입니다. 18차시에서는 이 함수를 공백 제거까지 하는 `parse_guess()`로 발전시킵니다.

정답 코드 파일: [ch08_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch08_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch08_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
