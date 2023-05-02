import sys
import os


def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    elif os.name == 'mac':
        _ = os.system('clear')

    elif os.name == 'posix':
        _ = os.system('clear')

    else:
        _ = os.system('clear')


def main_menu():
    clear()


    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n"
          "♦      WELCOME TO STUDENT REGISTRATION and INFORMATION SYSTEM            ♦\n"
          "♦   •••Choose an option (0-9)•••                                         ♦\n"
          "♦  0)List all the students their registered courses.                     ♦\n"
          "♦  1)List all the courses.                                               ♦\n"
          "♦  2)List all the course that have at least one student registered.      ♦\n"
          "♦  3)Add a new course.                                                   ♦\n"
          "♦  4)Search a course by course code.                                     ♦\n"
          "♦  5)Search a course by name.                                            ♦\n"
          "♦  6)Register a student to a course.                                     ♦\n"
          "♦  7)List top 3 most crowded courses.                                    ♦\n"
          "♦  8)List top 3 students with the most course registrations.             ♦\n"
          "♦  9)Exit                                                                ♦\n"
          "♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")


def next():

    print("-*-" * 20)
    a = input("1-Continue"+"\n""2-Exit"+"\n"+"Please select the option you want to do: ")
    if a == "1":
        print("-*-" * 20)
        print(main_menu())
    elif a == "2":
        sys.exit()
    else:
        print("-*-" * 20)
        print("Please enter a valid number.")

        print(next())


def all_courses_1():
    clear()
    with open("course.txt", "r") as list_course:
        print("Available Courses\n")
        for line in list_course:
            line = line.rstrip()
            line = line.split(";")
            new_line = f"{line[0]} •••> {line[1]} •••> {line[2]} •••> Total Enrolled Student : {line[3]} "
            print(new_line)

    print(next())


def add_new_course_3():
    clear()
    with open("course.txt", "a") as courses:
        courses.seek(0)
        add_new_course_code = str(input("Enter course code: "))
        add_new_course_name = str(input("Enter course name: "))
        add_course_teacher = str(input("Enter teacher of course: "))
        new_course_and_code = add_new_course_code+";"+add_new_course_name
        courses.write(new_course_and_code+";"+add_course_teacher+";"+"\n")
    print("Course successfully added!")

    print(next())


def register_student_6():
    clear()
    true_id = False
    while true_id == False:
        print("The ID must be 6 digits")
        enter_student_id = input("Enter the ID of the new student you will in order to enroll in the course: ")
        x = enter_student_id.isdigit()
        if x == True and len(enter_student_id) == 6:
            true_id = True
            break
        else:
            print("Please enter a valid ID!")

    enter_course_code = input("Enter the code of the course you want to enroll the student in: ")

    with open("student.txt", "r") as students:
        replaced = students.readline()
        full = ""

        while replaced != "":
            new_line = ""
            students_category = replaced.split(";")
            if students_category[0] == enter_student_id:
                new_line = replaced.rstrip() + "," + enter_course_code + "\n"
            else:
                new_line = replaced
            full = full + new_line
            replaced = students.readline()
        with open("student.txt", "w") as student_write:
            student_write.write(full)

    with open('course.txt', 'r') as f:
        courses = f.readlines()

    with open('student.txt', 'r') as f:
        students = f.readlines()

    courses = [course.strip().split(';') for course in courses]
    students = [student.strip().split(';') for student in students]
    student_courses = students[0][2].split(',')
    new_course_code = enter_course_code

    for course in courses:
        if course[0] == new_course_code:
            course[3] = str(int(course[3]) + 1)
    with open('course.txt', 'w') as f:
        for course in courses:
            f.write(';'.join(course) + '\n')

    print(next())


def search_course_by_name_5():
    clear()
    with open("course.txt", "r") as file:
        coursename = input("Enter the coursename what you are searching: ")
        courses = []
        for line in file:
            line = line.strip()
            listss = line.split(";")
            courses.append(listss[1])
        for i in range(len(courses)):
            if coursename in courses[i].split():
                print("-->"+courses[i]+"<--")
        print("If you can't find the course you're looking for, you can search for other courses.\n"
              "But if you found it, you can return to the menu again for different operations or exit from the system.")

    print(next())


