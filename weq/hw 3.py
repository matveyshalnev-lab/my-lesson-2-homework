#3.2
# def replace_last(lst):
#     if len(lst) <= 1:
#         return lst
#     return [lst[-1]] + lst[:-1]
#
# #3.3

def split_list(numbers):
    middle = (len(numbers) + 1) // 2
    return [numbers[:middle], numbers[middle:]]
