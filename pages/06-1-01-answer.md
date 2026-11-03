> 1차시 **놀이 속 알고리즘 찾기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 문제를 해결하기 위한 절차를 순서대로 명확하게 나타낸 것은?

- ① 프로그램
- ② 알고리즘
- ③ 컴파일러
- ④ 운영체제

> **정답: ② 알고리즘**  
> 알고리즘은 문제 해결 절차이고, 이를 프로그래밍 언어로 표현한 것이 프로그램입니다.

**Q2.** `print("=" * 3)`의 실행 결과는?

- ① = * 3
- ② ===
- ③ 3
- ④ 오류 발생

> **정답: ② ===**  
> 문자열에 정수를 곱하면 그 횟수만큼 반복된 문자열이 됩니다.

**Q3.** 업다운 게임에서 '정답과 비교하여 크다/작다를 판단'하는 것은 IPO 중 무엇인가?

- ① 입력
- ② 처리
- ③ 출력
- ④ 저장

> **정답: ② 처리**  
> 컴퓨터가 판단·계산하는 단계는 처리(Process)입니다.

**Q4.** 파이썬에서 주석을 시작하는 기호는?

- ① //
- ② /*
- ③ #
- ④ --

> **정답: ③ #**  
> 파이썬은 `#` 뒤의 내용을 주석으로 처리합니다.

**Q5.** `print("기회는", 7, "번")`의 출력으로 옳은 것은?

- ① 기회는7번
- ② 기회는 7 번
- ③ "기회는" 7 "번"
- ④ 기회는, 7, 번

> **정답: ② 기회는 7 번**  
> 쉼표로 여러 값을 출력하면 값 사이에 공백이 하나씩 들어갑니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ③ | ② |

## 코딩 테스트 1. 게임 타이틀 화면 출력

```python
print("=" * 20)
print("   UP & DOWN GAME")
print("=" * 20)
```

**해설** 같은 문자를 여러 번 출력할 때는 직접 20번 쓰기보다 `"=" * 20`처럼 반복 연산을 쓰면 실수가 줄고 수정도 쉽습니다.

정답 코드 파일: [ch01_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch01_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch01_test1.py)

## 코딩 테스트 2. 플레이어 환영 인사

```python
name = input()
print(name + "님, 게임을 시작합니다!")
```

**해설** `input()`으로 받은 값은 문자열이므로 `+`로 다른 문자열과 이어 붙일 수 있습니다. `print(name, "님...")`처럼 쉼표를 쓰면 사이에 공백이 생겨 출력 형식이 달라집니다.

정답 코드 파일: [ch01_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch01_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch01_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
