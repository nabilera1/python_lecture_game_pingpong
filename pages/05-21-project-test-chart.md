> **5부 테스트·프로젝트·공유** · 21차시 · 6단계 모형: **공유·확장**  
> 게임: 동료 테스트 · 코드 리뷰 체크리스트 · 최종 차트  
> 핵심 개념: 동료 테스트, 버그 리포트, 리팩터링, 코드 리뷰, 가독성, 차트-코드 일치

## 학습 목표

1. 동료 테스트로 발견한 문제를 분석하고 수정할 수 있다.
2. 중복 코드·이름·주석을 점검하여 코드를 리팩터링할 수 있다.
3. 완성한 프로그램과 일치하는 최종 차트(순서도·구조도·테스트 결과표)를 작성할 수 있다.

## 핵심 질문

> **'돌아가는 코드'를 '다른 사람도 이해하고 믿을 수 있는 코드'로 만들려면 무엇을 해야 할까?**

18차시에 배운 테스트 방법을 이제 **우리 프로젝트**에 적용합니다. 다른 모둠이 우리 게임을 테스트하고, 우리는 받은 버그 리포트로 코드를 고칩니다. 마지막으로 **완성된 코드와 일치하는 차트**를 정리합니다.

## 버그 리포트 쓰는 법

좋은 버그 리포트는 **누구나 같은 문제를 다시 만들 수 있게(재현)** 써야 합니다.

| 항목 | 좋은 예 | 나쁜 예 |
| --- | --- | --- |
| 상황 | 3점 상태에서 공이 패들 위쪽 모서리에 맞을 때 | 가끔 |
| 입력/행동 | W 키를 누른 채로 공을 받음 | 그냥 함 |
| 기대 결과 | 공이 한 번 튕겨 나감 | 잘 됨 |
| 실제 결과 | 공이 패들 안에서 3번 떨리다가 통과함 | 이상함 |

## 리팩터링 체크리스트

| 점검 | 질문 | 고치는 방법 |
| --- | --- | --- |
| 중복 | 같은 코드가 2번 이상 나오나? | 함수로 묶기 |
| 이름 | `a`, `tmp` 같은 이름이 있나? | `ball_speed`처럼 의미 있게 |
| 숫자 | 코드 속에 이유 모를 숫자(매직 넘버)가 있나? | 상수로 (`WIN_SCORE = 5`) |
| 주석 | 처음 보는 사람이 이해할까? | '왜'를 설명하는 주석 |
| 길이 | 한 함수가 30줄을 넘나? | 하위 문제로 다시 분해 |
| 예외 | 이상한 입력에 멈추나? | 입력 검증, try–except |

리팩터링 후에는 반드시 **회귀 테스트**를 다시 실행합니다.

## 매직 넘버를 상수로 (예)

```python
# 고치기 전
if self.left_score >= 5:
    ...
pygame.draw.line(self.screen, (90, 90, 110), (400, y), (400, y + 16), 3)

# 고친 후
if self.left_score >= WIN_SCORE:
    ...
pygame.draw.line(self.screen, GRAY, (SCREEN_WIDTH // 2, y), (SCREEN_WIDTH // 2, y + dash_height), 3)
```

핑퐁 완성본이 `constants.py`를 따로 둔 이유가 바로 이것입니다.

## 최종 차트 정리

평가 요소 '**차트 작성(진행한 프로젝트에 대한 이해)**'에서는 **제작한 산출물과 차트의 내용이 일치하는지** 확인합니다.

1. **순서도 / 상태 다이어그램**: 실제 코드의 반복·분기와 같은가?
2. **클래스 구조도 / 함수 설계표**: 실제 이름·매개변수·반환값과 같은가?
3. **테스트 결과표**: 몇 개 중 몇 개 통과? 실패를 어떻게 고쳤나?

설계 단계(19차시) 차트와 비교해 **무엇이 왜 바뀌었는지** 한 줄씩 적으면 성찰 자료가 됩니다.

## 실습 활동

