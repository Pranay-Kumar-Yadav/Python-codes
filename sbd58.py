#instance method
class Student:
    def __init__(self,nm,m):
        self.name=nm
        self.marks=m

    def display(self):
        print(self.name,self.marks)
    
    def change_data(self):
        self.name=input("enter new name:")
        self.marks=int(input("enter new marks:"))

std1=Student('Akshay',89)
std2=Student('raj',89)
std3=Student('Jay',89)

std2.change_data()
print(std2.__dict__)