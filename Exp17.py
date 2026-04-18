class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

s1 = Student("Ayaan", 19, "251M031")
s1.display()