#destructor
import time
class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal

    def display(self):
        print(f"name is {self.name}\nsalary is:{self.salary}")

    #defining destructor
    def __del__(self):
        print("destructor is called")

e1=Employee("kkkkk",50000)
e1.display()
e2=e1

del e1

time.sleep(5)