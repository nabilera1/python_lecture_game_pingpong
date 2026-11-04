> 4차시 **순서도와 while 반복문: 업다운 완성**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 반복문을 즉시 빠져나오게 하는 키워드는?

- ① continue
- ② break
- ③ pass
- ④ return

> **정답: ② break**  
> `break`는 반복을 끝내고, `continue`는 다음 반복으로 건너뜁니다.

**Q2.** 다음 코드의 출력 횟수는?

```python
n = 0
while n < 3:
    print(n)
    n += 1
```

- ① 2번
- ② 3번
- ③ 4번
- ④ 무한 번

> **정답: ② 3번**  
> n이 0, 1, 2일 때 출력하고 3이 되면 조건이 거짓이 됩니다.

**Q3.** 순서도에서 조건을 검사하여 흐름을 나누는 기호는?

- ① 사각형
- ② 평행사변형
- ③ 마름모
- ④ 둥근 사각형

> **정답: ③ 마름모**  
> 판단(조건)은 마름모로 나타냅니다.

**Q4.** `while ~ else`의 else 블록이 실행되는 경우는?

- ① break로 반복이 끝났을 때
- ② 조건이 거짓이 되어 반복이 끝났을 때
- ③ 항상
- ④ continue를 만났을 때

> **정답: ② 조건이 거짓이 되어 반복이 끝났을 때**  
> else는 break 없이 정상적으로 끝났을 때만 실행됩니다. 업다운에서는 '실패' 처리에 쓰였습니다.

**Q5.** 1~1000 범위에서 이진 탐색으로 반드시 맞히는 데 필요한 최소 기회는?

- ① 7번
- ② 9번
- ③ 10번
- ④ 100번

> **정답: ③ 10번**  
> k번 시도로 반드시 찾을 수 있는 범위는 최대 2ᵏ − 1개입니다. 2⁹ − 1 = 511 < 1000 ≤ 1023 = 2¹⁰ − 1 이므로 10번이 필요합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ③ | ② | ③ |

## 코딩 테스트 1. 1부터 n까지의 합

```python
n = int(input())
i, total = 1, 0
while i <= n:
    total += i
    i += 1
print(total)
```

**해설** 반복 변수 i를 1씩 늘려 조건 `i <= n`이 거짓이 되면 반복이 끝납니다. `i += 1`이 없으면 무한 반복입니다.

정답 코드 파일: [ch04_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch04_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch04_test1.py)

## 코딩 테스트 2. 업다운 기록 판정기

```python
secret = int(input())
n = int(input())
count = 0
while count < n:
    guess = int(input())
    count += 1
    if guess == secret:
        print(f"정답! {count}번 만에 성공")
        break
    elif guess < secret:
        print("UP")
    else:
        print("DOWN")
else:
    print(f"실패! 정답은 {secret}")
```

**해설** 정답을 맞히면 `break`로 나가므로 남은 입력은 읽지 않습니다. `while ~ else`로 '끝까지 못 맞힌 경우'만 깔끔하게 처리했습니다.

정답 코드 파일: [ch04_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch04_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch04_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
