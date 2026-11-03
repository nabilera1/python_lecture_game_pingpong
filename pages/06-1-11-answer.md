> 11차시 **종합 실습: 영단어 행맨**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `all([True, False, True])`의 결과는?

- ① True
- ② False
- ③ 2
- ④ 오류

> **정답: ② False**  
> 하나라도 거짓이 있으면 all은 False입니다.

**Q2.** word="cat", guessed=['a']일 때 `" ".join(ch if ch in guessed else "_" for ch in word)`는?

- ① _ a _
- ② c a t
- ③ a
- ④ _ _ _

> **정답: ① _ a _**  
> 맞힌 a만 보이고 나머지는 _입니다.

**Q3.** `3 + True + False`의 값은?

- ① 3
- ② 4
- ③ 5
- ④ 오류

> **정답: ② 4**  
> True는 1, False는 0으로 계산됩니다.

**Q4.** `"A".isalpha() and len("A") == 1`의 결과는?

- ① True
- ② False
- ③ "A"
- ④ 1

> **정답: ① True**  
> 알파벳이고 길이도 1이므로 True입니다.

**Q5.** 행맨의 `ask_letter`가 다시 입력을 요구하는 경우가 **아닌** 것은?

- ① "ab"
- ② "3"
- ③ 이미 쓴 글자
- ④ 처음 쓰는 "k"

> **정답: ④ 처음 쓰는 "k"**  
> 처음 쓰는 알파벳 한 글자는 그대로 반환됩니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ① | ② | ① | ④ |

## 코딩 테스트 1. 행맨 보드 출력

```python
word = input()
guessed = input().split()
print(" ".join(ch if ch in guessed else "_" for ch in word))
```

**해설** 같은 글자가 여러 번 나와도(loop의 o) 한 번 맞히면 모두 보입니다. 각 글자를 따로 검사하기 때문입니다.

정답 코드 파일: [ch11_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch11_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch11_test1.py)

## 코딩 테스트 2. 행맨 한 판 시뮬레이션

```python
word = input()
letters = input().split()
guessed = []
lives = 6
result = None
for ch in letters:
    guessed.append(ch)
    if ch not in word:
        lives -= 1
    if lives == 0:
        result = "실패"
        break
    if all(c in guessed for c in word):
        result = f"성공 {lives}"
        break
print(result if result else f"진행 중 {lives}")
```

**해설** 매 글자마다 '목숨이 0인가?'와 '모두 맞혔나?'를 검사합니다. 결과를 변수에 담아 두고 마지막에 한 번 출력하면 종료 경우가 여러 개여도 깔끔합니다.

정답 코드 파일: [ch11_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch11_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch11_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
