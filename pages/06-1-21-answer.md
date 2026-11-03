> 21차시 **프로젝트 테스트·리팩터링과 차트 작성**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 좋은 버그 리포트의 가장 중요한 조건은?

- ① 길게 쓰기
- ② 누구나 같은 문제를 재현할 수 있게 쓰기
- ③ 범인을 밝히기
- ④ 코드를 함께 붙이기

> **정답: ② 누구나 같은 문제를 재현할 수 있게 쓰기**  
> 재현할 수 있어야 원인을 찾고 고친 뒤 확인할 수 있습니다.

**Q2.** 리팩터링의 뜻으로 알맞은 것은?

- ① 새 기능 추가
- ② 동작은 그대로 두고 코드 구조를 개선
- ③ 모든 코드 삭제 후 재작성
- ④ 테스트 생략

> **정답: ② 동작은 그대로 두고 코드 구조를 개선**  
> 겉으로 보이는 동작을 바꾸지 않고 내부 구조를 개선합니다.

**Q3.** 코드 안에 설명 없이 쓰인 숫자 `5`, `400`을 무엇이라 하는가?

- ① 상수
- ② 매직 넘버
- ③ 인덱스
- ④ 반환값

> **정답: ② 매직 넘버**  
> 의미를 알기 어려운 숫자를 매직 넘버라 하며, 이름 있는 상수로 바꾸는 것이 좋습니다.

**Q4.** 리팩터링 후 반드시 해야 할 일은?

- ① 발표
- ② 회귀 테스트
- ③ 파일 삭제
- ④ 주석 삭제

> **정답: ② 회귀 테스트**  
> 구조를 바꾸다 기능이 망가지지 않았는지 확인해야 합니다.

**Q5.** '차트 작성' 평가에서 확인하는 핵심은?

- ① 색깔이 예쁜가
- ② 산출물(코드)과 차트 내용이 일치하는가
- ③ 차트가 몇 장인가
- ④ 손으로 그렸는가

> **정답: ② 산출물(코드)과 차트 내용이 일치하는가**  
> 차트가 실제 프로그램을 정확히 설명해야 합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. 버그 고치기: 승자 판정

```python
left, right, W = map(int, input().split())
if left >= W:
    print("왼쪽")
elif right >= W:
    print("오른쪽")
else:
    print("없음")
```

**해설** `>`는 W점을 '넘어야' 승리이므로 5점이 되어도 승리하지 않는 **경계값 논리 오류**입니다. 경계값(정확히 5점) 테스트 케이스가 있었다면 바로 발견했을 것입니다.

정답 코드 파일: [ch21_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch21_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch21_test1.py)

## 코딩 테스트 2. 중복 코드 함수로 묶기

```python
def grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    return "D"

for _ in range(3):
    name, *scores = input().split()
    avg = sum(map(int, scores)) / len(scores)
    print(f"{name} {avg:.1f} {grade(avg)}")
```

**해설** `name, *scores = ...`는 첫 값은 name에, 나머지는 리스트 scores에 담습니다. 세 학생에게 같은 등급 코드를 복사해 붙이는 대신 함수 하나를 세 번 호출합니다.

정답 코드 파일: [ch21_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch21_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch21_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
