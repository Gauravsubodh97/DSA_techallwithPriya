class student:
    school = 'St. marks school'  # class attribute :- they are defined for all the object

    # default constructor :- this is made by python by itself
    def __init__(self):
        pass

    # parameterized constructor
    def __init__ (self, name, rollno, school):
        self.name = name  # object attribute
        self.roll = rollno  # object attribute
        self.school = school  # object attribute

        # but the same attribute is made in the constructor then the program will give importance
        # to the constructor attribute and the class attribute will be ignored .

    def get_roll(self):
        return self.roll


s1 = student('Ankit', 56, 'st. marys')
print(s1.name, s1.roll, s1.school)
print('the rollnumber is : ',s1.get_roll())

s2 = student('shayam', 80, 'st. Anthonys')
print(s2.name, s2.roll, s2.school)

# s3= student
# print(s3.get_roll())
