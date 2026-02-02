#access members of one class inside another class

class Employee:
    def __init__(self,eid,name,sal):
        self.emp_id=eid
        self.emp_name=name
        self.emp_salary=sal
    def display(self):
        print("Employee id:",self.emp_id)
        print("employee name:",self.emp_name)
        print("empolyee salary:",self.emp_salary)
        
class Changes:
    @staticmethod
    def increment(obj):
        obj.emp_salary=obj.emp_salary+2000
        obj.display()

e1=Employee(101,'kkkkk',50000)
Changes.increment(e1)   
e1.display()             