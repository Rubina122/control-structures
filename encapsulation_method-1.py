class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        print(self.__salary)

    def set_salary(self,salary,user):
        if user.role=="hr":
            self.__salary=salary
        else:
            raise PermissionError("not allowed")

class user:
    def __init__(self,role,name):
        self.role=role
        self.name=name
emp1=user("ruby","hr")
emp2=user("ruby1","manager")
emp=employee('Ram',10000)



print(emp._employee__salary)



# emp.__salary=2000
# print(emp.salary)
emp._employee__salary=2000
print(emp._employee__salary)
emp.get_salary()

emp.set_salary('hr',1000)