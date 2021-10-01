"""
    scope
    LEGB
    Local, Enclosing, Global, Built-in
"""

# a = "global a"
#
#
# def test():
#     global a
#     # y = "local y"
#     a = 20
#     # print(y)
#     print(a)
#
#
# test()
# print(a)


def outer():
    x = "outer func"
    y = "outer y"

    def inner():
        print(x)
        print(y)

    inner()
    print(x)


outer()




# numbers = [1, 2, 3, 4, 5]
#
#
# # def min():
# #     pass
# #
# #
# # def max():
# #     pass
#
#
# min_number = min(numbers)
# max_number = max(numbers)
#
# print(min_number)
# print(max_number)