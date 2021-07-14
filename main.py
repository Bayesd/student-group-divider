MAXIMUM_GROUP_SIZE = 6
MINIMUM_GROUP_SIZE = 2
DEFAULT_GROUP_SIZE = 4


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
    for i in range(MAXIMUM_GROUP_SIZE):
        if i >= MINIMUM_GROUP_SIZE:
            if students_to_meet % i == 0:
                return i
            elif students_to_meet % i == 1 and i > 2:
                return i
            else:
                return DEFAULT_GROUP_SIZE


def generate_list_of_groups(size, students):
    list_of_groups = []
    for i in range(students // size):
        list_of_groups.append([])
    return list_of_groups


def generate_minimum_number_of_groups_where_everyone_meets_at_least_once():
    students = get_students()
    create_student_objects(students)
    group_size = find_optimal_group_size(number_of_students_for_each_student_to_meet())
    groups = generate_list_of_groups(group_size, number_of_students())
    for student in students:
        group = (students.index(student)) // group_size
        if len(groups[group]) < group_size:
            groups[group].append(student)
    print(groups)


generate_minimum_number_of_groups_where_everyone_meets_at_least_once()
