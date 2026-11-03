> 19차시 **나만의 게임 프로젝트 기획과 설계**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 프로젝트 계획서에 '테스트 계획'을 미리 쓰는 이유로 가장 알맞은 것은?

- ① 분량을 늘리려고
- ② 완성 기준을 미리 정해 구현 방향을 잡으려고
- ③ 선생님이 시켜서
- ④ 코드를 짧게 하려고

> **정답: ② 완성 기준을 미리 정해 구현 방향을 잡으려고**  
> 무엇이 '완성'인지 기준이 있어야 구현과 평가가 명확해집니다.

**Q2.** 기능 목록에서 우선순위를 정하는 가장 큰 이유는?

- ① 멋있어 보여서
- ② 주어진 시간 안에 꼭 필요한 기능부터 완성하려고
- ③ 코드를 길게 하려고
- ④ 모두 동시에 하려고

> **정답: ② 주어진 시간 안에 꼭 필요한 기능부터 완성하려고**  
> 시간이 부족할 때도 핵심 기능은 완성되도록 합니다.

**Q3.** '준비 → 진행 → 종료'처럼 게임의 흐름을 나타내는 설계 방법은?

- ① 상태 다이어그램
- ② 판정표
- ③ 추적표
- ④ IPO 표

> **정답: ① 상태 다이어그램**  
> 상태(state)와 상태 사이의 전환을 그림으로 나타냅니다.

**Q4.** `LEVELS = {"쉬움": {"speed": 4}}`에서 4를 꺼내는 코드는?

- ① LEVELS["speed"]
- ② LEVELS["쉬움"]["speed"]
- ③ LEVELS[0][0]
- ④ LEVELS.speed

> **정답: ② LEVELS["쉬움"]["speed"]**  
> 바깥 키로 안쪽 딕셔너리를 꺼낸 뒤 안쪽 키로 값을 꺼냅니다.

**Q5.** 클래스 구조도에 반드시 들어가야 하는 것은?

- ① 실행 화면 사진
- ② 속성과 메서드
- ③ 글꼴 이름
- ④ 파일 크기

> **정답: ② 속성과 메서드**  
> 클래스가 가진 정보(속성)와 할 수 있는 일(메서드)을 나타냅니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ① | ② | ② |

## 코딩 테스트 1. 난이도 설정 불러오기

```python
LEVELS = {"쉬움": [4, 3], "보통": [6, 5], "어려움": [8, 7]}
name = input().strip()
if name not in LEVELS:
    print("알 수 없는 난이도: 보통으로 설정")
    name = "보통"
ball_speed, ai_speed = LEVELS[name]
print(f"공 속도 {ball_speed}, AI 속도 {ai_speed}")
```

**해설** 설정을 딕셔너리로 묶으면 난이도를 추가할 때 데이터 한 줄만 늘리면 됩니다. 없는 키를 미리 검사해 KeyError를 막았습니다.

정답 코드 파일: [ch19_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch19_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch19_test1.py)

## 코딩 테스트 2. 게임 상태 전환기

```python
RULES = {
    ("준비", "S"): "진행",
    ("진행", "P"): "일시정지",
    ("일시정지", "P"): "진행",
    ("진행", "W"): "종료",
    ("종료", "R"): "준비",
}
state = "준비"
for cmd in input().strip():
    if (state, cmd) in RULES:
        state = RULES[(state, cmd)]
        print(state)
```

**해설** (현재 상태, 명령) 튜플을 키로 하는 딕셔너리로 상태 전환표를 만들었습니다. if 문을 잔뜩 쓰는 대신 **규칙을 데이터로** 적는 9차시의 아이디어를 다시 사용했습니다.

정답 코드 파일: [ch19_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch19_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch19_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
