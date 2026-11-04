> **5부 테스트·프로젝트·공유** · 18차시 · 6단계 모형: **테스트 및 개선**  
> 게임: 업다운 개선 버전 (11_updown_safe.py) · 핑퐁 테스트  
> 핵심 개념: 문법 오류, 실행 오류, 논리 오류, 테스트 케이스, 경계값, 입력 검증, try-except, assert, 회귀 테스트

## 학습 목표

1. 문법 오류·실행 오류·논리 오류를 구분할 수 있다.
2. 정상·경계·예외 입력으로 테스트 케이스를 설계하고 실행 결과를 기록할 수 있다.
3. 입력 검증, try–except, 함수 분리로 오류를 수정하고 회귀 테스트를 할 수 있다.

## 핵심 질문

> **내가 만든 게임은 친구가 어떤 값을 입력해도 끝까지 올바르게 동작할까?**

`01_updown_basic.py`에 1~100 범위인데 **150**을 넣어 보세요. 오류 메시지도 없이 **기회만 1번 줄어듭니다.** 가위바위보 기본 버전에 `가위 `(뒤에 공백)를 넣으면 올바른 값인데도 거부됩니다.

**오류 메시지가 없다고 프로그램이 맞는 것은 아닙니다.** 이번 시간에는 일부러 게임을 '망가뜨리는' 입력을 설계해서 숨은 문제를 찾고 고칩니다.

## 오류의 세 종류

| 종류 | 언제 발견? | 예 | 메시지 |
| --- | --- | --- | --- |
| 문법 오류 | 실행 전 | `if guess == secret` (콜론 없음) | `SyntaxError` |
| 실행 오류 | 실행 중 멈춤 | `int("abc")`, 없는 키 `d["z"]` | `ValueError`, `KeyError` |
| 논리 오류 | 실행은 되지만 결과가 틀림 | 범위 밖 숫자로 기회 감소, `>=` 대신 `>` | 없음! |

논리 오류는 메시지가 없기 때문에 **테스트 케이스**로만 찾을 수 있습니다.

## 테스트 케이스 설계: 정상 · 경계 · 예외

**테스트 케이스 = 입력값 + 예상 결과.** 실행 전에 예상 결과를 먼저 적어야 합니다.

| 번호 | 구분 | 입력 | 예상 결과 | 실제 결과 (기본 버전) | 통과 |
| --- | --- | --- | --- | --- | --- |
| 1 | 정상 | 50 | UP/DOWN, 기회 1 감소 | 예상과 같음 | ○ |
| 2 | 경계 | 1, 100 | 범위 안 숫자로 처리 | 예상과 같음 | ○ |
| 3 | 경계 | 마지막 기회에 정답 | 성공 메시지 | 예상과 같음 | ○ |
| 4 | 예외 | abc | 다시 입력, 기회 유지 | 예상과 같음 | ○ |
| 5 | 예외 | 150 | 다시 입력, 기회 유지 | **기회가 줄어듦** | × |
| 6 | 예외 | " 50 " (앞뒤 공백) | 50으로 인정 | **숫자를 입력하세요** | × |
| 7 | 예외 | (빈 입력), -5 | 다시 입력 | 예상과 같음 | ○ |

- **경계값**: 가장 작은 값, 가장 큰 값, 마지막 기회처럼 '끝'에 있는 값. 오류가 가장 많이 숨어 있는 곳입니다.
- **예외 입력**: 문자, 빈 입력, 범위 밖, 공백, 음수 등 '이상한' 값

## 고치기: 검사를 함수 하나에 모으기

```python
def parse_guess(text, low, high):
    """low~high 범위의 정수이면 그 정수를, 아니면 None 을 돌려준다"""
    text = text.strip()                 # 공백 제거 (6번 해결)
    if not text.isdigit():              # 문자·빈 입력·음수 거부
        return None
    number = int(text)
    if not (low <= number <= high):     # 범위 검사 (5번 해결)
        return None
    return number
```

`input()`을 함수 밖으로 빼고 **문자열을 받아 결과를 돌려주는 순수 함수**로 만들면, 키보드 없이도 자동으로 테스트할 수 있습니다.

## 자동 테스트와 회귀 테스트

```python
cases = [("50", 50), ("1", 1), ("100", 100), ("150", None),
         ("abc", None), ("", None), ("-5", None), (" 50 ", 50)]
for text, expected in cases:
    actual = parse_guess(text, 1, 100)
    assert actual == expected, f"실패: {text!r} → {actual}"
print("모든 테스트 통과!")
```

```bash
python 11_updown_safe.py test
```

`assert 조건`은 조건이 거짓이면 즉시 오류를 냅니다. 코드를 고친 뒤 **이전 테스트를 모두 다시 실행해 다른 기능이 망가지지 않았는지 확인**하는 것을 **회귀 테스트**라고 합니다.

## try–except: 실행 오류 대비

```python
try:
    number = int(text)              # 오류가 날 수 있는 코드
except ValueError:                  # 그 오류가 나면 대신 실행
    print("숫자를 입력하세요!")
```

`isdigit()`으로 **미리 검사**하는 방법과 `try–except`로 **오류가 나면 처리**하는 방법이 있습니다. 둘 다 장단점이 있으니 상황에 맞게 고릅니다.

## 핑퐁 게임 테스트 케이스

