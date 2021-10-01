

# def sum_numbers(a, b):
#     return a + b
#
#
# f = lambda a, b: a + b
# print(f(10, 5))
#
#
# print(sum_numbers(10, 5))

#
# def sum_list(numbers: list):
#     total_sum = 0
#     for number in numbers:
#         total_sum += number
#
#     return total_sum
#
# # input_number_2 = lambda: int(input("Enter number: "))
#
#
# def increment_number(number):
#     return number + 1
#
#
# def multiply_number(number):
#     return number * 2
#
#
# def modify_list(numbers, func):
#     for i, number in enumerate(numbers):
#         numbers[i] = func(number)
#     return numbers
# #
# #
# numbers = [1, 2, 3]
# # # result_list = modify_list(numbers, multiply_number)
# #
# # # result_list = list(map(increment_number, numbers))
# result_list = list(map(lambda number: number + 1, numbers))
# result_list_2 = list(map(lambda number: number * 2, numbers))
# result_list_3 = list(map(lambda number: number / 2, numbers))
# result_list_4 = list(map(lambda number: number - 1, numbers))
#
# print(result_list, result_list_2, result_list_3, result_list_4, sep="\n")


# def square_number(number):
#     return number ** 2
#
#
# def modify_number(numbers, func):
#     for i, number in enumerate(numbers):
#         numbers[i] = func(number)
#     return numbers


print((lambda a: a * 2)(2))

print((lambda a, b: a ** b)(2, 5))


names = ["Alex", "Namba", "Zara"]

print(list(map(lambda name:"Hello" + " " + name, names)))

nums = [10, 15, 18, 20, 25, 33, ]

print(list(map(lambda number: number % 5 == 0, nums)))