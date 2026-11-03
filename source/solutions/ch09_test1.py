"""9차시 코딩 테스트 1: 선택 횟수 세기 (기본) - 정답 예시 코드

한 줄에 여러 개의 선택(가위/바위/보)이 공백으로 주어집니다. 가위, 바위, 보 순서로 각각 몇 번 나왔는지 출력하세요.
"""

count = {"가위": 0, "바위": 0, "보": 0}
for pick in input().split():
    count[pick] += 1
for name, value in count.items():
    print(name, value)