그래픽 게임도 똑같이 테스트할 수 있습니다.

| 번호 | 상황 | 예상 결과 | 확인 방법 |
| --- | --- | --- | --- |
| 1 | 패들을 계속 위로 | 화면 위에 멈춤 | W 키 누르고 있기 |
| 2 | 공이 패들 모서리에 맞음 | 한 번만 튕김 | 여러 번 관찰 |
| 3 | 5점 도달 | 승리 문구, 공 정지 | WIN_SCORE=1로 바꿔 빠르게 확인 |
| 4 | 승리 후 R 키 | 0 : 0, 새 게임 | R 키 |
| 5 | 밀어내기 코드 삭제 | 공이 패들에 끼어 떨림 (버그 재현) | `ball.py` 주석 처리 |

**테스트를 쉽게 하려고 설정값을 잠시 바꾸는 것**(WIN_SCORE=1)도 좋은 테스트 기술입니다. 테스트가 끝나면 원래대로 돌려놓습니다.

## 실습 활동

1. 우리 모둠 게임의 테스트 케이스를 정상 2개 · 경계 2개 · 예외 3개 이상 활동지에 작성하세요. (예상 결과를 먼저!)
2. 옆 모둠과 노트북을 바꾸어 서로의 게임을 '테스터'로서 실행하고 실패 사례를 포스트잇으로 전달하세요.
3. 실패한 케이스를 고친 뒤 모든 케이스를 다시 실행(회귀 테스트)하여 통과 여부를 갱신하세요.

활동지: [ws18-test-debug.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws18-test-debug.md)

## 확인 퀴즈

**Q1.** 실행은 되지만 결과가 틀리는 오류는?

- ① 문법 오류
- ② 실행 오류
- ③ 논리 오류
- ④ 입력 오류

**Q2.** 1~100 범위 입력의 '경계값' 테스트로 가장 알맞은 것은?

- ① 50
- ② 1과 100
- ③ abc
- ④ 3.14

**Q3.** `int("abc")`를 실행하면 발생하는 오류는?

- ① SyntaxError
- ② ValueError
- ③ KeyError
- ④ IndexError

**Q4.** 테스트 케이스를 작성할 때 가장 먼저 적어야 하는 것은?

- ① 실제 결과
- ② 예상 결과
- ③ 수정 내용
- ④ 통과 여부

**Q5.** 코드를 고친 뒤 이전 테스트를 모두 다시 실행하는 것은?

- ① 단위 테스트
- ② 회귀 테스트
- ③ 부하 테스트
- ④ 사용자 테스트

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. parse_guess 구현 (기본)

`parse_guess(text, low, high)` 함수를 만드세요. 앞뒤 공백을 제거한 text가 숫자로만 되어 있고 low 이상 high 이하이면 그 정수를, 아니면 `None`을 반환합니다. 첫째 줄에 low high, 둘째 줄에 n, 다음 n줄 각각에 대한 반환값을 출력하세요.

- 입력: low high, n, n줄의 문자열 (빈 줄일 수도 있음)
- 출력: 각 줄의 반환값

예제 입력 1

```text
1 100
6
50
150
 abc
 7 

100
```

예제 출력 1

```text
50
None
None
7
None
100
```

### 문제 2. 안전한 나눗셈 계산기 (도전)

첫째 줄에 n, 다음 n줄에 `a b`가 주어집니다. a를 b로 나눈 몫을 출력하되, b가 0이면 `오류: 0으로 나눌 수 없음`, 정수가 아닌 값이 있으면 `오류: 정수가 아님`을 출력하세요. 두 가지가 함께 해당하면(예: `x 0`) 정수가 아님을 먼저 판단합니다. `try–except`를 사용하세요.

- 입력: n, n줄의 a b
- 출력: 몫 또는 오류 메시지

예제 입력 1

```text
4
10 3
7 0
x 2
-9 2
```

예제 출력 1

```text
3
오류: 0으로 나눌 수 없음
오류: 정수가 아님
-5
```

정답과 해설은 **[부록] 06-1-18. 18차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-18-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 오류 3종: 문법(실행 전) · 실행(멈춤) · 논리(메시지 없음)
- 테스트 케이스 = 입력 + 예상 결과, 정상·경계·예외
- 검사는 함수 하나에 → 자동 테스트(assert) 가능
- 고친 뒤에는 회귀 테스트

## 교사용 메모

본시(수업 지도안 대상 차시). 동기 유발 3분 → 목표 안내 2분 → 개념 5분 → 탐구1 테스트 설계 7분 → 탐구2 교차 테스트 7분 → 탐구3 입력 검증 구현 8분 → 개선 논의 4분 → 심화 5분 → 공유·정리 4분 (45분 기준, 50분 수업은 탐구 시간을 늘림).

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `01_updown_basic.py` | [01_updown_basic.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/01_updown_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/01_updown_basic.py) |
| 소스코드 `11_updown_safe.py` | [11_updown_safe.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/11_updown_safe.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/11_updown_safe.py) |
| 소스코드 `ball.py` | [ball.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/ball.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/ball.py) |
| 학습용 PPT | [18-test-debug.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/18-test-debug.pptx) |
| 학생 활동지 | [ws18-test-debug.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws18-test-debug.md) |
| 코딩 테스트 1 정답 코드 | [ch18_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch18_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch18_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch18_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch18_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch18_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
