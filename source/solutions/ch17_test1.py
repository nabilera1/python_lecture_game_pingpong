"""17차시 코딩 테스트 1: 득점 기록으로 승자 정하기 (기본) - 정답 예시 코드

첫째 줄에 승리 점수 W, 둘째 줄에 득점 기록(`L` 왼쪽 득점, `R` 오른쪽 득점) 문자열이 주어집니다. 누군가 W점에 도달하면 그 즉시 기록 읽기를 멈추고 `왼쪽 승리` 또는 `오른쪽 승리`와 최종 점수 `○ : ○`를 출력하세요. 끝까지 승자가 없으면 `진행 중`과 점수를 출력하세요.
"""

def winner(left, right, win_score):
    if left >= win_score:
        return "left"
    if right >= win_score:
        return "right"
    return None

W = int(input())
left = right = 0
for ch in input().strip():
    if winner(left, right, W):     # 이미 승자가 있으면 더 이상 득점하지 않음
        break
    if ch == "L":
        left += 1
    else:
        right += 1
result = winner(left, right, W)
if result == "left":
    print("왼쪽 승리")
elif result == "right":
    print("오른쪽 승리")
else:
    print("진행 중")
print(f"{left} : {right}")
