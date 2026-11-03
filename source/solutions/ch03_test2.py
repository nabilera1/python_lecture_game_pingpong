"""3차시 코딩 테스트 2: 가위바위보 한 판 판정 (도전) - 정답 예시 코드

나와 컴퓨터의 선택(가위/바위/보)을 한 줄에 입력받아 나를 기준으로 `이김`, `짐`, `비김`을 출력하세요.
"""

choices = ["가위", "바위", "보"]
me, cpu = input().split()
diff = (choices.index(me) - choices.index(cpu)) % 3
if diff == 0:
    print("비김")
elif diff == 1:
    print("이김")
else:
    print("짐")
