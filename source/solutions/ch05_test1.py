"""5차시 코딩 테스트 1: 점수 통계 (기본) - 정답 예시 코드

게임 점수 여러 개가 한 줄에 공백으로 주어집니다. 최고 점수, 최저 점수, 평균(소수 첫째 자리까지)을 한 줄에 하나씩 출력하세요.
"""

scores = list(map(int, input().split()))
print(max(scores))
print(min(scores))
print(f"{sum(scores) / len(scores):.1f}")
