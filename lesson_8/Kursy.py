# profile = {}
profile_1 = []
students = []
course_list = ["Python", "JS", "Java"]

while True:
    try:
        print("Select one of the option: ")
        print("1- Add new student: ")
        print("2- Search student information with ID number: ")
        print("3- Add new course: ")
        print("4- Students list")
        print("5- Quit the program")
        selection_list = [1, 2, 3, 4, 5]
        selection = int(input("Enter the selection: "))
        if selection not in selection_list:
            raise Exception(print("I apologise. you have to make a choice"))
        elif selection == 1:
            profile = {}
            profile["first_name"] = input("Имя: ")
            profile["last_name"] = input("Фамилия: ")
            profile["phone_number"] = list(input("Тел: ").split())
            try:
                course_name = input(f"Выберите курс ({course_list}): ")
                if course_name not in course_list:
                    raise ValueError("We have no courses you want to enter." 
                                     " We saved your data, we let you know when will open this course. ")
                else:
                    profile["courses"] = course_name
                    profile["paid"] = int(input("Оплата: "))
            except ValueError as e:
                print(f"We have no courses you want to enter. Your error is {e}")

            students.append(profile)
            print(profile)
        elif selection == 2:
            n = len(students)
            while True:
                try:
                    id_number = int(input("Enter ID-->"))
                    if id_number <= n:
                        print(students[id_number - 1])
                        breaking_point_1 = int(input("Do you want to quit program? (if yes enter 1/ if not enter 2)"))
                        if breaking_point_1 == 1:
                            break

                    else:
                        print(f"You entered {id_number}")
                        breaking_point = int(input("Do you want to quit program? (if yes enter 1/ if not enter 2)"))
                        if breaking_point == 1:
                            break
                except Exception as e:
                    print(f"We have no student with {id([])} ID. Your error is {e}. \
                        Please Enter the correct. ID have to be less then-->", n - 1)

        elif selection == 3:
            new_course = input("Enter new course name: ")
            course_list.append(new_course)

        elif selection == 4:
            a = len(students)
            print(a)
            # print(students)
            for student in students:
                for key, value in student.items():
                    print(f'{key}: {value}')
        elif selection == 5:
            print("See you next time.")
            break

        else:
            print(f"Your choice is {selection}")
            breaking_point = int(input("Do you want to quit program? (if yes enter 1/ if not enter 2)"))
            if breaking_point == 1:
                break

    except Exception as e:
        print(f"Please chose the correct option.Your error is {e}")