
a = 20
b = 20

if a > b:
    print("This is an if block: a > b")
elif a == b:
    print("This is an elif block: a = b")
else:
    print("This is an else block: a < b")


# 0, 0.0, False, None, [], (), {}, пустая строка вовращают False в условиях

name = None

if name is not None:
    print(name)
else:
    print("name variable is not None")

a = 10
b = 100

# Оператор is проверяет на соотвествие памяти, == проверяет значение переменных

print(hex(id(a)))
print(hex(id(b)))

if a is b:
    print("a is b")
else:
    print("a is not b")

if a == b:
    print('a == b')
else:
    print("a != b")

