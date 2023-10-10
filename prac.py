# class A:
#     pass
# obj=A()
# print(str(obj))

# class B:
#     def __new__(cls,name):
#         print(f'Creating a new {cls.__name__} object')
#         obj=object.__new__(cls)
#         return obj
#     def __init__(self,name):
#         print(f'intialise the object')
#         self.name=name
#
#     # def __str__(self):
#     #     return f"{self.name} {self.age}"
#     #
#     # def __repr__(self):
#     #     return  f"{self.name} {self.age}"
#
# obj=B('A')
# print(obj)

# class Basket:
#     def __init__(self,items):
#         self.items=items
#     def __add__(self,other_basket):
#         return Basket(self.items+other_basket.items)
# my_basket=Basket(['Banana','Apple','Juice'])
# other_basket=Basket(['Mango'])
#
# full_basket=my_basket+other_basket
# print(full_basket.items)


# __add__ : Returns a new object that represent the addition of two objects
# class Basket:
#     def __init__(self,items):
#         self.items=items
#     def __add__(self, new):
#         return Basket(self.items+new.items)
# my_basket=Basket(['Banana','Apple','Juice'])
# other_basket=Basket(['Mango'])
#
# full_basket=my_basket+other_basket
# print(full_basket.items)



# __Sub__ : Represents a new object that represent the difference of two objects
# class Basket:
#     def __init__(self,goods):
#         self.goods=goods
#     def __sub__(self, new):
#         return Basket(self.goods-new.goods)
# my_basket=Basket({'Banana','Apple','Juice'})
# other_basket=Basket({'Banana'})
#
# updated=my_basket-other_basket
# print(updated.goods)


# class A:                         # __new__: It is special method,Triggered when object is Created
#     def __new__(cls,name):
#         print(f'Creating a new object')
#         obj=object.__new__(cls)
#         return obj
#     def __init__(self,name):
#         print(f'Intializing a new object')
#         self.name=name
#
#
#
# obj=A('l')
# print(obj.name)

# class Book:                       # it is repersention of Class and Object
#     def __init__(self,Book_name):
#         self.Book_name=Book_name
#     def __str__(self):
#         return f"{self.Book_name}"
#     def __repr__(self):
#         return f"Book('{self.Book_name}')"
# Book1=Book("Author")
# print(str(Book1))
# print(repr(Book1))





# class A:
#     def __init__(self,name):
#         self.name=name
# class B(A):
#     def __init__(self,age):
#         self.age=age
#
#
# obj=B('apple',20)
# print(obj.age)



# class person:
#     def __init__(self,fn,ln,age):
#         self.fn=fn
#         self.ln=ln
#         self.age=str(age)
#     def fullname(self):
#         print(self.fn+self.ln)
# class employee(person):
#     def set_company_name(self,company_name):
#         self.company_name=company_name
#     def set_company_adress(self,adress):
#         self.adress=adress
# class manager(employee):
#     def set_role(self,role):
#         self.role = role
# class security(employee):
#     def set_roles(self,role):
#         self.role=role
#
#
# emp1=employee('Ram','naresh',20)
# print(emp1.__dict__)
# emp1.fullname()
# emp1.set_company_name("cgi")
# emp1.set_company_adress("hyd")
# print(emp1.__dict__)


# emp=manager('Ram','Suresh',50)
# print(emp.__dict__)
# emp.set_role('I am a Manager')
# print(emp.__dict__)
#
# emp2=security('ram','rani',500)
# emp2.set_roles('I am a Security')
# emp2.set_company_adress('Hyd')
# emp2.set_company_name('cgi')
# emp2.set_roles('I am a Security')
# print(emp2.__dict__)





