"""가위바위보 (함수 버전) - 9차시: 딕셔너리, 함수, 반환값, main() 구조

실행 방법: python 06_rps_func.py
"""

# =====================================================================
# 딕셔너리(dictionary)란?
#   {키: 값} 짝을 모아 둔 자료구조예요. "이름표를 붙인 사물함"과 비슷해요.
#   BEATS["가위"] → "보"   : 가위가 이기는 상대는 보
#   score["win"] += 1      : "win" 사물함의 숫자를 1 올림
#
# 리스트는 "번호(인덱스)"로, 딕셔너리는 "이름(키)"으로 값을 찾아요.
# 규칙(누가 누구를 이기나)을 데이터로 적어 두면 if 문이 훨씬 짧아져요!
# =====================================================================

import random

CHOICES = ["가위", "바위", "보"]
BEATS = {"가위": "보", "바위": "가위", "보": "바위"}          # 이기는 쪽: 지는 쪽
RESULT_TEXT = {"draw": "비겼어요!", "win": "이겼다!", "lose": "졌다..."}


def get_pick():
    """올바른 선택이 입력될 때까지 다시 물어본다"""
    while True:
        pick = input("가위 / 바위 / 보 > ")
        if pick in CHOICES:
            return pick
        print("가위, 바위, 보 중에서 입력하세요!")


def judge(me, cpu):
    """'draw' / 'win' / 'lose' 중 하나를 돌려준다"""
    if me == cpu:
        return "draw"
    # BEATS[me] : 내가 낸 것이 이기는 상대. 그게 컴퓨터가 낸 것과 같으면 내가 이김
    return "win" if BEATS[me] == cpu else "lose"


def play_match():
    """먼저 2승 하면 끝나는 한 경기. 내가 이기면 True를 돌려준다"""
    score = {"win": 0, "lose": 0}
    # score.values() → 딕셔너리의 값들만 모음 (예: 1, 0). max 로 가장 큰 값 확인
    while max(score.values()) < 2:
        me, cpu = get_pick(), random.choice(CHOICES)
        result = judge(me, cpu)
        print(f"나: {me}  vs  컴퓨터: {cpu}  →  {RESULT_TEXT[result]}")
        if result != "draw":
            score[result] += 1          # 결과 문자열을 그대로 키로 사용!
        print(f"현재 점수  나 {score['win']} : {score['lose']} 컴퓨터")
    return score["win"] == 2            # 비교식의 결과(True/False)를 그대로 반환


def main():
    print("=== 가위바위보 === 먼저 2승 하면 이깁니다!")
    wins = games = 0
    while True:
        games += 1
        if play_match():
            wins += 1
            print("최종 승리!")
        else:
            print("아쉽게 패배...")
        print(f"전적: {games}경기 {wins}승")
        if input("또 할까요? (y/n) > ") != "y":
            break


if __name__ == "__main__":
    main()