1. 다른 모둠 게임을 테스트하고 버그 리포트를 2개 이상 작성해 전달하세요.
2. 받은 버그 리포트로 코드를 고치고 회귀 테스트를 실행하세요.
3. 리팩터링 체크리스트로 우리 코드를 점검하고, 최종 차트를 완성하세요.

활동지: [ws21-project-test-chart.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws21-project-test-chart.md)

## 확인 퀴즈

**Q1.** 좋은 버그 리포트의 가장 중요한 조건은?

- ① 길게 쓰기
- ② 누구나 같은 문제를 재현할 수 있게 쓰기
- ③ 범인을 밝히기
- ④ 코드를 함께 붙이기

**Q2.** 리팩터링의 뜻으로 알맞은 것은?

- ① 새 기능 추가
- ② 동작은 그대로 두고 코드 구조를 개선
- ③ 모든 코드 삭제 후 재작성
- ④ 테스트 생략

**Q3.** 코드 안에 설명 없이 쓰인 숫자 `5`, `400`을 무엇이라 하는가?

- ① 상수
- ② 매직 넘버
- ③ 인덱스
- ④ 반환값

**Q4.** 리팩터링 후 반드시 해야 할 일은?

- ① 발표
- ② 회귀 테스트
- ③ 파일 삭제
- ④ 주석 삭제

**Q5.** '차트 작성' 평가에서 확인하는 핵심은?

- ① 색깔이 예쁜가
- ② 산출물(코드)과 차트 내용이 일치하는가
- ③ 차트가 몇 장인가
- ④ 손으로 그렸는가

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 버그 고치기: 승자 판정 (기본)

아래 코드는 승리 점수 W에 '도달'하면 승리여야 하는데, 버그가 있습니다. 버그를 고쳐 `왼쪽`, `오른쪽`, `없음` 중 하나를 출력하세요. 입력은 한 줄에 `왼쪽점수 오른쪽점수 W`입니다.

```python
left, right, W = map(int, input().split())
if left > W:
    print("왼쪽")
elif right > W:
    print("오른쪽")
else:
    print("없음")
```

- 입력: left right W
- 출력: 승자

예제 입력 1

```text
5 3 5
```

예제 출력 1

```text
왼쪽
```

예제 입력 2

```text
2 5 5
```

예제 출력 2

```text
오른쪽
```

예제 입력 3

```text
4 4 5
```

예제 출력 3

```text
없음
```

### 문제 2. 중복 코드 함수로 묶기 (도전)

학생 세 명의 '이름 점수1 점수2 점수3'이 한 줄씩 주어집니다. 평균(소수 첫째 자리)과 등급(평균 90 이상 A, 80 이상 B, 70 이상 C, 그 외 D)을 `이름 평균 등급` 형식으로 출력하세요. 등급 계산은 `grade(avg)` 함수 하나로 만들어 중복을 없애세요.

- 입력: 세 줄의 이름과 점수
- 출력: 각 학생의 이름 평균 등급

예제 입력 1

```text
kim 90 95 100
lee 70 80 85
park 60 65 70
```

예제 출력 1

```text
kim 95.0 A
lee 78.3 C
park 65.0 D
```

정답과 해설은 **[부록] 06-1-21. 21차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-21-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 버그 리포트: 상황·행동·기대·실제 (재현 가능하게)
- 리팩터링: 중복→함수, 매직 넘버→상수, 의미 있는 이름, '왜' 주석
- 리팩터링 후 회귀 테스트
- 차트는 완성 코드와 일치해야 한다

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `11_updown_safe.py` | [11_updown_safe.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/11_updown_safe.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/11_updown_safe.py) |
| 학습용 PPT | [21-project-test-chart.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/21-project-test-chart.pptx) |
| 학생 활동지 | [ws21-project-test-chart.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws21-project-test-chart.md) |
| 코딩 테스트 1 정답 코드 | [ch21_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch21_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch21_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch21_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch21_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch21_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
