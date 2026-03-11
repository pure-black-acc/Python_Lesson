# print -> print is the basic command that prints the contents in the output terminal.
# Ex) print('Context')
print('This is py ;>')
print('-------------------------------------------')
# "while" -> it's a loop command which repeatedly executes a block of code as long as a specified condition remains.
# Ex)
# a = 10
# while a < 1:
#     print(a)
#     a = a - 1
num = 1 # define variable
while num <= 5: # loop
    print(num)
    num = num + 1
print('-------------------------------------------')
# while inf loop
# Ex)
# while 1:
#     print('bruh')


# 'for' command is a loop command such as 'while'
# the list is inserted into the command to execute and the looping will be determined via sizes of the list given
# Ex)
names = ['Adam', 'Ayin', 'benjamin', 'carmen']
for temp in names:
    print(temp)
print('-------------------------------------------')
# 'range' is the subcommand which can be used with 'for' command
# Ex)
for count in range(1, 10):
    print(count)
print('-------------------------------------------')    
# if u want to go backwards, use this
for count in range(10, 1, -2):
    print(count)
print('-------------------------------------------')
# 'if' statement is the command which executes when the given input, or the state matches the condition in the 'if' statement
# Ex)
pw = 'xD'
if pw == 'xD':
    print('pw matched')
else:
    print('pw incorrect')
print('ending process')
# print('-------------------------------------------')

# Assignment 1
# add 1 ~ n with inf loop, however, find the n when the total of the (1~n) is over 100
# Condition: use inf loop, and 'break' command, Use 2 variables, Use only 1 'if' statement
n = 1 #inital declare
current_total = 1 
while 1: #inf loop
    print("current total = ", current_total, "+", n, "=", current_total + n)
    current_total = n + current_total
    if(current_total > 100):
        print("current n is", n)
        # print("current n is {}".format(n)) this is also viable
        break
    n = n + 1
print('-------------------------------------------')
# Assignment 2
# print 1 ~ 10, but only print odd numbers only
# Condition: 
# - use variable "num" -> set to 0 
# - in 'while' statement, check if 'num' variable is less then 10 or same.
#   - check if the 'num' variable is odd number(num%2 !=0)
#   - include this in the loop "num = num + 1"

# standard anw:
# num = 0
# while num <= 10:
#     if num%2 != 0:
#         print(num)
#     num =+ 1
    
# 'contiune' is command which makes the loop to go to the starting point without execting the remaing codes
# with 'continue' command:
num = 0
while num < 10:
    num = num + 1
    # print('current num is', num) -> for debug
    if num%2 == 0:
        continue

    print(num)
print('-------------------------------------------')

# Assignment 3
# Make a program that inputs the scores of the exam and output grades following the scores
# Conditions: over 100 or less then 0 will be marked as 'Invaild Scores', A => starts from 90, B => 80, C => 70, D => 60, rest is F
score = int(input('Insert the scores to determine the Grades: '))

if score > 100 or score < 0 or score == 'NULL':
    print('Invaild Score')
elif score >= 90:
    print('Your Grade is A')
elif score >= 80:
    print('Your Grade is B')
elif score >= 70:
    print('Your Grade is C')
elif score >= 60:
    print('Your Grade is D')
else:
    print('Your Grade is F')
print('-------------------------------------------')
    
# Assignment 4
# Make a program that inputs the person names and if the person's name matches the list tht was declared, 
# print if checkup is needed if not, prints it's not needed.
# Conditions: use 'in', 'not in'
checkup_list = ['James', 'Lily', 'Sam', 'Mark']
name = input('Enter your name to check(Only First Name!): ')
if name in checkup_list:
    print('You are viable for checkup.')
else:
    print('you are not viable for checkup for now.')

# Assignment 5
for a in range(1, 6):
    print('*'*a)

# Assignment 6:
for a in range(1, 10, 2):
    print('*'*a)

