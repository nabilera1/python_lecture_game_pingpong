"""11차시 코딩 테스트 2: 행맨 한 판 시뮬레이션 (도전) - 정답 예시 코드

첫째 줄에 단어, 둘째 줄에 순서대로 말한 글자들이 공백으로 주어집니다. 목숨은 6개이며, 단어에 없는 글자를 말하면 1 줄어듭니다. 단어를 완성하면 `성공 ○`(남은 목숨), 목숨이 0이 되면 `실패`를 출력하고 그 즉시 끝냅니다. 글자를 다 말해도 끝나지 않으면 `진행 중 ○`(남은 목숨)을 출력하세요.
"""

word = input()
letters = input().split()
guessed = []
lives = 6
result = None
for ch in letters:
    guessed.append(ch)
    if ch not in word:
        lives -= 1
    if lives == 0:
        result = "실패"
        break
    if all(c in guessed for c in word):
        result = f"성공 {lives}"
        break
print(result if result else f"진행 중 {lives}")
