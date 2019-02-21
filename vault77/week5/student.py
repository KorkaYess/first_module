import random

class Student:
    
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def hello(self):
        print('Hello, my name is {}. My grades are {}'.format(self.name, self.grades))

    def gpa(self):
        return sum(self.grades) / len(self.grades)


class ExchangeStudent(Student):

    def __init__(self, name, grades, country):
        super().__init__(name, grades)
        self.country = country

    def hello(self):
        super().hello()
        print('I am from {}'.format(self.country))


countries = ['Kazakhstan', 'Ukraine', 'UAE', 'Japan', 'Singapure']
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eric', 'Fiona']

def generate_grades():
    grades = []
    for i in range(random.randint(1, 5)):
        grades.append(1 + random.random() * 3)
    return grades


if __name__ == '__main__':
    students = [
        ExchangeStudent(
            name=random.choice(names),
            grades=generate_grades(),
            country=random.choice(countries)
        )
        for i in range(5)
    ]
    best_student = max(students, key=lambda x: x.gpa())
    print(best_student.name, best_student.country, best_student.grades)