class Student:
    def __init__(self, Name, r_no):
        self.Name = Name
        self.r_no = r_no

    def update_marks(self, marks):
        self.marks = marks

for i in range(3):
    name = input("Name of student {}: ".format(i+1))
    r_no = input("Roll no: ")
    marks = int(input("Marks: "))
    s = Student(name, r_no)
    s.update_marks(marks)
    print("{}'s marks: {}\n".format(s.Name, s.marks))