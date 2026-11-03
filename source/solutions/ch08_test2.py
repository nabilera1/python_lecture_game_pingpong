"""8차시 코딩 테스트 2: 입력 검사 함수 (도전) - 정답 예시 코드

`is_valid(text, low, high)` 함수를 만드세요. text가 숫자로만 되어 있고 low 이상 high 이하이면 True, 아니면 False를 반환합니다. 첫째 줄에 low high, 둘째 줄에 n, 다음 n줄의 문자열마다 결과를 출력하세요.
"""

def is_valid(text, low, high):
    if not text.isdigit():
        return False
    return low <= int(text) <= high

low, high = map(int, input().split())
n = int(input())
for _ in range(n):
    print(is_valid(input(), low, high))
