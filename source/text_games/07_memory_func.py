"""기억력 게임 (함수 버전) - 8차시 추가 예제: 매개변수 기본값, 반환값, main() 구조

실행 방법: python 07_memory_func.py
"""

# =====================================================================
#   show_sequence(seq, base=1.0) : 숫자를 보여 주고 지움 (base 를 안 주면 1.0초 사용)
#   ask_sequence()               : 입력을 글자 리스트로 바꿔 돌려줌
#   play()                       : 한 판 진행 → 성공 라운드 수 반환
#   main()                       : 여러 판 반복 + 최고 기록
# =====================================================================

import random
import time


def show_sequence(seq, base=1.0):
    """숫자를 잠깐 보여 준 뒤 화면을 지운다 (숫자가 많을수록 오래 보여 줌)"""
    # base=1.0 : "기본값이 있는 매개변수". show_sequence(seq) 처럼 생략 가능
    print(f"\n[{len(seq)}라운드] 기억하세요:", " ".join(seq))
    time.sleep(base + len(seq) * 0.5)
    print("\n" * 40)


def ask_sequence():
    """입력한 글자를 한 글자씩 나눈 리스트로 돌려준다"""
    text = input("방금 본 숫자를 붙여서 입력 > ")
    return list(text.replace(" ", ""))


def play():
    """한 판을 진행하고, 성공한 라운드 수를 돌려준다"""
    seq, level = [], 0
    while True:
        seq.append(random.choice("123456789"))
        show_sequence(seq)
        if ask_sequence() != seq:               # 리스트끼리 비교
            print("틀렸어요! 정답은", "".join(seq))
            return level                        # return 이 무한 반복을 끝내는 출구
        level += 1
        print("정답! 다음 라운드로!")


def main():
    print("=== 기억력 게임 === 화면에 나온 숫자를 기억해서 입력하세요!")
    best = 0
    while True:
        level = play()
        best = max(best, level)                 # 최고 기록 = 지금까지 중 가장 큰 값
        print(f"이번 기록: {level}라운드 / 최고 기록: {best}라운드")
        if input("또 할까요? (y/n) > ") != "y":
            break


if __name__ == "__main__":
    main()
