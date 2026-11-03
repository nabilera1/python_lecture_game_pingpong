"""5차시 코딩 테스트 2: 가위바위보 전적 계산 (도전) - 정답 예시 코드

첫째 줄에 판 수 n, 다음 n줄에 `나 컴퓨터`의 선택이 주어집니다. 나의 승, 패, 무 횟수를 `○승 ○패 ○무` 형식으로 출력하세요.
"""

choices = ["가위", "바위", "보"]
n = int(input())
result = [0, 0, 0]              # [무, 승, 패] 개수 : 인덱스가 곧 diff 값
for _ in range(n):
    me, cpu = input().split()
    diff = (choices.index(me) - choices.index(cpu)) % 3
    result[diff] += 1
print(f"{result[1]}승 {result[2]}패 {result[0]}무")
