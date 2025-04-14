class Student:
    schoolname = 'st. Anthony convent School'
    def __init__(self, name):
        self.name = name
        print("creating new student")


s1 = Student("Gaurav")
print(s1.name)

s2 = Student("Subodh")
print("Student name :-",s2.name,",","School Name:-",s2.schoolname)

