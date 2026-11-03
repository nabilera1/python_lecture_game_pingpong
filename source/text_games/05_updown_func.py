"""업다운 게임 (함수 버전) - 8차시: 함수 정의·호출, 매개변수, 반환값, main() 구조

실행 방법: python 05_updown_func.py
"""

# =====================================================================
# 01_updown_basic.py 와 무엇이 달라졌을까요?
# ---------------------------------------------------------------------
# 같은 게임을 "기능별 함수"로 나누었어요. (문제 분해 → 함수 하나 = 작은 문제 하나)
#
#   read_number(low, high, chance) : 숫자가 들어올 때까지 다시 묻고 정수로 돌려줌
#   judge(guess, secret)           : "correct" / "up" / "down" 판정 결과를 돌려줌
#   play()                         : 한 판 진행, 맞힌 횟수(실패 시 0)를 돌려줌
#   main()                         : 여러 판 반복 + 최고 기록 관리
#
# 함수로 나누면 좋은 점
#   1) 이름만 봐도 무슨 일을 하는지 알 수 있어요. (가독성)
#   2) judge() 처럼 작은 함수는 따로 테스트하기 쉬워요. (테스트 용이성)
#   3) 같은 코드를 여러 번 쓰지 않아도 돼요. (재사용)
# =====================================================================

import random

MAX_CHANCE = 7          # 대문자 이름 = 바뀌지 않는 값(상수)이라는 약속


def read_number(low, high, chance):
    """숫자가 입력될 때까지 다시 물어보고, 정수로 바꿔 돌려준다"""
    # low, high, chance 는 "매개변수": 함수를 부를 때 넘겨받는 값이에요.
    while True:
        text = input(f"[{low}~{high}] 남은 기회 {chance}회 > ")
        if text.isdigit():
            return int(text)        # return: 값을 돌려주고 함수를 즉시 끝냄 (반복도 끝!)
        print("숫자를 입력하세요!")


def judge(guess, secret):
    """'correct' / 'up' / 'down' 중 하나를 돌려준다"""
    if guess == secret:
        return "correct"
    # 조건 표현식으로 두 경우를 한 줄에
    return "up" if guess < secret else "down"


def play():
    """한 판을 진행하고, 맞힌 횟수를 돌려준다 (실패하면 0)"""
    secret = random.randint(1, 100)
    low, high, history = 1, 100, []

    # range(7, 0, -1) → 7, 6, 5, 4, 3, 2, 1  (시작, 끝(포함 안 함), 간격)
    for chance in range(MAX_CHANCE, 0, -1):
        guess = read_number(low, high, chance)    # 함수 호출 → 돌려받은 값을 guess 에 저장
        history.append(guess)
        result = judge(guess, secret)
        if result == "correct":
            print(f"정답! {len(history)}번 만에 맞혔어요. 기록: {history}")
            return len(history)
        if result == "up":
            print("UP! 더 큰 수예요.")
            low = max(low, guess + 1)       # 범위를 좁혀 간다
        else:
            print("DOWN! 더 작은 수예요.")
            high = min(high, guess - 1)
    print(f"실패! 정답은 {secret}, 기록: {history}")
    return 0


def main():
    print("=== 업다운 === 1~100 사이의 숫자를 7번 안에 맞히세요!")
    best = 0                                # 가장 적은 시도 횟수 기록 (0 = 아직 기록 없음)
    while True:
        tries = play()
        # tries 가 0이 아니고(성공), 처음 기록이거나 더 적은 횟수면 최고 기록 갱신
        if tries and (best == 0 or tries < best):
            best = tries
        print(f"최고 기록: {best}번" if best else "아직 성공 기록이 없어요.")
        if input("또 할까요? (y/n) > ") != "y":
            break


# 이 파일을 직접 실행할 때만 main() 을 호출 (다른 파일에서 import 할 때는 실행 안 됨)
if __name__ == "__main__":
    main()
