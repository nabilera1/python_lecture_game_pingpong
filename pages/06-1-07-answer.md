> 7차시 **리스트 누적·비교와 문자열 메서드: 기억력 게임**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `[1, 2, 3] == [3, 2, 1]`의 결과는?

- ① True
- ② False
- ③ 오류
- ④ [1,2,3]

> **정답: ② False**  
> 리스트 비교는 순서까지 같아야 True입니다.

**Q2.** `"  y  ".strip().upper()`의 결과는?

- ① "  Y  "
- ② "Y"
- ③ "y"
- ④ "  y"

> **정답: ② "Y"**  
> strip으로 공백을 지운 뒤 upper로 대문자로 바꿉니다.

**Q3.** `"hello".find("z")`의 결과는?

- ① 0
- ② -1
- ③ None
- ④ 오류

> **정답: ② -1**  
> find는 찾는 글자가 없으면 -1을 돌려줍니다.

**Q4.** `while True:` 반복을 끝내려면 반복 안에 무엇이 필요한가?

- ① continue
- ② break
- ③ else
- ④ pass

> **정답: ② break**  
> 조건이 항상 참이므로 break(또는 함수의 return)가 있어야 끝납니다.

**Q5.** `text = " 5 "` 다음 `text.strip()`만 실행했을 때 `text`의 값은?

- ① "5"
- ② " 5 "
- ③ 5
- ④ ""

> **정답: ② " 5 "**  
> 메서드는 원본을 바꾸지 않습니다. `text = text.strip()`처럼 다시 저장해야 합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. 기억력 정답 확인

```python
shown = input().replace(" ", "")
typed = input().replace(" ", "")
print("정답" if shown == typed else "오답")
```

**해설** 양쪽 모두 같은 방식으로 정리(정규화)한 뒤 비교해야 공정한 판정이 됩니다.

정답 코드 파일: [ch07_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch07_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch07_test1.py)

## 코딩 테스트 2. 이메일 아이디와 도메인 분리

```python
email = input().strip()
idx = email.find("@")
if idx == -1:
    print("올바른 이메일이 아닙니다")
else:
    print(f"아이디: {email[:idx]}, 도메인: {email[idx + 1:]}")
```

**해설** find의 결과가 -1인지 먼저 검사하는 것이 예외 처리의 시작입니다. -1을 검사하지 않으면 `email[:-1]`처럼 엉뚱한 결과가 나옵니다.

정답 코드 파일: [ch07_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch07_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch07_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
