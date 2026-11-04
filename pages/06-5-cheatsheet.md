## 입출력과 변수

| 코드 | 뜻 |
| --- | --- |
| `print(a, b)` | 출력 (사이 공백) |
| `print(a, end="")` | 줄 바꿈 없이 출력 |
| `x = input("안내 > ")` | 입력 (항상 문자열) |
| `n = int(input())` | 정수로 입력 |
| `a, b = map(int, input().split())` | 한 줄에 정수 두 개 |
| `f"점수 {score}점"` | f-문자열 |
| `f"{avg:.1f}"` | 소수 첫째 자리 |

## 연산자

| 종류 | 연산자 |
| --- | --- |
| 산술 | `+ - * / // % **` |
| 비교 | `== != < > <= >=` |
| 논리 | `and or not` |
| 포함 | `in`, `not in` |
| 복합 대입 | `+= -= *=` |

## 조건과 반복

```python
if 조건:
    ...
elif 다른조건:
    ...
else:
    ...

while 조건:          # break 탈출, continue 다음 반복
    ...

for i in range(시작, 끝, 간격):   # 끝은 미포함
    ...
```

## 자료구조

| 자료구조 | 만들기 | 읽기 | 추가/수정 |
| --- | --- | --- | --- |
| 리스트 | `a = [1, 2, 3]` | `a[0]`, `a[-1]`, `a[1:3]` | `a.append(4)`, `a[0] = 9` |
| 2차원 리스트 | `g = [[0, 1], [2, 3]]` | `g[행][열]` | `g[1][0] = 5` |
| 딕셔너리 | `d = {"win": 0}` | `d["win"]`, `d.get("x", 0)` | `d["win"] += 1` |
| 튜플 | `pos = (2, 3)` | `pos[0]` | 바꿀 수 없음 |
| 집합 | `s = {(0, 0)}` | `(0, 0) in s` | `s.add((1, 0))` |

## 문자열 메서드

`strip()` `replace(a, b)` `split()` `join()` `lower()` `upper()` `isdigit()` `isalpha()` `find()`

## 함수와 클래스

```python
def 함수이름(매개변수, 기본값=1):
    return 결과

class 클래스이름:
    def __init__(self, 값):
        self.속성 = 값
    def 메서드(self):
        return self.속성

obj = 클래스이름(10)
obj.메서드()
```

## 특수 문자 입력 (♥ ♡ ↑ ↓ ★)

| 방법 | 하는 법 |
| --- | --- |
| 윈도우 한글 자판 | 한글 상태에서 **ㅁ** 입력 → **한자** 키 → **Tab**으로 목록 펼치기 → 기호 선택 |
| 맥 | **Control + Command + Space** → 문자 뷰어에서 검색 |
| 유니코드 | `"\u2665"` ♥, `"\u2661"` ♡, `"\u2191"` ↑, `"\u2193"` ↓, `"\u2605"` ★ |
| 복사·붙여 넣기 | 이 페이지의 기호를 복사해 코드에 붙여 넣기 |

자세한 설명은 11차시 '♥ ♡ 같은 특수 문자 입력하기'를 참고하세요.

## 오류 처리

```python
try:
    n = int(text)
except ValueError:
    print("숫자가 아니에요")
```

## pygame 게임 루프

```python
while running:
    for event in pygame.event.get():   # 입력
        ...
    update()                           # 업데이트
    screen.fill(BLACK); draw()         # 그리기
    pygame.display.flip()
    clock.tick(60)                     # 시간 조절
```
