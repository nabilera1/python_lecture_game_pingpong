> 9차시 **딕셔너리: 규칙을 데이터로 표현하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `d = {"a": 1, "b": 2}`일 때 `d["b"]`는?

- ① 1
- ② 2
- ③ "b"
- ④ 오류

> **정답: ② 2**  
> 키 "b"에 연결된 값은 2입니다.

**Q2.** 딕셔너리에 없는 키를 `d["z"]`로 읽으면?

- ① None
- ② 0
- ③ KeyError 오류
- ④ 빈 문자열

> **정답: ③ KeyError 오류**  
> 없는 키를 대괄호로 읽으면 KeyError가 납니다. `d.get("z", 기본값)`을 쓰면 안전합니다.

**Q3.** `BEATS = {"가위": "보", ...}`에서 `BEATS["가위"] == "보"`가 뜻하는 것은?

- ① 가위가 보에게 진다
- ② 가위가 보를 이긴다
- ③ 비긴다
- ④ 알 수 없다

> **정답: ② 가위가 보를 이긴다**  
> 이기는 쪽: 지는 쪽 형태로 규칙을 저장했습니다.

**Q4.** `score = {"win": 1, "lose": 2}`일 때 `max(score.values())`는?

- ① win
- ② lose
- ③ 1
- ④ 2

> **정답: ④ 2**  
> values()는 값들만 모으므로 최댓값 2입니다.

**Q5.** 딕셔너리의 (키, 값) 쌍을 함께 반복하는 메서드는?

- ① keys()
- ② values()
- ③ items()
- ④ pairs()

> **정답: ③ items()**  
> `for k, v in d.items():` 형태로 씁니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ③ | ② | ④ | ③ |

## 코딩 테스트 1. 선택 횟수 세기

```python
count = {"가위": 0, "바위": 0, "보": 0}
for pick in input().split():
    count[pick] += 1
for name, value in count.items():
    print(name, value)
```

**해설** 딕셔너리는 넣은 순서를 기억하므로 처음 만든 순서(가위, 바위, 보)대로 출력됩니다.

정답 코드 파일: [ch09_test1.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch09_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch09_test1.py)

## 코딩 테스트 2. 딕셔너리 판정으로 먼저 2승

```python
BEATS = {"가위": "보", "바위": "가위", "보": "바위"}
n = int(input())
score = {"win": 0, "lose": 0}
for _ in range(n):
    me, cpu = input().split()
    if me != cpu:
        score["win" if BEATS[me] == cpu else "lose"] += 1
    if max(score.values()) == 2:
        break
if score["win"] == 2:
    print("승리")
elif score["lose"] == 2:
    print("패배")
else:
    print("미정")
print(f"나 {score['win']} : {score['lose']} 컴퓨터")
```

**해설** 조건 표현식으로 고른 문자열("win"/"lose")을 바로 키로 사용했습니다. 2승이 나오면 break로 남은 입력을 읽지 않습니다.

정답 코드 파일: [ch09_test2.py 보기](https://github.com/nabilera1/python_lecture_game_pingpong/blob/main/source/solutions/ch09_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/python_lecture_game_pingpong/main/source/solutions/ch09_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
