#super function
class Computer(object):
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
        print("computer class constructor called")

    def display(self):
        print("hello world")

class Mobile(Computer):
    def __init__(self, ram, storage):
        super().display()
        self.mode1='iphone X'
        print("Mobile class construtor called")

Apple=Mobile('8gb','512gb')
print(Apple.__dict__)
              