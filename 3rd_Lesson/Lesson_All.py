# Dictionary 
dic = {
    'name' : 'Heh',
    'phone' : '+821072836742',
    'birth' : '1992-12-21'
}
print(f"{dic.keys()}") #prints the keys of the dic

a = list(dic.keys())
print(f"a : {a}")
print(f"{type(a)}")

print(f"{dic.values()}")
print(f"{dic.items()}")

for key, value in dic.items():
    print(f"{key}")
    print(f"{value}")

# function
# input -> function -> output
# Ex)
# def function_name(input):
#     command1
#     command2
#     return return_value

# function without output
# def function_name(input):
#     command1
#     command2

# function without input
# def function_name():
#     command1
#     command2

def add(a, b):
    return a+b
num1=11
num2=89
num3 =100
result = add(num1, num2)
print(f"Result : {result}")

def add1(a, b):
    print(f"{a}, {b}'s addition is {a+b}")

result = add1(num1, num2)
print(f"Result : {result}")

def say_it_back():
    return 'say it back'
print(f"{say_it_back()}")

def many_input(a,b,c):
    return a+b+c

additon = many_input(num1, num2, num3)
print(f"Result : {additon}")

def too_many_input(*args):
    result = 0
    for i in args:
        result = result +  i
    return result

additon2 = too_many_input(1,2,3,4,5,6,7,8,9,10)
print(f"Result : {additon2}")

def kw_func(**kwargs):
    print(f"{kwargs}")

kw_func(name = 'idk', age = '19', school =  'swjb')


def kw_func1(**kwargs):
    for key, value in kwargs.items():
        print(f"key : {key} / value : {value}")

kw_func1(name = 'idk', age = '19', school =  'swjb')

# Assignment

def definition(a):
    if a%2 != 0:
        return False
    else:
        return True

a= int(input("enter num: "))
result12 = definition(a)
print(f"{result12}")

def order_price(**kwargs):
    pr = kwargs.get("price")
    qu = kwargs.get("quan")
    fee = kwargs.get("delivery_fee")
    return pr*qu+fee

total_price = order_price(price = 1000, quan = 5, delivery_fee =  3000)
print(f"{total_price}")