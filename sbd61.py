#setter and getter method
class Employee:
    def setName(self,nm):     #setter method
        self.name=nm

    def getName(self):        #getter method
        print("the name is:",self.name)

e1=Employee()
e2=Employee()

e1.setName(input("enter the name:"))
e2.setName(input("enter the name:"))
print("e1 object is:",e1.__dict__)
print("e2 object is:",e2.__dict__)
e1.getName()
e2.getName()
