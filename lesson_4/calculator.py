

number_1 = int(input('Введите первое число: '))
operation = input('Введите одну из операций +, -, *, /: ')
number_2 = int(input('Введите второе число: '))
if operation == '+':
    print('total:', number_1 + number_2)
elif operation == '-':
    print('total:', number_1 - number_2)
elif operation == '*':
    print('total:', number_1 * number_2)
elif operation == '/':
    if number_2 != 0:
        print('total:', number_1 / number_2)
    else:
        print('На ноль делить нельзя!')