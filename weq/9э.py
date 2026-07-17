#9.1
# def popular_words(text, words):
#     text = text.lower().split()
#     d = {}
#
#     for i in words:
#         d[i] = text.count(i)
#
#     return d
#
#
# assert popular_words(
#     '''When I was One I had just begun When I was Two I was nearly new''',
#     ['i', 'was', 'three', 'near']
# ) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
#
# print('OK')

##9.2
# def difference(*args):
#     if len(args) == 0:
#         return 0
#     return round(max(args) - min(args), 2)
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
#
# print("OK")

