"""11차시 코딩 테스트 1: 행맨 보드 출력 (기본) - 정답 예시 코드

첫째 줄에 단어, 둘째 줄에 지금까지 말한 글자들이 공백으로 주어집니다. 맞힌 글자는 그대로, 아닌 글자는 `_`로 바꿔 공백으로 구분해 출력하세요. 둘째 줄이 빈 줄이면 아무 글자도 말하지 않은 것입니다.
"""

word = input()
guessed = input().split()
print(" ".join(ch if ch in guessed else "_" for ch in word))
