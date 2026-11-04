"""18차시 코딩 테스트 2: 안전한 나눗셈 계산기 (도전) - 정답 예시 코드

첫째 줄에 n, 다음 n줄에 `a b`가 주어집니다. a를 b로 나눈 몫을 출력하되, b가 0이면 `오류: 0으로 나눌 수 없음`, 정수가 아닌 값이 있으면 `오류: 정수가 아님`을 출력하세요. 두 가지가 함께 해당하면(예: `x 0`) 정수가 아님을 먼저 판단합니다. `try–except`를 사용하세요.
"""

for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ValueError:
        print("오류: 정수가 아님")
    except ZeroDivisionError:
        print("오류: 0으로 나눌 수 없음")
