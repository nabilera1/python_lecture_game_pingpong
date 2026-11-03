"""20차시 코딩 테스트 1: 공 가속 시뮬레이션 (기본) - 정답 예시 코드

처음 속력 v, 배율 r, 최대 속력 m, 패들 충돌 횟수 n이 주어집니다. 충돌할 때마다 속력에 r을 곱하되 m을 넘지 않게 합니다. 각 충돌 후 속력을 소수 둘째 자리까지 공백으로 구분해 출력하세요.
"""

v, r, m, n = input().split()
v, r, m, n = float(v), float(r), float(m), int(n)
speeds = []
for _ in range(n):
    v = min(v * r, m)
    speeds.append(f"{v:.2f}")
print(" ".join(speeds))
