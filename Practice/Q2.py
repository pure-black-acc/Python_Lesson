# 문제: 아래 조건을 만족하는 프로그램을 작성하세요.

# 1부터 100까지의 숫자 중 3의 배수이면서 5의 배수가 아닌 숫자들의 합을 구하고 출력하세요.
# while문만 사용하세요.

a = 1
total = 0
while (a <= 100):
    if a%3 == 0 and a%5 != 0:
        total += a
        print(f"added {a}, current total = {total}")
        a+=1
        pass
    else:
        a+=1
        pass
    

print(f"total: {total}")