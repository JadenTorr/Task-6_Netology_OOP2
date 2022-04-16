class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            return 'Ошибка'
    
    def av_raiting(self):
        sum_ = 0
        len_ = 0
        for el in self.grades:
            sum_ += sum(self.grades[el])
            len_ += len(self.grades[el])
        return round(sum_ / len_, 2)
    
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.av_raiting()}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__ (self, other):
        if not isinstance(other, Student):
            print('Not a Student')
        return self.av_raiting() < other.av_raiting()
 

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade = {}

    def set_raiting(self):
        sum_ = 0
        len_ = 0
        for el in self.grade:
            sum_ += sum(self.grade[el])
            len_ += len(self.grade[el])
        return round(sum_ / len_, 2)
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.set_raiting()}'
        return res

    def __lt__ (self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
        return self.set_raiting() < other.set_raiting()
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'GIT']
some_student.finished_courses += ['Введение в программирование']

other_student = Student('Pol', 'Secret', 'male')
other_student.courses_in_progress += ['Python', 'GIT']
other_student.finished_courses += ['Введение в программирование']

some_mentor = Reviewer('Some', 'Buddy')

some_lecturer = Lecturer('Saimon', 'Peg')
some_lecturer.courses_attached = ['GIT', 'Python']
# some_lecturer.grade['GIT'] = 6
# some_lecturer.grade['Python'] = 4


other_lecturer = Lecturer('Max', 'Torr')
other_lecturer.courses_attached = ['GIT', 'Python']
# other_lecturer.grade['GIT'] = 5
# other_lecturer.grade['Python'] = 5

some_student.rate_lecture(some_lecturer, 'Python', 9)
some_student.rate_lecture(some_lecturer, 'Python', 6)
some_student.rate_lecture(some_lecturer, 'GIT', 9)

other_student.rate_lecture(other_lecturer, 'Python', 5)
other_student.rate_lecture(other_lecturer, 'Python', 3)
other_student.rate_lecture(other_lecturer, 'GIT', 9)


some_mentor.courses_attached += ['Python', 'GIT']
some_mentor.rate_hw(some_student, 'Python', 10)
some_mentor.rate_hw(some_student, 'Python', 10)
some_mentor.rate_hw(some_student, 'GIT', 9)

some_mentor.rate_hw(other_student, 'Python', 5)
some_mentor.rate_hw(other_student, 'Python', 7)
some_mentor.rate_hw(other_student, 'GIT', 5)


print(some_mentor)
print()
print(some_lecturer)
print()
print(some_student)
print()
print(other_student)
print()
print(some_lecturer > other_lecturer)
print()
print(some_student < other_student)
print()

stud_list = [some_student, other_student]
lecturer_list = [some_lecturer, other_lecturer]

def show_mid_student_avr(student_list, course):
    avr_sum = 0
    len_ = 0
    for students in student_list:
        avr_sum += sum(students.grades[course])
        len_ += len(students.grades[course])
    print(f'Средний бал студентов по курсу {course} составляет: {avr_sum/len_}')

show_mid_student_avr(stud_list, 'Python')

def show_mid_lecturer_avr(lec_list, course):
    avr_sum = 0
    len_ = 0
    for lecturers in lec_list:
        avr_sum += sum(lecturers.grade[course])
        len_ += len(lecturers.grade[course])
    print(f'Средний бал лекторов по курсу {course} составляет: {avr_sum/len_}')

show_mid_lecturer_avr(lecturer_list, 'Python')
