"""4차시 코딩 테스트 2: 업다운 기록 판정기 (도전) - 정답 예시 코드

첫째 줄에 정답, 둘째 줄에 시도 횟수 n, 다음 n줄에 추측한 수가 주어집니다. 각 추측마다 `UP`, `DOWN`을 출력하고, 맞히면 `정답! k번 만에 성공`을 출력한 뒤 끝냅니다. 끝까지 못 맞히면 `실패! 정답은 ○`를 출력하세요.
"""

secret = int(input())
n = int(input())
count = 0
while count < n:
    guess = int(input())
    count += 1
    if guess == secret:
        print(f"정답! {count}번 만에 성공")
        break
    elif guess < secret:
        print("UP")
    else:
        print("DOWN")
else:
    print(f"실패! 정답은 {secret}")
