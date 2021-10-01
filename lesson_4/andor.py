
names = {"Brandon", "Sara"}

name = "Brandon"


# True and True = True
# True and False = False
# True or True = True
# True or False = True
# False and False = False
# False or False = False

if name is not None and name in names:
    print("Yes it is")
else:
    print("No it's not")

result = (1 + 5 + 10) * 10
print(result)

a = 10
b = 10

if a == b and (a is not None and a is not False):
    print('yes')
else:
    print('no')