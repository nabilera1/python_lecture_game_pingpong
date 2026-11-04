> **5부 테스트·프로젝트·공유** · 20차시 · 6단계 모형: **공유·확장**  
> 게임: 확장 예제: 공 가속 · AI 패들 · 최고 기록 저장  
> 핵심 개념: 점진적 구현, 버전 관리, 상속 맛보기, 파일 입출력, with open, 주석, AI 활용 기록

## 학습 목표

1. 계획서와 설계 차트에 따라 프로그램을 단계적으로 구현할 수 있다.
2. 기존 클래스와 함수를 수정·확장하여 새 기능을 추가할 수 있다.
3. 파일 입출력으로 게임 기록을 저장하고 불러올 수 있다.

## 핵심 질문

> **설계한 대로 만들려면 어떤 순서로, 얼마나 작게 나누어 구현해야 할까?**

한 번에 모든 기능을 만들려고 하면 어디서 문제가 생겼는지 찾기 어렵습니다. **작은 기능 하나 → 실행 → 확인**을 반복하는 **점진적 구현**이 핵심입니다. 오늘은 자주 쓰이는 확장 기능 3가지를 예제로 보고, 각 모둠의 계획서대로 구현합니다.

## 구현 순서 잡기

1. **원본 백업**: 작업 전 파일을 복사해 `game_v1.py`처럼 버전을 남깁니다. (깃허브를 쓰면 커밋으로 관리)
2. **꼭 필요한 기능(必)부터** 하나씩 구현하고 바로 실행해 봅니다.
3. 기능 하나가 끝날 때마다 **주석**을 달고, 활동지 테스트 계획의 케이스를 실행합니다.
4. AI의 도움을 받았다면 **AI 활용 기록표**에 적고, 코드를 **내가 설명할 수 있는지** 확인합니다.

## 확장 예제 1: 공 가속

```python
MAX_SPEED = 12

def bounce_paddle(self, paddle):
    if self.rect.colliderect(paddle.rect):
        # 방향은 반대로, 크기는 1.1배 (단, 최대 속도 제한)
        speed = min(abs(self.vx) * 1.1, MAX_SPEED)
        self.vx = speed if self.vx < 0 else -speed
        ...
```

`abs()`는 절댓값입니다. **방향**(부호)과 **크기**(속력)를 따로 생각하면 코드가 명확해집니다.

## 확장 예제 2: AI 패들 (상속 맛보기)

```python
class AIPaddle(Paddle):                  # Paddle 의 기능을 물려받는다 (상속)
    def follow(self, ball):
        if ball.rect.centery < self.rect.centery - 10:
            self.rect.y -= self.speed
        elif ball.rect.centery > self.rect.centery + 10:
            self.rect.y += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
```

`class AIPaddle(Paddle):`처럼 쓰면 `Paddle`의 `__init__`, `draw`를 그대로 쓰면서 `follow`만 새로 추가할 수 있습니다. `±10`의 여유(데드존)가 없으면 패들이 공 근처에서 덜덜 떨립니다. `self.speed`를 공 속도보다 작게 하면 사람이 이길 수 있는 AI가 됩니다.

## 확장 예제 3: 최고 기록 파일 저장

```python
def load_best(path="best.txt"):
    try:
        with open(path, encoding="utf-8") as f:   # 파일 열기 (자동으로 닫힘)
            return int(f.read())
    except (FileNotFoundError, ValueError):       # 파일이 없거나 내용이 이상하면
        return 0

def save_best(score, path="best.txt"):
    with open(path, "w", encoding="utf-8") as f:  # "w": 쓰기 (덮어쓰기)
        f.write(str(score))
```

프로그램을 껐다 켜도 기록이 남으려면 **파일**에 저장해야 합니다. 변수는 프로그램이 끝나면 사라집니다.

## 실습 활동

