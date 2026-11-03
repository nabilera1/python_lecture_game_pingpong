"""6차시 코딩 테스트 1: 스트라이크·볼 계산기 (기본) - 정답 예시 코드

정답 세 자리와 추측 세 자리가 한 줄에 공백으로 주어집니다. 결과를 `○S ○B` 형식으로 출력하세요. (각 수의 숫자는 서로 다르다.)
"""

answer, guess = input().split()
strike = ball = 0
for i in range(3):
    if guess[i] == answer[i]:
        strike += 1
    elif guess[i] in answer:
        ball += 1
print(f"{strike}S {ball}B")
