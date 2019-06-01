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

class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
    
    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name, self._first_name, self._middle_name)
    
    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name, self._first_name[:1], self._middle_name[:1])


class Student(People):
    def __init__(self, last_name, first_name, middle_name, class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {'mather': mather, 'father': father}
    
    @property
    def get_class_room(self):
        return self._class_room
    
    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name, subjects, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._subjects = subjects
        self._classes = classes
    
    @property
    def get_subjects(self):
        return self._subjects
    
    @property
    def get_classes(self):
        return self._classes

class School:
    def __init__(self, school_name, teachers, students):
        self._school_name = school_name
        self._teachers = teachers
        self._students = students
    
    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))
    
    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]
    
    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]
    
    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                            subjects = [teachers.get_subjects for teachers in
                                        self._teachers if person.get_class_room in
                                        teachers.get_classes]
                            parents = person.get_parents
                            
                            return {
                                'full_name': student_full_name,
                                    'class_room': person.get_class_room,
                                        'teachers': teachers,
                                            'subjects': subjects,
                                                'parents': parents
                                                }

@property
    def name(self):
        return 'School name ' \
            '"{}"'.format(self._school_name)

@property
    def adress(self):
        return '{}'.format(self._school_adress)





teachers = [
            Teacher('Иванов', 'Иван', 'Иваныч', 'Математика',
                    ['1А', '2А', '1Б']),
            Teacher('Петров', 'Василий', 'Васильевич', 'Физика',
                    ['1А', '2А', '1Б'])]


students = [
            Student('Ффф', 'Бббб', 'Вввв', '1А', 'Фффф Ф Ф', 'Бббб Б Б'),
            Student('Ыыыы', 'Яяя', 'Ййй', '1А', 'ффф Ф Ф', 'Бббб Б Б'),
            Student('Ввв', 'Ччч', 'Ппп', '1Б', 'Фффф Ф Ф', 'Бббб Б Б'),
            Student('Аааа', 'Ммм', 'Ввв', '1Б', 'Фффф Ф Ф', 'Бббб Б Б'),
            Student('Пппп', 'Иии', 'Ппп', '2А', 'Фффф Ф Ф', 'Бббб Б Б'),
            Student('Оооо', 'Ттт', 'Ццц', '2А', 'Фффф Ф Ф', 'Бббб Б Б')]

school = School('GB', teachers, students)

print(school.name)


print('\nClasses list:')
print(', '.join(school.get_all_classes()))

print('\nList "1А" class:')
print('\n'.join(school.get_students('1J')))

student = school.find_student('Ффф Бббб Вввв')
print('\nStudent: {0}\nClass: "{1}"\n''Teacher: {2}\nSubject: {3}'.format(student['full_name'],
                                                                          student['class_room'], ', '.join(student['teachers']), ', '.join(student['subjects'])))

print('Parents: {0}, {1}'.format(student['parents']['mather'], student['parents']['father']))

print('\nClass: "2A"\nTeacher: ''{0}'.format(', '.join(school.get_teachers('2А'))))
