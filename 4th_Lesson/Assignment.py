def odd_list(list):
    b = list
    for a in list:
       if a%2 == 0:
           b.remove(a)

    print(b)

list = [1,2,3,4,5,6,7,8,9,10]

odd_list(list)

def say_it_back(*arg):
    for a in arg:
        print(a)

say_it_back("hi", "hello", "mate")

def max(*arg):
    max = 0
    for i in arg:
        if max < i:
            max = i
    return max

print(max(1,543,764465,234,132))

def info(**data):
    for key, value in data.items():
            print(f"{key}: {value}")

info(name='hi', city='kr', school='idk')