"""16차시 코딩 테스트 2: 사각형 충돌 판정 (도전) - 정답 예시 코드

각 줄에 두 사각형 `x1 y1 w1 h1 x2 y2 w2 h2`가 주어집니다. 첫째 줄의 n개 테스트마다 두 사각형이 겹치면 `충돌`, 아니면 `통과`를 출력하세요. 변이 딱 맞닿기만 한 경우는 겹치지 않은 것으로 봅니다.
"""

def overlap(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah

for _ in range(int(input())):
    v = list(map(int, input().split()))
    print("충돌" if overlap(v[:4], v[4:]) else "통과")
