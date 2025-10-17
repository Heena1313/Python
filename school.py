class student:
    school_name= "ABC School"
    
    def __init__(self,name):
        self.name=name

     #Class method
    @classmethod
    def change_school(cls,new_name):
        cls.school_name=new_name

#Using class method
student.change_school("XYZ School")

print(student.school_name)
        