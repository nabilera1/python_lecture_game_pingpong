"""2차시 코딩 테스트 1: 두 수의 사칙연산 (기본) - 정답 예시 코드

두 정수 a, b를 한 줄에 입력받아 합, 차, 몫, 나머지를 한 줄에 하나씩 출력하세요. (b는 0이 아니다.)
"""

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a // b)
print(a % b)