1. 계획서의 '꼭 필요한 기능'을 순서대로 구현하고, 기능마다 실행 결과를 확인하세요.
2. 확장 예제 중 하나를 우리 게임에 적용해 보세요.
3. 구현하며 바뀐 설계가 있다면 차트(순서도·구조도)도 함께 고쳐 두세요.

활동지: [ws20-project-build.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws20-project-build.md)

## 확인 퀴즈

**Q1.** 점진적 구현에 대한 설명으로 옳은 것은?

- ① 모든 기능을 한 번에 작성 후 실행
- ② 작은 기능 하나씩 구현하고 바로 확인
- ③ 테스트는 마지막에 한 번만
- ④ 주석은 쓰지 않는다

**Q2.** `class AIPaddle(Paddle):`의 의미는?

- ① Paddle을 삭제한다
- ② Paddle의 기능을 물려받은 새 클래스
- ③ Paddle 객체를 만든다
- ④ 함수 호출

**Q3.** `abs(-7.5)`의 값은?

- ① -7.5
- ② 7.5
- ③ 7
- ④ -7

**Q4.** `with open("best.txt", "w") as f:`에서 "w"의 뜻은?

- ① 읽기
- ② 쓰기(덮어쓰기)
- ③ 이어 쓰기
- ④ 삭제

**Q5.** 프로그램을 다시 실행해도 최고 기록이 남아 있게 하려면?

- ① 전역 변수에 저장
- ② 리스트에 저장
- ③ 파일에 저장
- ④ print로 출력

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 공 가속 시뮬레이션 (기본)

처음 속력 v, 배율 r, 최대 속력 m, 패들 충돌 횟수 n이 주어집니다. 충돌할 때마다 속력에 r을 곱하되 m을 넘지 않게 합니다. 각 충돌 후 속력을 소수 둘째 자리까지 공백으로 구분해 출력하세요.

- 입력: v r m n
- 출력: n개의 속력

예제 입력 1

```text
6 1.1 8 4
```

예제 출력 1

```text
6.60 7.26 7.99 8.00
```

예제 입력 2

```text
5 1.5 20 3
```

예제 출력 2

```text
7.50 11.25 16.88
```

### 문제 2. 최고 기록 갱신 기록 (도전)

첫째 줄에 저장되어 있던 최고 기록 best(없으면 0), 둘째 줄에 이번에 플레이한 점수들이 공백으로 주어집니다. 각 판이 끝날 때마다 최고 기록을 공백으로 구분해 출력하고, 마지막 줄에 기록이 갱신된 횟수를 `갱신 ○회`로 출력하세요.

- 입력: best, 점수들
- 출력: 판마다의 최고 기록, 갱신 횟수

예제 입력 1

```text
50
30 70 60 90
```

예제 출력 1

```text
50 70 70 90
갱신 2회
```

예제 입력 2

```text
0
5 5 3
```

예제 출력 2

```text
5 5 5
갱신 1회
```

정답과 해설은 **[부록] 06-1-20. 20차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/pages/06-1-20-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 작게 만들고 바로 실행하는 점진적 구현
- 공 가속: 방향(부호)과 크기(abs) 분리, 최대 속도 제한
- AI 패들: 상속 + 데드존 + clamp
- 파일 입출력: with open, 'r'/'w', 예외 처리

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `ball.py` | [ball.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/ball.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/ball.py) |
| 소스코드 `paddle.py` | [paddle.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/pingpong/paddle.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/pingpong/paddle.py) |
| 소스코드 `05_updown_func.py` | [05_updown_func.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/text_games/05_updown_func.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/text_games/05_updown_func.py) |
| 학습용 PPT | [20-project-build.pptx 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/raw/main/slides/20-project-build.pptx) |
| 학생 활동지 | [ws20-project-build.md](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/worksheets/ws20-project-build.md) |
| 코딩 테스트 1 정답 코드 | [ch20_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch20_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch20_test1.py) |
| 코딩 테스트 2 정답 코드 | [ch20_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch20_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch20_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/python_lecture_game_pingpong/archive/refs/heads/main.zip) |
