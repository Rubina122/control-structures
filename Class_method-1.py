# class Student:
#     def stdinfo(self):
#         self.name='Momin'
#         self.place='Anantapur'
#         self.College="Cit"
#         self.Branch='B.E.Mechanical Engineering'
#         self.Passing_Year='2019'
#         print(f"hi i am {self.name} from{self.place} ,Persued {self.Branch},from {self.College}")
#
#
# obj=Student()
# obj.stdinfo()





# class pen:
#     def Pen_Pro(self):
#         self.pen_name='Reynolds'
#         self.Colour='Blue'
#         self.type='Ball point'
#         self.price=20
#         print(f"Pen name is {self.pen_name},wtih ink {self.Colour},and type is {self.type} ,cost rs.{self.price}")
# obj=pen()
# obj.Pen_Pro()


# class state():
#     def state_info(self):
#         self.state='AndhraPradesh'
#         self.District_Name='Anantapur'
#         self.population=123456
#         print(self.state)
#         print(self.District_Name)
#         print(self.population)
# obj=state()
# obj.state_info()

#School
#Student

#-----school-----------------------------
#Class Variable
#Md
#Principal
#School
#Location

# Object Variable/instance Variable
# name
# id
# father_name
# standard
# section

# class Student:
#     School='Lrg'
#     Md='xyz'
#     principal='abc'
#     location='Anantapur'
# s1=Student()
# s1.name='ram'
# s1.gender='male'
# s1.id=2
# s1.section='Mpc'
# print(s1.section)
# print(s1.Md)

# class student:
#     school = 'Lrg'
#     Md = 'xyz'
#     principal = 'abc'
#     location = 'Anantapur'
#     def __init__(self,id,name,father_name,standard,section):
#         self.id=id
#         self.name=name
#         self.father_name=father_name
#         self.standard=standard
#
# student1=student(1,"Phyton","Guido Van Rossum","1","A-Section")
# student2=student(2,"Java","James Gosling","2","B-Section")
# student3=student(3,"C","Dennis Ritchie","3","A-Section")
# student4=student(4,"Javascript","Brenden Eich","1","A-Section")
# print(student1.id,student1.name,student1.father_name,student1.standard,student.school)
# print(student2.id,student2.name,student2.father_name,student2.standard,student.school)
# print(student3.id,student3.name,student3.father_name,student3.standard,student.school)
# print(student4.id,student4.name,student4.father_name,student4.standard,student.school)


# class school:
#     board='Ap State Board'
#     mode='English Medium'
#     state='AndhraPradesh'
#     def __init__(self,principal_name,school_name,class_name,student_name,teacher_name,location):
#         self.principal_name=principal_name
#         self.school_name=school_name
#         self.class_name=class_name
#         self.student_name=student_name
#         self.teacher_name=teacher_name
#         self.location=location
# school1=school("Alpha","Minerva High School","Science","ken","Gill","Old Town")
# school2=school("Beta","MGM High School","English","Len","Suresh","New Town")
# print(school1)
# print(school1.student_name,school1.school_name,school.mode,school.board,school.state)
# print(school2.student_name,school2.school_name,school.mode,school.board,school.state)