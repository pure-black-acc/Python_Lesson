# 문제: 점수(score)와 출석률(attendance)을 입력받아 최종 등급을 출력하는 프로그램을 작성하세요.
# 조건:

# 출석률이 80% 미만이면 무조건 "F" 출력
# 출석률 80% 이상일 때:

# 90점 이상 → "A"
# 80점 이상 → "B"
# 70점 이상 → "C"
# 60점 이상 → "D"
# 60점 미만 → "F"

score = int(input("점수를 입력하세요: "))
attendance = int(input("출석률을 입력하세요: "))

if attendance >= 80:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
else:
    print("F")