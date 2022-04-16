class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in Mentor.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grade:
                Lecturer.grade[course] += [grade]
            else:
                Lecturer.grade[course] = [grade]
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
            print('Not a Lecturer')
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
        for el in self.grade:
            sum_ += self.grade[el]
        return round(sum_ / len(self.grade), 2)
    
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
some_lecturer.grade['GIT'] = 6
some_lecturer.grade['Python'] = 9

other_lecturer = Lecturer('Max', 'Torr')
other_lecturer.grade['GIT'] = 5
other_lecturer.grade['Python'] = 8

some_mentor.courses_attached += ['Python']
some_mentor.rate_hw(some_student, 'Python', 10)
some_mentor.rate_hw(some_student, 'Python', 10)
some_mentor.rate_hw(some_student, 'Python', 9)

some_mentor.rate_hw(other_student, 'Python', 5)
some_mentor.rate_hw(other_student, 'Python', 7)
some_mentor.rate_hw(other_student, 'Python', 9)


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