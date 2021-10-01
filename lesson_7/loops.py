
# employees = [
#     {
#         "name": "Brandon",
#         "age": 25,
#         "is_married": "Yes",
#         "department": "TEC",
#     },
#     {
#         "name": "Alex",
#         "age": 20,
#         "is_married": "No",
#         "department": "MIN energo",
#     },
#     {
#         "name": "Sara",
#         "age": 18,
#         "is_married": "No",
#         "department": "GAZPROM",
#     }
# ]
#
# min_age = 100
# name = None
# for employee in employees:
#     if employee["age"] < min_age:
#         min_age = employee["age"]
#         name = employee["name"]
# print(f"name: {name}", "age:", min_age)


# employees = [
#     {
#         "name": "Brandon",
#         "age": 25,
#         "is_married": True,
#         "department": "TEC",
#     },
#     {
#         "name": "Alex",
#         "age": 20,
#         "is_married": False,
#         "department": "MIN energo",
#     },
#     {
#         "name": "Sara",
#         "age": 30,
#         "is_married": False,
#         "department": "GAZPROM",
#     },
#     {
#         "name": "Anton",
#         "age": 30,
#         "is_married": True,
#         "department": "IT",
#     }
# ]
#
# max_age = 0
# name = None
# eldest_employees = []
# for employee in employees:
#     if employee["age"] >= max_age:
#         max_age = employee["age"]
#
# for employee in employees:
#     if employee["age"] == max_age:
#         eldest_employees.append(employee)
#
# print(eldest_employees)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10, 84, 196]
# for number in numbers:
# print(number)
# # max_iter = len(numbers)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#

#
# for item in matrix:
#     for number in item:
#         print(number, end=" ")
#     print()
#
# # max_iter_2 = len(matrix) ** 2




# employees = [
#     {
#         "name": "Brandon",
#         "age": 25,
#         "is_married": True,
#         "department": "TEC",
#     },
#     {
#         "name": "Alex",
#         "age": 20,
#         "is_married": False,
#         "department": "MIN energo",
#     },
#     {
#         "name": "Sara",
#         "age": 30,
#         "is_married": False,
#         "department": "GAZPROM",
#     },
#     {
#         "name": "Anton",
#         "age": 30,
#         "is_married": True,
#         "department": "IT",
#     }
# ]
#
# max_age = 0
# name = None
# eldest_employees_dict = {}
# create_employees = ()

# for employee in employees:
#     if employee["age"] >= max_age:
#         max_age = employee["age"]
#     if eldest_employees_dict.get(employee["age"]) is None:
#         eldest_employees_dict[employee["age"]] = [employee["name"]]
#     else:
#         eldest_employees_dict[employee["age"]].append(employee["name"])
#
#
# print(eldest_employees_dict)
# print(eldest_employees_dict[max_age])


def create_employees() -> list[dict]:
    employees = [
        {
            "name": "Brandon",
            "age": 25,
            "is_married": True,
            "department": "TEC",
        },
        {
            "name": "Alex",
            "age": 20,
            "is_married": False,
            "department": "MIN energo",
        },
        {
            "name": "Sara",
            "age": 30,
            "is_married": False,
            "department": "GAZPROM",
        },
        {
            "name": "Anton",
            "age": 30,
            "is_married": True,
            "department": "IT",
        }
    ]
    return employees

max_age = 0
name = None
eldest_employees_dict = {}
# employees = create_employees()
print(create_employees())


def find_eldest_employees(employees: list):
    max_age = 0
    eldest_employees_dict = {}

    for employee in employees:
        if employee["age"] >= max_age:
            max_age = employee["age"]
        if eldest_employees_dict.get(employee["age"]) is None:
            eldest_employees_dict[employee["age"]] = [employee["name"]]
        else:
            eldest_employees_dict[employee["age"]].append(employee["name"])

    return eldest_employees_dict[max_age]


employees = create_employees()
eldest_employees = find_eldest_employees(employees)

print(eldest_employees)
