MINIMUM_GROUP_SIZE = 2


class Students:
    def __init__(self, name, position):
        self.name = name
        self.position = position + 1
        self.has_met = []


def get_students():
    return open("student_list.txt", "r").readlines()


def number_of_students():
    return len(get_students())


def number_of_students_for_each_student_to_meet():
    return number_of_students() - 1


def create_student_objects(students):
    for i in students:
        student = Students(i, students.index(i))


def find_optimal_group_size(students_to_meet):
    print(students_to_meet)
    for i in range(6):
        if i >= MINIMUM_GROUP_SIZE:
            if students_to_meet % (i) == 0:
                print(i)


def generate_minimum_number_of_groups_where_everyone_meets_at_least_once():
    students = get_students()
    create_student_objects(students)
    find_optimal_group_size(number_of_students_for_each_student_to_meet())


generate_minimum_number_of_groups_where_everyone_meets_at_least_once()

