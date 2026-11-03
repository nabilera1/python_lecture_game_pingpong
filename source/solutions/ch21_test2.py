"""21차시 코딩 테스트 2: 중복 코드 함수로 묶기 (도전) - 정답 예시 코드

학생 세 명의 '이름 점수1 점수2 점수3'이 한 줄씩 주어집니다. 평균(소수 첫째 자리)과 등급(평균 90 이상 A, 80 이상 B, 70 이상 C, 그 외 D)을 `이름 평균 등급` 형식으로 출력하세요. 등급 계산은 `grade(avg)` 함수 하나로 만들어 중복을 없애세요.
"""

def grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    return "D"

for _ in range(3):
    name, *scores = input().split()
    avg = sum(map(int, scores)) / len(scores)
    print(f"{name} {avg:.1f} {grade(avg)}")
