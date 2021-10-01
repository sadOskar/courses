

def print_hello_massage():
    print("Hello. I'm a calculator")


def input_numbers():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
    except Exception:
        print("You have to enter numbers!!!")
        exit(1)
    else:
        return a, b
#
#
# allowed_signs = {"+", "-", "*","/"}
#
# try:
#     sign = input("Enter a sign(+, -, *, /): ")
#     if sign not in allowed_signs:
#         raise Exception
# except Exception:
#     print(f"Sign is not in {allowed_signs}")


def input_sign():
    sign = input("Enter a sign(+, -, *, /): ")
    return sign
#     try:
#         sign = input("Enter a sign(+, -, *, /): ")
#         if sign not in allowed_signs:
#             raise Exception
#         return sign
#     except Exception:
#         print(f"Sign is not in {allowed_signs}")
#
#
# allowed_signs = {"+", "-", "*", "/"}

# def is_int(a):
#     try:
#         if type(a) != int:
#             raise Exception("Это не число!")
#         if a % 2 == 0:
#             raise ValueError(f"{a} четное")
#         if a < 0:
#             raise TypeError(f"{a} меньше нуля")
#         if a > 10:
#             raise IndexError(f"{a} больше десяти")
#
#     except ValueError:
#         print(f"{a} четное")
#     except TypeError:
#         print(f"{a} меньше нуля")
#     except IndexError:
#         print(f"{a} больше десяти")
#     except Exception:
#         print("Это не число!")
#
#     return "Программа завершенна"
#
#
# print(is_int('sd'))


# the_list = [1, 2, 3, 4, 5, 6, 7, 8, "sdf"]
# try:
#     a = int(input("Введите индекс: "))
#     if a >= 0:
#         if a >= len(list):
#             raise IndexError("Не верный индекс")
#     print(list[a])
# except IndexError:
#     print("Не верный индекс")
# except ValueError:
#     print("Вводите только цифры")


# def make_shirt():
#     a = "dirty"
#     b = 33
#     i = 0
#     while True:
#         try:
#             text = input("Текст футболки: ")
#             size = int(input("Размер: "))
#             i += 1
#             if text == a and size == b:
#                 print(a, b)
#             if text != a and size != b:
#                 raise Exception
#             print(f"Текст футболки: {text}", f"Размер: {size}")
#             quit(1)
#         except Exception:
#             print("Нету такого товара")
#
#
# make_shirt()


