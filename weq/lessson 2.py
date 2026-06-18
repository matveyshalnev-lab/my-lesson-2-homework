from operator import truediv
from token import NUMBER

# number: int = 10 + 1
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

# let num = 10
# num = 30;

# my_site.com?param1=123&param2=qwerty

NUMBER = 10
print(NUMBER)

# pep

#
# a = 10
# b = 20
# first_number = 10
# second_number = 20
# #
# ###
#userName1 = "Vasya"
#print(userName1)
#user_name = "Petya"
#print(user_name)

####
#number1 = 10
#print(number1)
#print(number := 10 + number1)   # моржовій оператор
#print(number)

# num2 = 3
# result = 2 + (num1 :=4) + num2
# print(result)
# print(num1)

######
# + - * /
# print(2+3)
# print(2-3)
# print(2*3)
# print(2/3)
# print(2 ** 3)
# print(2 // 3)
# print(2 % 3)
# ##
# num1 = 19
# num2 = 6
# print(num1 // num2) #3
# print(num1 % num2)  #1

############

# number = 456
# n1 = number // 100 #4
# n2 = number % 100 // 10 #5
# n2_v2 = number % 10 // 100
# n3 = number % 10 # 6
# #
# print(n1)
# print(n2)
# print(n2_v2)
# print(n3)

# number = 123
# n1 = number // 100 #4
# n2 = number % 100 // 10 #5
# n2_v2 = number // 10 % 10
# n3 = number % 10 # 6
# #
# print(n1)
# print(n2)
# print(n2_v2)
# print(n3)
# #

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# result = first_number + second_number
# print(result)

# # name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # v1
# print("Hello,", name, "You are", age, "years old!")
# # v2
# print("Hello," + name, " You are " + str(age) + " years old!")
# # v3
# print(f"Hello,{name}. You are {age} years old!")

a = int(input())
b = int(input())
d = input()

if d == "+":
    print(a + b)
if d == "-":
    print(a - b)
if d == "*":
    print(a * b)
if d == "/":
    if b == 0:
        print("Не можна")
    else:
        print(a / b)
