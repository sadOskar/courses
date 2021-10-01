
numbers = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7]
total = sum(numbers)
print(total)

print(numbers.count(6))

# numbers.reverse()
# print(numbers)

numbers.pop(-1)
print(numbers)

numbers.append('Askar')
print(numbers)

nums = [8, 9, 14]
numbers.extend(nums)
print(numbers)

numbers.insert(3, 11)
print(numbers)

numbers.remove('Askar')
print(numbers)

numbers.sort()
print(numbers)

man_dict = {
    'first_name': input(),
    'last_name': input(),
    'age': input(),
    'city': input(),
}






print(man_dict)