#accessing class members outside the class
class empolyee:
    def __init__(self,sal,ag):
        self.salary=sal
        self.age=ag

    def dispaly(self):
        print(f"salary is {self.salary} and age is {self.age}")

e1=empolyee(24000,21)
e2=empolyee(26000,26)
#accessing attribute outside the class
print(e1.salary)  #24000
e1.salary=34000 #updating attribute
print(e1.salary)   #34000