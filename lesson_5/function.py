

#DRY - don't repead yourself


# def print_hello(name):
#     print(f"Hello, {name}")



# print_hello("Alex")
# print_hello("Brandon")
# print_hello("Sara")


# def print_info(name, age=None):
#     print('Name: ', name)
#     print('Age: ', age)
#
# print_info("Brandon")
# print_info("Alex, 25")
# print_info("Sara")





# def sum_numbers(a, b):
#     return a + b
#
# print(sum_numbers(10, 5))


# def sum_list_numbers(numbers: list) -> float:
#     result = 0
#     for number in numbers:
#         result += number
#
#     return result
#
#
# nums = [100, 200, 300]
# print(sum_list_numbers(nums))
#
#
# def reverse_list(numbers: list) -> list:
#     i = len(numbers) - 1
#     reversed_list = []
#     while i >= 0:
#         reversed_list.append(numbers[i])
#         i -= 1
#
#     return reversed_list
#
#
# nums = [10, 20, 30, 40, 50]
# result = reverse_list(nums)
# print(result)



def find_max(a, b, c: float) -> float:

    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > a:
        return c


print(find_max(2, 6, 34))


def find_min(a, b, c: float) -> float:
    if b > a < c:
        return a
    if a > b < c:
        return b
    else:
        return c


print(find_min(129, 6252, 32344))


def max_list_numbers(numbers: list) -> float:
    result = 0
    for number in numbers:
        if number > result:
            result = number

    return result


nums = [1534, 1345, 2376, 2854]
print(max_list_numbers(nums))


def min_list_numbers(numbers: list) -> float:
    result = numbers[-1]
    for number in numbers:
        if number < result:
            result = number

    return result


nums = [1534, 1345, 2376, 2854]
print(min_list_numbers(nums))


def max_list_minus_numbers(numbers: list) -> float:
    result = numbers[-1]
    for number in numbers:
        if number > result:
            result = number

    return result


nums = [-1534, -1345, -2376, -123456, -2854, -12345]
print(max_list_minus_numbers(nums))



def chop(numbers: list) -> list:
    del numbers[0]
    del numbers[-1]
    return numbers


numbs = [1, 2, 3, 4]

print(chop(numbs))


def cumsum(list1: list) -> list:
    total = 0
    result = []
    for val in list1:
        total += val
        result.append(total)
    return result


nums = [1, 2, 3]
print(cumsum(nums))




a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)









