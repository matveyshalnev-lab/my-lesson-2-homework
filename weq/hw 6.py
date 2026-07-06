#6.1
# import string
#
# letters = string.ascii_lowercase
# start, end = input().split("-")
#
# print(letters[letters.index(start):letters.index(end) + 1])

#6.2

# sec = int(input())
#
# days = sec // 86400
# sec %= 86400
#
# hours = sec // 3600
# sec %= 3600
#
# minutes = sec // 60
# sec %= 60
#
# if days == 1:
#     word = "день"
# elif days >= 2 and days <= 4:
#     word = "дні"
# else:
#     word = "днів"
#
# print(days, word + ",", str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(sec).zfill(2))

#6.3

# num = int(input())
#
# while num > 9:
#     result = 1
#
#     while num > 0:
#         result *= num % 10
#         num //= 10
#
#     num = result
#
# print(num)