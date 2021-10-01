
# personAge = "Введите Ваш возраст: "
#
# while True:
#     massage = input(personAge)
#     if int(massage) <= 3:
#         print("Билет бесплтный детям до 3-х лет :-)")
#     elif 3 < int(massage) <= 12:
#         print("Цена билет: 10$")
#     else:
#         print("Цена билет: 15$")


# from random import random
# number = round(random() * 100)
# i = 1
# print("Отгадайте число из 7-ми попыток, которое загадал компьютер")
# while i <= 7:
#     a = int(input(str(i) + '-я попытка: '))
#     if a > number:
#         print('Пишите число меньше')
#     elif a < number:
#         print('Пишите загаданое число больше')
#     else:
#         print('Вы угадали с %d-й попытки' % i)
#         break
#     i += 1
# else:
#     print('Game over. Вы исчерпали все попытки')


# sandwich_orders = ['SAM', 'BATYR', 'GEROY']
# finished_sandwiches = []
#
# i = 0
#
# while i < len(sandwich_orders):
#     print(f'I made your {sandwich_orders[i]} sandwich')
#     finished_sandwiches.append(min(sandwich_orders))
#     sandwich_orders.remove(min(sandwich_orders))
# print(finished_sandwiches)
# print(sandwich_orders)


# travel_list = {}
# i = -1
#
# while i < 3:
#     i += 1
#     travel_list[i] = input(str(i))
# print(travel_list)


def make_album(artist, title, songs=None):
    artist_album = {'artist': artist, 'album': title, 'songs': songs}
    return artist_album


album_1 = make_album('Guf', 'Kacheli', 'dsfsdfsdf')
print(album_1)
album_2 = make_album('Basta', 'Drugaya volna')
print(album_2)
album_3 = make_album('Eminem', 'Fake')
print(album_3)

print("Enter 'quit' at any time to stop.")
while True:
    title = input("What's your favorite album? ")
    if title == 'quit':
        break
    artist = input("Who's the artist? ")
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)