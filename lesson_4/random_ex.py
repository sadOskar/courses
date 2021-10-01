
import random

number = random.randint(50, 150)
print(number)

if number <= 100:
    a = list(range(0, number, 2))
    print(a)
elif number > 100:
    print(list(range(200, number, -2)))
    # print(a)

# if number <= 100:
#     for seq in range(0, number, 2):
#         print(seq)
# if number > 100:
#     for seq in range(200, number, -2):
#         print(seq)

# number = list(range(50, 150))
# print(number)

