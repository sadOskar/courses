
from functions import print_hello_massage, input_numbers, input_sign
from math_funcs import sum_numbers, multiply_numbers, subtract_numbers, numbers_division


print_hello_massage()
a, b = input_numbers()
sign = input_sign()


if sign == "+":
    print(sum_numbers(a, b))
elif sign == "-":
    print(subtract_numbers(a, b))
elif sign == "*":
    print(multiply_numbers(a, b))
# elif sign == "/":
#     print(numbers_division_on_null(b))
else:
    numbers_division(a, b)