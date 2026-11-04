"""9차시 코딩 테스트 2: 딕셔너리 판정으로 먼저 2승 (도전) - 정답 예시 코드

`BEATS` 딕셔너리로 판정하세요. 첫째 줄에 최대 판 수 n, 다음 줄부터 최대 n줄에 `나 컴퓨터`의 선택이 한 줄씩 주어집니다. 누군가 먼저 2승을 하면 즉시 멈추고 `승리` 또는 `패배`와 `나 ○ : ○ 컴퓨터`를 출력합니다. n판이 끝날 때까지 2승이 없으면 `미정`과 점수를 출력하세요.
"""

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
