"""15차시 코딩 테스트 2: 패들 이동 기록 (도전) - 정답 예시 코드

화면 높이 H, 패들 높이 PH, 속도 S, 처음 top 좌표 Y가 첫째 줄에 주어지고, 둘째 줄에 프레임마다 눌린 키가 문자열로 주어집니다. (`U` 위, `D` 아래, `N` 없음, `B` 위아래 동시) 각 프레임 후 top 좌표를 공백으로 구분해 출력하세요. top은 0 이상 H-PH 이하로 제한됩니다.
"""

H, PH, S, Y = map(int, input().split())
top = Y
result = []
for key in input().strip():
    if key in "UB":
        top -= S
    if key in "DB":
        top += S
    top = max(0, min(top, H - PH))
    result.append(top)
print(*result)
