# 문제: 아래 리스트에서 다음 조건을 만족하는 프로그램을 작성하세요.
# scores = [88, 45, 72, 95, 60, 38, 81, 77, 55, 90]
# 조건:

# 60점 미만인 점수를 리스트에서 모두 제거하세요.
# 남은 점수들을 내림차순으로 정렬하세요.
# 평균 점수를 계산하여 출력하세요.

scores = [88, 45, 72, 95, 60, 38, 81, 77, 55, 90]

scores = [s for s in scores if s >= 60]

scores.sort()
scores.reverse()
avg =  sum(scores) / len(scores)
print(f"{scores}")
print(f"{avg:.2f}")

