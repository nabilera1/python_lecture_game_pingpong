"""3차시 코딩 테스트 1: 업다운 한 번 판정 (기본) - 정답 예시 코드

정답 secret과 추측 guess를 입력받아 같으면 `정답`, guess가 작으면 `UP`, 크면 `DOWN`을 출력하세요.
"""

secret = int(input())
guess = int(input())
if guess == secret:
    print("정답")
elif guess < secret:
    print("UP")
else:
    print("DOWN")
