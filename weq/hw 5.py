#5.1
# import keyword
# import string
#
# print(keyword.kwlist)
#
# test_data = ["_", "__", "___", "import"]
#
# for test_variable_name in test_data:
#
#     if test_variable_name in keyword.kwlist:
#         print(False)
#         continue
#
#     if test_variable_name[0].isdigit():
#         print(False)
#         continue
#
#     if test_variable_name != test_variable_name.lower():
#         print(False)
#         continue
#
#     if " " in test_variable_name:
#         print(False)
#         continue
#
#     if "__" in test_variable_name:
#         print(False)
#         continue
#
# bad = string.punctuation.replace("_", " ")
#
# for i in bad:
#         if i in test_variable_name:
#             print(False)
#             break
# else:
#     print(True)

    #5.2
# while True:
#
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#
#     operation = input("Введіть операцію (+, -, *, /): ")
#
#     if operation == "+":
#         result = num1 + num2
#         print(result)
#
#     elif operation == "-":
#         result = num1 - num2
#         print(result)
#
#     elif operation == "*":
#         result = num1 * num2
#         print(result)
#
#     elif operation == "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(result)
#         else:
#             print("Помилка!!! ділення на нуль неможливе")
#
#     else:
#         print("Помилка!!! невідома операція")
#
#     anwser = input("Продовжити? (y/yes): ")
#
#     if anwser != "y" and anwser != "yes":
#         break

#5.3

# import string
#
# text = input()
#
# for i in string.punctuation:
#     text = text.replace(i,"")
#
# words = text.split()
#
# hashtag = "#" + "".join(word[:1].upper() + word[1:] for word in words)
#
# hashtag = hashtag[:140]
# print(hashtag)