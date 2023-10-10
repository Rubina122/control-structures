class student:
    school="chaitanya"
    branchs="anantapur"
    total_subjects=6
    def __init__(self,first_name,last_name,branch,reg_no):
        self.first_name=first_name
        self.last_name=last_name
        self.branch=branch
        self.reg_no=reg_no
        self.active=True
        self.percantage=None
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def leave_school(self):
        self.active=False
    def Join_school(self):
        self.active=True
    def get_active_status(self):
        return self.active
    @classmethod
    def set_school_name(cls,name):
        cls.school=name

    @classmethod
    def set_branch_name(cls,branch):
        cls.branchs=branch

    @staticmethod
    def compute_percentage(total,subject_count):
        return total/subject_count

    def set_percent(self,total_score):
        percent=self.set_percent(total_score,self.total_subjects)
        self.percantage=percent


s1=student("ram","ret","mpc",123 )
# print(s1)
# print(s1.__dict__)

# print(s1.first_name + " "+s1.last_name)
# print(s1.fullname())
print(s1.get_active_status())
s1.leave_school()
print(s1.get_active_status())
s1.Join_school()
print(s1.get_active_status())

print(s1.school)
print(s1.set_school_name("Sri Chaitanya"))
print(student)
print(s1.school)

# print(s1.branchs)
# s1.set_branch_name("Goa")
# print(s1.branchs)

print(s1.school)
print(student.school)

print(s1.percantage)
s1.set_percent(300)
print(s1.percantage)
