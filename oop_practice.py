## oop is not obeject. oop is blueprint.

# class Dog:
#     animal_kind = "canine"
#
#     def bark(self):
#         return "woof"

class Student:
    def __init__(self, name, english, math, science):
        self.name = name
        self.english = english
        self.math =math
        self.science = science
    def get_sum(self):
        return self.english + self.math +  self.science
    def get_average(self):
        return self.get_sum()/3

yoonhee = Student("Yoonhee", 90, 80, 95)
luis = Student("Luis", 95, 90, 100)
james = Student("James", 100, 90, 95)

print(yoonhee.get_sum())
print(luis.get_sum())
print(james.get_sum())

print(round(yoonhee.get_average()),2)
print(round(luis.get_average()),2)
print(round(james.get_average()),2)


