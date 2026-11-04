> 13차시 **클래스와 객체: 붕어빵 틀로 게임 요소 만들기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 클래스로부터 만들어진 실체를 무엇이라 하는가?

- ① 모듈
- ② 객체(인스턴스)
- ③ 매개변수
- ④ 상수

> **정답: ② 객체(인스턴스)**  
> 클래스는 설계도, 객체는 설계도로 만든 실물입니다.

**Q2.** 객체를 만들 때 자동으로 실행되는 메서드는?

- ① __main__
- ② __init__
- ③ start
- ④ self

> **정답: ② __init__**  
> `__init__`은 객체 생성 시 자동 호출되는 초기화 메서드입니다.

**Q3.** `a = Player("A")`, `b = Player("B")` 후 `a.damage(5)`를 실행하면?

- ① a와 b의 hp가 모두 줄어든다
- ② a의 hp만 줄어든다
- ③ b의 hp만 줄어든다
- ④ 오류

> **정답: ② a의 hp만 줄어든다**  
> self.hp는 객체마다 따로 저장됩니다.

**Q4.** `self`에 대한 설명으로 옳은 것은?

- ① 클래스 이름이다
- ② 메서드를 호출한 그 객체를 가리킨다
- ③ 전역 변수이다
- ④ 생략하면 자동으로 붙는다

> **정답: ② 메서드를 호출한 그 객체를 가리킨다**  
> 메서드 정의의 첫 매개변수 self는 호출한 객체 자신입니다.

**Q5.** `constants.py`에 설정값을 모아 두는 가장 큰 이유는?

- ① 실행 속도가 빨라진다
- ② 한 곳만 고치면 게임 전체에 적용된다
- ③ 오류가 나지 않는다
- ④ pygame이 요구한다

> **정답: ② 한 곳만 고치면 게임 전체에 적용된다**  
> 여러 파일에서 쓰는 값을 한곳에서 관리하면 수정과 실험이 쉬워집니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. Player 클래스 명령 처리

```python
class Player:
    def __init__(self, hp=30):
        self.hp = hp

    def damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def heal(self, amount):
        self.hp = min(30, self.hp + amount)

p = Player()
for _ in range(int(input())):
    cmd, value = input().split()
    if cmd == "damage":
        p.damage(int(value))
    else:
        p.heal(int(value))
print(p.hp)
if p.hp == 0:
    print("GAME OVER")
```

**해설** `max(0, ...)`, `min(30, ...)`로 범위를 넘지 않게 막는 것을 **클램프**(clamp)라고 합니다. 패들이 화면 밖으로 못 나가게 하는 원리와 같습니다.

정답 코드 파일: [ch13_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch13_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch13_test1.py)

## 코딩 테스트 2. 두 객체를 따로 관리하기

```python
class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

names = input().split()
teams = {name: Team(name) for name in names}    # 이름 → Team 객체
for who in input().split():
    teams[who].add_point()
a, b = teams[names[0]], teams[names[1]]
print(a.name, a.score)
print(b.name, b.score)
if a.score == b.score:
    print("무승부")
else:
    print(a.name if a.score > b.score else b.name)
```

**해설** 딕셔너리의 값으로 객체를 저장하면 이름으로 객체를 찾아 메서드를 부를 수 있습니다. 같은 클래스의 두 객체가 점수를 **각자** 기억한다는 것이 핵심입니다.

정답 코드 파일: [ch13_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch13_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch13_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
