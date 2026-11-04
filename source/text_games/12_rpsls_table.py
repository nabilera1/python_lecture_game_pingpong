"""5가지 가위바위보 (산출물 예시) - 딕셔너리 → 2차원 판정표 자동 생성, 기록표, 함수, 자동 테스트

실행 방법: python 12_rpsls_table.py
자동 테스트: python 12_rpsls_table.py test
"""

# =====================================================================
# 08_rps_table.py(3가지)를 5가지 규칙으로 확장한 예시예요.
#   가위 · 바위 · 보 · 도마뱀 · 스팍  (각 선택은 다른 2개를 이기고, 2개에게 져요)
#
# 3가지일 때는 판정표 TABLE 을 손으로 9칸 썼지만, 5가지면 25칸!
# → 규칙은 딕셔너리 BEATS 에 "누가 누구를 이기나"만 적고,
#   판정표(2차원 리스트)는 중첩 반복문으로 자동으로 만들어요.
#   이렇게 하면 규칙이 바뀌어도 BEATS 한 곳만 고치면 됩니다.
# =====================================================================

import random
import sys

CHOICES = ["가위", "바위", "보", "도마뱀", "스팍"]
# 이기는 쪽: [지는 쪽 2개]  (딕셔너리의 값이 리스트)
BEATS = {
    "가위": ["보", "도마뱀"],
    "바위": ["가위", "도마뱀"],
    "보": ["바위", "스팍"],
    "도마뱀": ["스팍", "보"],
    "스팍": ["가위", "바위"],
}
RESULT_TEXT = ["비김", "이김", "짐"]


def make_table(choices, beats):
    """BEATS 딕셔너리로 판정표 TABLE[나][컴퓨터] (0 비김, 1 이김, 2 짐)를 만든다"""
    table = []
    for me in choices:                      # 행: 나
        row = []
        for cpu in choices:                 # 열: 컴퓨터
            if me == cpu:
                row.append(0)
            elif cpu in beats[me]:
                row.append(1)
            else:
                row.append(2)
        table.append(row)
    return table


TABLE = make_table(CHOICES, BEATS)


def get_pick():
    """올바른 선택이 들어올 때까지 다시 묻고, 인덱스를 돌려준다"""
    while True:
        pick = input("가위/바위/보/도마뱀/스팍 > ").strip()
        if pick in CHOICES:
            return CHOICES.index(pick)
        print("다섯 가지 중에서 입력하세요!")


def play_match(win_goal=2):
    """먼저 win_goal승 하면 끝나는 한 경기. 기록표와 승리 여부를 돌려준다"""
    score = {"이김": 0, "짐": 0, "비김": 0}
    records = []                            # [[라운드, 나, 컴퓨터, 결과], ...]
    while score["이김"] < win_goal and score["짐"] < win_goal:
        me, cpu = get_pick(), random.randrange(len(CHOICES))
        result = RESULT_TEXT[TABLE[me][cpu]]
        score[result] += 1
        records.append([len(records) + 1, CHOICES[me], CHOICES[cpu], result])
        print(f"나: {CHOICES[me]} vs 컴퓨터: {CHOICES[cpu]} → {result}")
    return records, score["이김"] == win_goal


def print_records(records):
    """기록표를 중첩 반복문으로 출력한다"""
    for row in [["라운드", "나", "컴퓨터", "결과"]] + records:
        for item in row:
            print(f"{item!s:<5}", end="| ")
        print()


def run_tests():
    """판정표가 규칙에 맞는지 자동으로 검사한다"""
    n = len(CHOICES)
    for a in range(n):
        assert TABLE[a][a] == 0, "같은 선택은 비김이어야 함"
        assert TABLE[a].count(1) == 2 and TABLE[a].count(2) == 2, "각 선택은 2개를 이기고 2개에게 져야 함"
        for b in range(n):
            if a != b:
                # 대칭성: a가 b를 이기면(1) b는 a에게 진다(2)
                assert {TABLE[a][b], TABLE[b][a]} == {1, 2}, (CHOICES[a], CHOICES[b])
    assert RESULT_TEXT[TABLE[CHOICES.index("스팍")][CHOICES.index("가위")]] == "이김"
    print("판정표 테스트 통과!")
    for name, row in zip(CHOICES, TABLE):
        print(f"{name:<4}", row)


def main():
    print("=== 5가지 가위바위보 === 먼저 2승 하면 이깁니다!")
    while True:
        records, won = play_match()
        print_records(records)
        print("최종 승리!" if won else "아쉽게 패배...")
        if input("또 할까요? (y/n) > ").strip().lower() != "y":
            break


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
