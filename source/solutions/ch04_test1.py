"""4차시 코딩 테스트 1: 1부터 n까지의 합 (기본) - 정답 예시 코드

정수 n을 입력받아 while 문으로 1부터 n까지의 합을 구해 출력하세요.
"""

n = int(input())
i, total = 1, 0
while i <= n:
    total += i
    i += 1
print(total)
