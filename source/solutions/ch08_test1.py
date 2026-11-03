"""8차시 코딩 테스트 1: judge 함수 만들기 (기본) - 정답 예시 코드

`judge(guess, secret)` 함수를 만들어 정답이면 `correct`, guess가 작으면 `up`, 크면 `down`을 반환하게 하세요. 첫째 줄에 정답, 둘째 줄에 n, 다음 n줄의 추측마다 judge 결과를 출력합니다.
"""

def judge(guess, secret):
    if guess == secret:
        return "correct"
    return "up" if guess < secret else "down"

secret = int(input())
n = int(input())
for _ in range(n):
    print(judge(int(input()), secret))
