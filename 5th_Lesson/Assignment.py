import random
def stargazer(a):
    for i in range(1, a+1):
        b = a+1 - i
        while b > 0:
            print(end=" ")
            b = b - 1
        print('*'*i)
# a = int(input())
# stargazer(a)

def mul(a):
    for i in range(1, 10):
        print(f"{a} x {i} = {a*i}")

# b = int(input())
# mul(b)

def mul_pro():
    got_it = False
    while got_it == False:
        a = random.randint(1,10)
        b = random.randint(1,10)
        total = a*b
        anw = int(input(f'what is {a} x {b}? '))
        if total == anw:
            print('correct.')
            got_it = True
        else:
            print('incorrect. try again.')
            continue

# mul_pro()

# def mul_pro_v2():
#     a = random.randint(1,10)
#     b = random.randint(1,10)
#     inp(a, b, 0)

# def inp(a, b, tf):
#     while tf == False:
#         total = a*b
#         anw = input(f'what is {a} x {b}? \n Tip: you can type "skip" if you do not know: ')
#         if isinstance(anw, int) == True:
#             if total == anw:
#                 print('correct.')
#                 tf = True
#             else:
#                 print('incorrect. try again.')
#                 mul_pro_v2()
                
#         else:
#             print(f"Please type a whole number, or you can skip this question")
#             continue
   
# mul_pro_v2()
