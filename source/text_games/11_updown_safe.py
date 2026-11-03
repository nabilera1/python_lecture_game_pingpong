"""업다운 게임 (테스트 후 개선 버전) - 18차시: 입력 검증, 테스트 케이스, 회귀 테스트

실행 방법: python 11_updown_safe.py
자동 테스트: python 11_updown_safe.py test
"""

# =====================================================================
# 01_updown_basic.py 를 테스트하다가 찾은 문제와 고친 방법
# ---------------------------------------------------------------------
#  번호 | 입력      | 기대 결과                | 기존 결과          | 고친 방법
#  1   | 150       | 다시 입력, 기회 유지       | 기회가 줄어듦       | 범위 검사 low<=n<=high
#  2   | " 50 "    | 50 으로 인정              | "숫자를 입력하세요" | strip() 으로 공백 제거
#  3   | (빈 입력)  | 다시 입력                 | 통과(정상)          | -
#  4   | -5        | 다시 입력                 | 통과(정상)          | isdigit() 가 '-' 를 거부
#
# 테스트하기 쉽게 "판정"과 "입력 검사"를 순수 함수로 분리했어요.
#   parse_guess(text, low, high) : 올바르면 정수, 아니면 None 을 돌려줌 (input 을 쓰지 않음!)
#   → input 없이도 자동 테스트(run_tests)가 가능해요.
# =====================================================================

import random
import sys

MAX_CHANCE = 7


def parse_guess(text, low, high):
    """문자열 text 가 low~high 범위의 정수이면 그 정수를, 아니면 None 을 돌려준다"""
    text = text.strip()                 # 앞뒤 공백 제거
    if not text.isdigit():              # 빈 문자열, 문자, 음수 기호(-)는 여기서 걸러짐
        return None
    number = int(text)
    if not (low <= number <= high):     # 범위 검사
        return None
    return number


def judge(guess, secret):
    """'correct' / 'up' / 'down' 중 하나를 돌려준다"""
    if guess == secret:
        return "correct"
    return "up" if guess < secret else "down"


def read_number(low, high, chance):
    """올바른 숫자가 들어올 때까지 다시 묻는다 (잘못된 입력은 기회를 줄이지 않음)"""
    while True:
        number = parse_guess(input(f"[{low}~{high}] 남은 기회 {chance}회 > "), low, high)
        if number is not None:          # None 인지 확인할 때는 is 를 써요.
            return number
        print(f"{low}~{high} 사이의 숫자를 입력하세요!")


def play(secret=None):
    """한 판 진행. secret 을 넘기면 정답을 고정할 수 있어 테스트에 편리해요."""
    if secret is None:
        secret = random.randint(1, 100)
    low, high, history = 1, 100, []
    for chance in range(MAX_CHANCE, 0, -1):
        guess = read_number(low, high, chance)
        history.append(guess)
        result = judge(guess, secret)
        if result == "correct":
            print(f"정답! {len(history)}번 만에 맞혔어요. 기록: {history}")
            return len(history)
        if result == "up":
            print("UP! 더 큰 수예요.")
            low = guess + 1             # 이제 범위 밖 숫자는 들어오지 않으므로 max 가 필요 없어요.
        else:
            print("DOWN! 더 작은 수예요.")
            high = guess - 1
    print(f"실패! 정답은 {secret}, 기록: {history}")
    return 0


def run_tests():
    """테스트 케이스 표를 코드로 옮긴 자동 테스트 (assert: 조건이 거짓이면 오류 발생)"""
    cases = [
        # (입력, low, high, 기대 결과)
        ("50", 1, 100, 50),     # 정상
        ("1", 1, 100, 1),       # 경계(최솟값)
        ("100", 1, 100, 100),   # 경계(최댓값)
        ("150", 1, 100, None),  # 예외: 범위 밖
        ("abc", 1, 100, None),  # 예외: 문자
        ("", 1, 100, None),     # 예외: 빈 입력
        ("-5", 1, 100, None),   # 예외: 음수
        (" 50 ", 1, 100, 50),   # 예외: 앞뒤 공백 → 인정
    ]
    for text, low, high, expected in cases:
        actual = parse_guess(text, low, high)
        assert actual == expected, f"실패: {text!r} → {actual} (기대 {expected})"
        print(f"통과: {text!r:8} → {actual}")
    assert judge(30, 50) == "up" and judge(70, 50) == "down" and judge(50, 50) == "correct"
    print("모든 테스트 통과!")


if __name__ == "__main__":
    # 명령줄에서 python 11_updown_safe.py test 로 실행하면 자동 테스트
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        play()
