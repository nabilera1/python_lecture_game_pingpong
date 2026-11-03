> 6차시 **for 반복문과 문자열: 숫자 야구**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `range(2, 8, 3)`이 만드는 값은?

- ① 2, 5
- ② 2, 5, 8
- ③ 2, 3, 4, 5, 6, 7
- ④ 3, 6

> **정답: ① 2, 5**  
> 2에서 시작해 3씩 증가, 8은 포함하지 않으므로 2, 5입니다.

**Q2.** `s = "python"`일 때 `s[1:4]`는?

- ① pyt
- ② yth
- ③ ytho
- ④ tho

> **정답: ② yth**  
> 1번(y)부터 4번 앞(3번 h)까지입니다.

**Q3.** 정답 `['3','5','8']`, 추측 `['5','3','8']`의 결과는?

- ① 3S 0B
- ② 1S 2B
- ③ 2S 1B
- ④ 0S 3B

> **정답: ② 1S 2B**  
> 8은 자리까지 같아 1S, 5와 3은 자리만 달라 2B입니다.

**Q4.** `"-".join(["a", "b", "c"])`의 결과는?

- ① abc
- ② a-b-c
- ③ -a-b-c-
- ④ ['a','b','c']

> **정답: ② a-b-c**  
> join은 리스트 값 사이에 앞의 문자열을 넣어 이어 붙입니다.

**Q5.** 정해진 횟수만큼 반복할 때 주로 쓰는 반복문은?

- ① while True
- ② for ~ in range()
- ③ if ~ else
- ④ try ~ except

> **정답: ② for ~ in range()**  
> 횟수가 정해져 있으면 for와 range 조합이 간결합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ① | ② | ② | ② | ② |

## 코딩 테스트 1. 스트라이크·볼 계산기

```python
answer, guess = input().split()
strike = ball = 0
for i in range(3):
    if guess[i] == answer[i]:
        strike += 1
    elif guess[i] in answer:
        ball += 1
print(f"{strike}S {ball}B")
```

**해설** 문자열도 인덱싱과 `in`을 쓸 수 있으므로 굳이 리스트로 바꾸지 않아도 됩니다.

정답 코드 파일: [ch06_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch06_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch06_test1.py)

## 코딩 테스트 2. 자릿수 합과 거꾸로 읽기

```python
s = input()
total = 0
for ch in s:
    total += int(ch)
print(total)
print(s[::-1])
```

**해설** for 문으로 글자를 하나씩 꺼내 int로 바꿔 더합니다. 슬라이싱 `[::-1]`은 간격 -1, 즉 뒤에서부터 읽기입니다.

정답 코드 파일: [ch06_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch06_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch06_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
