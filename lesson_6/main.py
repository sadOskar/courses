
# integer = int(input())
#
# if integer % 2 == 0:
#     print('Even number')
# else:
#     print('Odd number')


# integer_1 = int(input('Enter number: '))
#
# if integer_1 > 0:
#     print('Positive number')
# elif integer_1 == 0:
#     print('Zero number')
# else:
#     print('Negative number')


# name = input("Enter name: ")
#
# if name[0].isupper():
#     print("First letter in upper case")
# else:
#     print("First letter in lover case")

numbers = [100, 50, 25, 10]
difference = 0

for i, number in enumerate(numbers):
    if i == 0:
        difference = number
    else:
        difference = difference - number

print(difference)



