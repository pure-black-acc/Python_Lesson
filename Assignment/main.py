# 3-1 dic assignment
print("="*45)
print("3-1 dic assignment\n")
dic = {'name': 'Alan', 'Phone' : '000-0000-0000', 'birth' : '1990-01-01'}
print(f"dic.keys = {dic.keys()}")
print(f"dic.values = {dic.values()}")
for key, values in dic.items():
    print(f"key : {key}")
    print(f"values : {values}")
print("\n")

# 2-2-2 function assignment
print("="*45)
print("2-2-2 function assignment\n")
def add_mul(*args):
    result = 0
    for i in args:
        result += i
    return result
result = add_mul(1,2,3,4,5,6)
print(f"Result = {result}")
print("\n")

# 3-2-2 function assignment
print("="*45)
print("3-2-2 function assignment\n")
def kwargs_funct(**kwargs):
    for key, value in kwargs.items():
        print(f"key : {key},  value : {value}")
kwargs_funct(name = 'suwon', age = '19', school = 'idk')
print("\n")

# 4 class assignment
print("="*45)
print("4 class assignment\n")
class Person:
    def say_hello(self):
        print(f"self: {self}")
p1 = Person()
print(f"p1: {p1}")
p1.say_hello()
p2 = Person()
print(f"p2: {p2}")
p2.say_hello()