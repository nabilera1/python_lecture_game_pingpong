"""가위바위보 판정표 버전 - 10차시: 2차원 리스트, 중첩 반복문, 딕셔너리, 함수

실행 방법: python 08_rps_table.py
"""

# =====================================================================
# 2차원 리스트 = "리스트 안에 리스트" = 표(행과 열)
#
#   판정표 TABLE[나][컴퓨터]  (0 비김, 1 이김, 2 짐)
#                 컴퓨터: 가위  바위  보
#     나: 가위 (0)      [  0,   2,   1 ]
#     나: 바위 (1)      [  1,   0,   2 ]
#     나: 보   (2)      [  2,   1,   0 ]
#
#   TABLE[1][0] → 1행 0열 → 나 바위, 컴퓨터 가위 → 1(이김)
#   ※ 첫 번째 [ ] 는 행(나), 두 번째 [ ] 는 열(컴퓨터). 순서를 바꾸면 결과가 반대가 돼요!
#
# 기록표 records 도 2차원 리스트예요.
#   [[1, "바위", "가위", "이김"],
#    [2, "보",   "보",   "비김"], ...]
#   → 중첩 for 문으로 행을 하나씩, 그 안에서 칸을 하나씩 출력해요.
# =====================================================================

import random

CHOICES = ["가위", "바위", "보"]
# 판정표: TABLE[나][컴퓨터] → 0 비김, 1 이김, 2 짐 (if문 대신 표로 규칙을 모델링)
TABLE = [[0, 2, 1],   # 나: 가위
         [1, 0, 2],   # 나: 바위
         [2, 1, 0]]   # 나: 보
RESULT_TEXT = ["비김", "이김", "짐"]


def get_pick():
    """올바른 선택(가위/바위/보)이 들어올 때까지 다시 묻고, 인덱스를 돌려준다"""
    while True:
        pick = input("가위 / 바위 / 보 > ").strip()   # strip(): 앞뒤 공백 제거 ("가위 " → "가위")
        if pick in CHOICES:
            return CHOICES.index(pick)
        print("가위, 바위, 보 중에서 입력하세요!")


def play_match(win_goal=2):
    """먼저 win_goal승 하면 끝나는 한 경기. 기록표(2차원 리스트)와 승리 여부를 돌려준다"""
    score = {"이김": 0, "짐": 0, "비김": 0}
    records = []                      # [[라운드, 나, 컴퓨터, 결과], ...]
    while score["이김"] < win_goal and score["짐"] < win_goal:
        me, cpu = get_pick(), random.randrange(3)   # randrange(3): 0, 1, 2 중 하나
        result = RESULT_TEXT[TABLE[me][cpu]]        # 표에서 값 찾기 → 문구로 변환
        score[result] += 1
        # 한 라운드 = 한 행(리스트)을 기록표 맨 뒤에 추가
        records.append([len(records) + 1, CHOICES[me], CHOICES[cpu], result])
        print(f"나: {CHOICES[me]} vs 컴퓨터: {CHOICES[cpu]} → {result}")
    # 값 2개를 한 번에 돌려줌 (튜플). 받는 쪽: records, won = play_match()
    return records, score["이김"] == win_goal


def print_records(records):
    """기록표를 중첩 반복문으로 출력한다"""
    # 바깥 for: 행(라운드) 하나씩 / 안쪽 for: 그 행의 칸 하나씩
    for row in [["라운드", "나", "컴퓨터", "결과"]] + records:   # 머리글 행 + 기록 행들
        for item in row:
            # :<5 → 5칸 너비로 왼쪽 정렬, end="| " → 줄을 바꾸지 않고 "| "로 끝냄
            print(f"{item!s:<5}", end="| ")
        print()                                                  # 한 행이 끝나면 줄 바꿈


def main():
    print("=== 가위바위보 === 먼저 2승 하면 이깁니다!")
    while True:
        records, won = play_match()
        print_records(records)
        print("최종 승리!" if won else "아쉽게 패배...")
        # .strip().lower(): 공백 제거 + 소문자로 → "Y", " y " 도 모두 "y" 로 인정
        if input("또 할까요? (y/n) > ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
