"""18차시 코딩 테스트 1: parse_guess 구현 (기본) - 정답 예시 코드

`parse_guess(text, low, high)` 함수를 만드세요. 앞뒤 공백을 제거한 text가 숫자로만 되어 있고 low 이상 high 이하이면 그 정수를, 아니면 `None`을 반환합니다. 첫째 줄에 low high, 둘째 줄에 n, 다음 n줄 각각에 대한 반환값을 출력하세요.
"""

def parse_guess(text, low, high):
    text = text.strip()
    if not text.isdigit():
        return None
    number = int(text)
    if not (low <= number <= high):
        return None
    return number

low, high = map(int, input().split())
for _ in range(int(input())):
    print(parse_guess(input(), low, high))
