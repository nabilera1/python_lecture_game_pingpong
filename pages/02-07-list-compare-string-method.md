> **2부 리스트와 반복으로 게임 만들기** · 7차시 · 6단계 모형: **컴퓨팅 설계**  
> 게임: 기억력 게임 (기본 버전)  
> 핵심 개념: while True, 리스트 누적, 리스트 비교, strip, replace, split, find, time.sleep

## 학습 목표

1. 반복할 때마다 리스트에 값을 누적하고, 리스트끼리 비교할 수 있다.
2. strip, replace, split, lower, find 등 문자열 메서드를 목적에 맞게 사용할 수 있다.
3. 무한 반복(while True)과 break로 종료 시점을 제어할 수 있다.

## 핵심 질문

> **사용자의 입력을 '공정하게' 비교하려면 무엇을 정리해야 할까?**

기억력 게임은 라운드마다 숫자가 하나씩 늘어나고, 플레이어가 **본 그대로** 입력했는지 비교합니다.
그런데 `3 8`처럼 공백을 넣거나 앞뒤에 실수로 스페이스를 넣으면 같은 답인데도 틀렸다고 판정할 수 있습니다. **문자열 메서드**로 입력을 정리하면 이런 문제를 막을 수 있습니다.

## 무한 반복과 누적

```python
seq = []
while True:                                   # 항상 참 → break 를 만나야 끝
    seq.append(random.choice("123456789"))    # 라운드마다 1개씩 누적
    print("기억하세요:", " ".join(seq))
    time.sleep(1 + len(seq) * 0.5)            # 길수록 오래 보여 주기
    print("\n" * 40)                          # 화면 밀어 올리기
    guess = list(input("입력 > ").replace(" ", ""))
    if guess == seq:                          # 리스트끼리 비교
        print("정답! 다음 라운드로!")
    else:
        print("틀렸어요! 정답은", "".join(seq))
        break
```

리스트끼리 `==` 비교는 **길이, 순서, 값이 모두 같을 때만** True입니다. `['3','8'] == ['8','3']`은 False입니다.

## 자주 쓰는 문자열 메서드

| 메서드 | 예시 | 결과 | 게임 속 쓰임 |
| --- | --- | --- | --- |
| `strip()` | `" 가위 ".strip()` | `"가위"` | 앞뒤 공백 실수 방지 |
| `replace(a, b)` | `"3 8".replace(" ", "")` | `"38"` | 공백 모두 제거 |
| `split()` | `"3 5 7".split()` | `['3','5','7']` | 여러 값 입력 |
| `lower()` / `upper()` | `"Y".lower()` | `"y"` | 대소문자 통일 |
| `isdigit()` | `"12".isdigit()` | `True` | 숫자인지 검사 |
| `isalpha()` | `"a".isalpha()` | `True` | 글자(문자)인지 검사 — 한글도 True |
| `find(s)` | `"a@b.kr".find("@")` | `1` | 글자 위치 찾기 (없으면 -1) |

메서드는 **원래 문자열을 바꾸지 않고 새 문자열을 돌려줍니다.** 그래서 `text = text.strip()`처럼 다시 저장해야 합니다.

## find와 슬라이싱 응용

```python
email = "student@school.ac.kr"
idx = email.find("@")        # 7
user_id = email[:idx]        # student
domain = email[idx + 1:]     # school.ac.kr
print(f"아이디: {user_id}, 도메인: {domain}")
```

## 실습 활동

1. `04_memory_basic.py`에서 사용할 숫자를 1~9 대신 알파벳 A~E로 바꿔 보세요.
2. 입력 앞뒤에 공백이 있어도 정답으로 인정되도록 `strip()`을 추가해 보세요.
3. IDLE에서는 스크롤을 올리면 숫자가 보이는 문제가 있습니다. 어떤 방법으로 개선할 수 있을지 모둠별로 아이디어를 내 보세요.

활동지: [ws07-list-compare-string-method.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws07-list-compare-string-method.md)

## 확인 퀴즈

**Q1.** `[1, 2, 3] == [3, 2, 1]`의 결과는?

- ① True
- ② False
- ③ 오류
- ④ [1,2,3]

**Q2.** `"  y  ".strip().upper()`의 결과는?

- ① "  Y  "
- ② "Y"
- ③ "y"
- ④ "  y"

**Q3.** `"hello".find("z")`의 결과는?

- ① 0
- ② -1
- ③ None
- ④ 오류

**Q4.** `while True:` 반복을 끝내려면 반복 안에 무엇이 필요한가?

- ① continue
- ② break
- ③ else
- ④ pass

**Q5.** `text = " 5 "` 다음 `text.strip()`만 실행했을 때 `text`의 값은?

- ① "5"
- ② " 5 "
- ③ 5
- ④ ""

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 기억력 정답 확인 (기본)

첫째 줄에 보여 준 숫자열, 둘째 줄에 플레이어 입력이 주어집니다. 공백을 모두 무시하고 같으면 `정답`, 다르면 `오답`을 출력하세요.

- 입력: 두 줄의 문자열
- 출력: 정답 또는 오답

예제 입력 1

```text
3 8 1
381
```

예제 출력 1

```text
정답
```

예제 입력 2

```text
3 8 1
 3 8  1 
```

예제 출력 2

```text
정답
```

예제 입력 3

```text
381
318
```

예제 출력 3

```text
오답
```

### 문제 2. 이메일 아이디와 도메인 분리 (도전)

이메일 주소를 입력받아 `아이디: ○○, 도메인: ○○` 형식으로 출력하세요. `@`가 없으면 `올바른 이메일이 아닙니다`를 출력하세요.

- 입력: 첫째 줄에 문자열
- 출력: 형식에 맞게 출력

예제 입력 1

```text
student@school.ac.kr
```

예제 출력 1

```text
아이디: student, 도메인: school.ac.kr
```

예제 입력 2

```text
hello
```

예제 출력 2

```text
올바른 이메일이 아닙니다
```

정답과 해설은 **[부록] 06-1-07. 7차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-07-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- while True + break: 종료 시점을 반복 안에서 결정
- 리스트 == 비교는 길이·순서·값이 모두 같아야 True
- strip · replace · split · lower · isdigit · find
- 메서드는 새 값을 돌려줌 → 다시 저장

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `04_memory_basic.py` | [04_memory_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/04_memory_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/04_memory_basic.py) |
| 학습용 PPT | [07-list-compare-string-method.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/07-list-compare-string-method.pptx) |
| 학생 활동지 | [ws07-list-compare-string-method.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws07-list-compare-string-method.md) |
| 코딩 테스트 1 정답 코드 | [ch07_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch07_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch07_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch07_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch07_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch07_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
