"""15차시 코딩 테스트 1: clamp 함수 (기본) - 정답 예시 코드

`clamp(value, low, high)` 함수를 만드세요. value가 low보다 작으면 low, high보다 크면 high, 아니면 value를 돌려줍니다. 첫째 줄에 low high, 둘째 줄에 값들이 공백으로 주어질 때 각 결과를 공백으로 구분해 출력하세요.
"""

def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

low, high = map(int, input().split())
values = map(int, input().split())
print(*[clamp(v, low, high) for v in values])
