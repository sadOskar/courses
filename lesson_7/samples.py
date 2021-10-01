
try:
    # Блок try позволяет проверить блок кода на ошибки
    number = int(input("Enter a number: "))
except ValueError as e:
    # Блок except обрабатывает ошибку.
    print(e)
else:
    # Блок else позволяет выполнить кодБ если try успешен
    result = 10 + number
    print(f"10 + {number} = ", result)
finally:
    # Блок finally позволяет выполнить кодб не засисимо от результата блоков try и except
    print("Executing Finally...")
# result = 10 + number

# print(result)

# person = {
#     "name": "Alex",
#     "age": 20
# }
#
# try:
#     age = person["is_married"]
# except KeyError:
#     print("Sorry, not correct")