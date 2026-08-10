#15.1

class GroupLimitError(Exception):
    """Виняток, якщо у групі більше 10 студентів"""
    pass


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupLimitError(
                "Неможливо додати студента: у групі вже 10 студентів!"
            )

        self.students.append(student)

    def __str__(self):
        result = f"Група: {self.number}\n"
        result += "Студенти:\n"

        for student in self.students:
            result += f"{student}\n"

        return result


# Створюємо групу
group = Group("PD1")

# Додаємо 10 студентів
for i in range(1, 11):
    student = Student(f"Student{i}", f"Surname{i}")
    group.add_student(student)


# Намагаємося додати 11-го студента
try:
    student_11 = Student("Ivan", "Petrenko")
    group.add_student(student_11)

except GroupLimitError as error:
    print(error)


print(group)

