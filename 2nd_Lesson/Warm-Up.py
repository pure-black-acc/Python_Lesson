# Assignment 5(from last lesson)
# Print the '*' from 1 to 5(each time you have to change line when done with the line, only here use 'while' loop)
a=1
while a <= 5:
    print('*'*a, a)
    a=a+1

# Assignment 6(from last lesson):
# Print the '*' from 1 to 9 but the number grow 2 time not + 1(Conditions are same with the above one)
for a in range(1, 10, 2):
    print('*'*a, a)

# b = int(input('enter num'))
# for c in range(1, b+1, 2):
#     spaces = " " * (c + 1 - b)
#     print(spaces+'*'*c+spaces)
#     c=c+1
