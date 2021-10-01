
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# print(gcd(24, 36))
#
# t = [[1, 2], [3], [4, 5, 6]]
#
#
# def nested_sum(t):
#     total = 0
#     for item in t:
#         a = sum(item)
#         total += a
#     return total
#
# print(nested_sum(t))
#
#
massages = ["Python", "Java", "Android"]
#
#
def show_massages(massages):
    for item in massages:
        print(item)
    return massages


show_massages(massages)


def send_massages(massages):
    sent_massages = []
    for item in massages:
        sent_massages.append(item)
    return massages, sent_massages


print(send_massages(massages))








# def total_numbers(a, b, c):
#     sum_numbers = 0
#     if a == b == c:
#         sum_numbers = a + b + c
#     else:
#         sum_numbers = (a + b + c) ** 2
#     return sum_numbers
#
#
# print(total_numbers(1, 2, 3))


# def showEmployee(name, wages=9000):
#
#     print(name, wages)
#
#
# name = input()
# wages = int(input())
# showEmployee(name)












