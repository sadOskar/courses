
# a = set()
# a.add(1)
# a.add(2)
# a.add(3)
#
# print(a)
#
# total = sum(a)
# print(total)
#
# a.add("legacy")
# a.add("chaser")
# print(a)
#
# b = {4, 5, 6}
#
# c = a.union(b)
# print(c)
#
# c.remove(4)
# print(c)
#
# c.discard(1000)
# print(c)
#
# c.pop()
# print(c)
#
# c.clear()
# print(c)
#
# menu_swed = ('lagman', 'plov', 'manty', 'samsy', 'mastava')
# print(menu_swed)
#
# # menu_swed[0] = 'lazuro'
# # print(menu_swed)
#
# menu_swed = ('lagman', 'plov', 'manty', 'samsy', 'mastava')
# for i in menu_swed:
#     print(i)

# a = (1, 2, [5, 1, 6])
#
# a[2][1] = 'hello'
#
# print(a)


# a = 'string'

# print(dir(a))
#
# a.capitalize()
# print(a)

# index = a.index('string')
# print(index)
#
# a.casefold()
# print(a)
#
# join = ','.join(a)
# print(join)

i = {}

# for letter in "abcde":
#     i[letter]="abcde".index(letter)
#     print(i)

me_dict = {
    'first_name': 'Bolzhurov',
    'name': 'Askar',
    'patronymic': 'Adamovich',
    'tel.number': 123456,
    'address': 'Komsomolskay str.',
}

for key in me_dict.keys():
    print(key, ':', me_dict[key])

for key in me_dict:
    print(key)
me_dict.pop('name')
me_dict.pop('patronymic')
print(me_dict)

key_1 = me_dict['first_name']
print(key_1)


# key_1 = me_dict['first_name']
# key_2 = me_dict['name']
# key_3 = me_dict['patronymic']
# key_4 = me_dict['tel.number']
# key_5 = me_dict['address']
# print(key_1)
# print(key_2)
# print(key_3)
# print(key_4)
# print(key_5)


# keys = me_dict.keys()

