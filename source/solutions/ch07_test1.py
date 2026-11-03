"""7차시 코딩 테스트 1: 기억력 정답 확인 (기본) - 정답 예시 코드

첫째 줄에 보여 준 숫자열, 둘째 줄에 플레이어 입력이 주어집니다. 공백을 모두 무시하고 같으면 `정답`, 다르면 `오답`을 출력하세요.
"""

shown = input().replace(" ", "")
typed = input().replace(" ", "")
print("정답" if shown == typed else "오답")
