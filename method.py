class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks    #instance variable

    #Instance Method
    def display_info(self):
        return f"Name: {self.name}, Marks:{self.marks}"
    
    #Creating ojects
s1= Student("Heena",85)
s2= Student("Meera",90)

print(s1.display_info())
print(s2.display_info())