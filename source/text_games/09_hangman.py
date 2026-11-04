"""영단어 행맨 (난이도 중) - 11차시: 딕셔너리, 리스트, 함수, 제너레이터 표현식, all()

실행 방법: python 09_hangman.py
"""

# =====================================================================
# 게임 규칙
#   컴퓨터가 영단어 하나를 고르고, 뜻(힌트)과 글자 수만 알려 줘요.
#   알파벳을 하나씩 말해서 단어를 완성하면 성공!
#   단어에 없는 글자를 말할 때마다 목숨(♥)이 1개씩 줄어요. 6개를 다 잃으면 실패.
#
# 배운 내용 총정리 (종합 차시)
#   딕셔너리 WORDS  : {영단어: 뜻}
#   리스트 guessed  : 지금까지 말한 글자들
#   함수 show / ask_letter / play : 화면 출력 / 입력 검사 / 한 판 진행
#   all(...)        : 괄호 안의 조건이 "모두" 참이면 True → 모든 글자를 맞혔는지 확인
# =====================================================================

import random

WORDS = {"computer": "컴퓨터", "algorithm": "알고리즘", "variable": "변수",
         "python": "파이썬", "internet": "인터넷", "function": "함수"}   # 영단어: 뜻(힌트)


def show(word, guessed, lives):
    """현재 상태(맞힌 글자, 목숨, 사용한 글자)를 보여 준다"""
    # 단어의 각 글자 ch 에 대해: 맞힌 글자면 그대로, 아니면 "_" → 공백으로 이어 붙임
    # 예) word="python", guessed=['p','o'] → "p _ _ _ o _"
    board = " ".join(ch if ch in guessed else "_" for ch in word)
    # 문자열 * 정수 → 반복. '♥' * 4 → '♥♥♥♥'
    # ♥(검은 하트)·♡(흰 하트) 입력 방법
    #   - 윈도우: 한글 입력 상태에서 ㅁ 을 치고 [한자] 키 → Tab 으로 목록 펼치기 → ♥, ♡ 선택
    #   - 맥: Control + Command + Space → 문자 뷰어에서 '하트' 검색
    #   - 어디서나: 유니코드로 '\u2665'(♥), '\u2661'(♡) 라고 써도 똑같이 출력돼요.
    print(f"\n{board}   목숨: {'♥' * lives}{'♡' * (6 - lives)}   사용: {' '.join(guessed)}")


def ask_letter(guessed):
    """알파벳 한 글자이고, 아직 쓰지 않은 글자일 때만 돌려준다"""
    while True:
        ch = input("알파벳 한 글자 > ").lower()       # 대문자로 입력해도 소문자로 통일
        # 세 가지 중 하나라도 해당하면(or) 다시 입력: 길이가 1이 아님 / 영어 알파벳이 아님 / 이미 씀
        # isalpha()는 한글('ㅁ')도 True 라서 isascii()와 함께 검사해야 영어 알파벳만 받아요.
        #   (한글 자판 상태에서 a 를 누르면 'ㅁ'이 입력돼요!)
        if len(ch) != 1 or not (ch.isascii() and ch.isalpha()) or ch in guessed:
            print("알파벳 한 글자만, 이미 쓴 글자는 안 돼요!")
        else:
            return ch


def play():
    """한 판을 진행하고 성공하면 True, 실패하면 False 를 돌려준다"""
    word = random.choice(list(WORDS))          # list(딕셔너리) → 키 목록. 그중 무작위 선택
    guessed, lives = [], 6
    print(f"\n힌트(뜻): {WORDS[word]}  /  글자 수: {len(word)}")
    while lives > 0:
        show(word, guessed, lives)
        if all(ch in guessed for ch in word):  # 단어의 모든 글자가 guessed 안에 있으면 성공
            print("성공! 정답:", word)
            return True
        ch = ask_letter(guessed)
        guessed.append(ch)
        if ch not in word:                     # 문자열에도 in 을 쓸 수 있어요: 'y' in 'python' → True
            lives -= 1
    print("실패... 정답은", word)
    return False


# 프로그램 시작 ----------------------------------------------------------
if __name__ == "__main__":
    wins = games = 0
    while True:
        games += 1
        wins += play()          # True 는 1, False 는 0 으로 계산돼요! (성공하면 +1)
        print(f"전적: {games}판 {wins}승")
        if input("또 할까요? (y/n) > ") != "y":
            break
