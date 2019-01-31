# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class people:
    def __init__(self, surname, name, fathername):
        self._surname = surname
        self._name = name
        self._fathername = fathername
    
    @property
    def get_name(self):
        return "{0} {1}. {2}.".format(self._surname, self._name[:1], self._fathername[:1])


class student(people):
    def __init__(self, surname, name, fathername, school, mother, father, class_room):
        people.__init__(self, surname, name, fathername)
        self.school = school
        self._parents = {'father': father, "mother": mother}
        self._class_room = class_room
    
    @property
    def get_class_room(self):
        return self._class_room
    
    
    @property
    def get_parents(self):
        return self._parents


class teacher(people):
    def __init__(self, surname, name, fathername, school, subject, classes):
        people.__init__(self, surname, name, fathername)
        self._school = school
        self._subject = subject
        self._classes = classes
    
    @property
    def get_subject(self):
        return self._subject
    
    def get_classes(self):
        return self._classes
"""
    School
    """

class School:
    def __init__(self, school_name, teachers, students):
        self._school_name = school_name
        self._teachers = teachers
        self._students = students
    
    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))
    
    def get_students(self, class_room):
        return [student.get_name for student in self._students if
                class_room == student.get_class_room]
    
    def get_teachers(self, class_room):
        return [teacher.get_name for teacher in self._teachers if
                class_room in teacher.get_classes]
    
    def find_student(self, student_name):
        for person in self._students:
            if student_name == person.get_name:
                teachers = [teachers.get_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                            subject = [teachers.get_subject for teachers in
                                       self._teachers if person.get_class_room in
                                       teachers.get_classes]
                            parents = person.get_parents
                            
                            return {
                                'name': student_name,
                                    'class_room': person.get_class_room,
                                        'teachers': teachers,
                                            'lessons': lessons,
                                                'parents': parents
                                                }

@property
    def name(self):
        return 'School name ' \
            '"{}"'.format(self._school_name)



teachers = [teacher("Petrov", "Ivan", "Ivanich", "1", "Math", ["1A", "2B", "3V"]), teacher("Ivanov", "Vsiliy", "Ivanich", "1", "Physics", ['1A', '2B', '3V'])]


students = [
            student("Ahhh", "Vdddd", "Veee", "1", "Ahh D.V.", "Fddd S. F.", "1A"),
            student("Ahhh", "Vdddd", "Veee", "1", "Ahh D.V.", "Fddd S. F.", "1B"),
            student("Ahhh", "Vdddd", "Veee", "1", "Ahh D.V.", "Fddd S. F.", "1A"),
            student("Ahhh", "Vdddd", "Veee", "1", "Ahh D.V.", "Fddd S. F.", "1B"),
            student("Ahhh", "Vdddd", "Veee", "1", "Ahh D.V.", "Fddd S. F.", "1A"),
            student("Ahhh", "Vdddd", "Veee", "1", "Ahh D.V.", "Fddd S. F.", "1C")]

school = School("Super", teachers, students)

print(school.name)

print("\nClasses list:")
print(", ".join(school.get_all_classes()))

print("\nList '1A' class:")
print("\n".join(school.get_students("1A")))

student = school.find_student("Ahhh V. V.")
print("\nStudent: {0}\nClass: {1}\n Teacher: {2}\nSubject: {3}".format(student["name"], student["class_room"], ", ".join(student["teachers"]), ", ".join(student["lessons"])))

print("Parents: {0}, {1}".format(student["parents"]["mather"], student["parents"]["father"]))

print("\nClass: '1A'\nTeacher: ""{0}".format(", ".join(school.get_teachers("p1"))))