def searchbycode_4():
    clear()
    with open("course.txt", "r") as file:
        searchcode = input("Enter the course code which your are searching: ")
        for line in file:
            line = line.strip()
            lists = line.split(";")
            coursecode = lists[0]
            searchedlist = []
            if searchcode == coursecode:
                searchedlist.append(line)
                print("-->"+lists[1]+"<--")
                print(next())
                return searchedlist
            else:
                pass
        if len(searchedlist) != 0:
            pass
        else:
            print("Sorry. This course is not in the system.")

    print(next())


def top3_crowded_courses_7():
    clear()
    with open("student.txt", "r") as file:
        lesson_dict = {}
        for lines in file:
            categories = lines.split(";")
            all_lessons = categories[2].split(",")
            for lesson in all_lessons:
                if lesson in lesson_dict.keys():
                    lesson_dict[lesson] += 1
                else:
                    lesson_dict[lesson] = 1
        top3 = []
        for i in range(0, 3):
            value = max(lesson_dict.values())
            number = list(lesson_dict.values()).index(value)
            name = list(lesson_dict.keys())[number]
            top3.append(name)
            lesson_dict[name] = 0
    order = 1
    for i in top3:
        print(str(order)+")"+i)
        order += 1

    print(next())


def top3_registration_student_8():
    clear()
    with open("student.txt", "r") as f:
        students = []
        lesson_numbers = []
        for block in f:
            blocks = block.split(";")
            all_lessons = blocks[2].split(",")
            students.append(blocks[1])
            lesson_numbers.append(len(all_lessons))

        top3 = []
        orders = 1

        for i in range(3):
            value = max(lesson_numbers)
            value_of_index = lesson_numbers.index(value)
            top3.append(students[value_of_index])
            lesson_numbers[value_of_index] = 0
        print("'"*20)
    for i in top3:
        print(str(orders)+")" + i)
        print("'"*20)
        orders += 1

    print(next())


def at_least_2():
    clear()
    with open("student.txt", "r") as least:
        at_least_list = []
        for line in least:
            line = line.rstrip()
            line = line.split(";")
            all_codes = line[2].split(",")
        all_codes = set(all_codes)
        with open("course.txt", "r") as for_code:
            for line in for_code:
                line = line.split(";")
                at_least_list.append(line[0])
            for i in all_codes:
                if i in at_least_list:
                    print("•"+i)

    print(next())


def students_registered_courses_0():
    clear()
    with open("student.txt", "r") as registered:
        for line in registered:
            line = line.split(";")
            print("•" * 50)
            print(f"{line[1]}:")
            if line[2] == "\n":
                print("There is no course that the student is registered for.")
            else:
                print(line[2])
            print("•" * 50)

    print(next())


while True:
    main_menu()
    islem_numarasi = input("Enter the number of the option you want to do: ")

    if islem_numarasi == "1":
        print("-*-" * 25)
        all_courses_1()
        print("-*-" * 25)
    elif islem_numarasi == "3":
        print("-*-" * 25)
        add_new_course_3()
        print("-*-" * 25)
    elif islem_numarasi == "9":
        print("-*-" * 25)
        print("Exited from the system")
        print("-*-" * 25)
        break
    elif islem_numarasi == "6":
        print("-*-" * 25)
        register_student_6()
        print("-*-" * 25)
    elif islem_numarasi == "5":
        print("-*-" * 25)
        search_course_by_name_5()
        print("-*-" * 25)
    elif islem_numarasi == "4":
        print("-*-" * 25)
        searchbycode_4()
        print("-*-" * 25)
    elif islem_numarasi == "7":
        print("-*-" * 25)
        top3_crowded_courses_7()
        print("-*-" * 25)
    elif islem_numarasi == "8":
        print("-*-" * 25)
        top3_registration_student_8()
        print("-*-" * 25)
    elif islem_numarasi == "2":
        print("-*-" * 25)
        at_least_2()
        print("-*-" * 25)
    elif islem_numarasi == "0":
        print("-*-" * 25)
        students_registered_courses_0()
        print("-*-" * 25)
