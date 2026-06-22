
# All data is private via name-mangling (__name, __marks). 
# @property creates read-only getters for name, percentage, and grade. 
# add_marks() validates range 0-100 and rejects duplicates. 
# Demonstrates why direct attribute access is dangerous and how @property provides a clean public 
# API -- the same pattern used in Django model fields.

# Student class with private marks. 
# @property for read-only access. Reject invalid marks (< 0 or > 100)

class Student:
    def __init__(self, name, roll_num):
        self.__name = name
        self.__roll_num = roll_num
        self.__marks = {}

    @property
    def name(self):
        return self.__name
    
    @property
    def roll_num(self):
        return self.__roll_num
    
    def add_marks(self, subject, marks):

        if subject in self.__marks:
            raise ValueError(f"Marks already added for this subject - {subject}")
        
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        
        self.__marks[subject] = marks

    @property
    def percentage(self):

        if len(self.__marks) == 0:
            return 0
        
        total = sum(self.__marks.values())

        subjects = len(self.__marks)

        return total / subjects
        
    @property
    def grade(self):

        percentage = self.percentage

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        else:
            return "Fail"

student1 = Student("Rahul" , 101)

student1.add_marks("Math", 95)
student1.add_marks("English", 87)

print(student1.name)
print(student1.roll_num)
print(student1.percentage)
print(student1.grade)

