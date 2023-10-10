
# __repr__:
# It is a Special magic method used to represent class object within a string
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'g{self.name},{self.age}'

    def __repr__(self):
        return f'Person("{self.name},{self.age}")'



per = Person("John", 20)
print(str(per))
print(repr(per))





