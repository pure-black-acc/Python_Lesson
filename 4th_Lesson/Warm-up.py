# Addition function
# def addition(a,b):
#     total = a + b
#     print(f"{a} + {b} = {total}")

# a = int(input("num 1: "))
# b = int(input("num 2: "))
# addition(a,b)

# variation
# def addition_triple(a,b,c):
#     total = a + b + c
#     print(f"{a} + {b} + {c} = {total}")

# a = int(input("num 1: "))
# b = int(input("num 2: "))
# c = int(input("num 3: "))
# addition_triple(a,b,c)

# w. return 
# def addition_triple_return(a,b,c):
#     total = a + b + c
#     return total

# a = int(input("num 1: "))
# b = int(input("num 2: "))
# c = int(input("num 3: "))
# addition = addition_triple_return(a,b,c)
# print(f"{a} + {b} + {c} = {addition}")

# def say_it_back(smth):
#     print('hi '+ smth)

# say_it_back('mate')

# # list addition
# def addition_list(lists):
#     total = 0
#     for a in lists:
#         total = total + a
#         print(f'done adding {a} times current total = {total}')
        
    
#     print(total)

# list = [1,2,3,4,5,6,7,8,9,10]

# addition_list(list)

# Addition function with args
def addition(*arg):
    total = 0
    for a in arg:
        total = total + a
    return total
    
result = addition(1,5634,45323,234,1,324,234231,678,56)
print(f"the total is {result}")



# Addition function with args
def avg(*arg):
    total = 0
    for a in arg:
        total = total + a
    total = total / len(arg)
    return total
    
result = avg(1,5634,45323,234,1,324,234231,678,56)
print(f"the total is {result}")

