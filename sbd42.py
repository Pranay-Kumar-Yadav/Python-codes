# inhertiance
class person:

    def __init__(self, name, age, height) :
        self.name = name
        self.age = age
        self.height = height

    def __str__(self) :
        return "name: {}, age: {}, height: {}".format(self.name, self.age, self.height)
    
    def get_older(years) :
        self.age += years

class worker(person) :

    def __init__(self, name, age, height, salary) :
        super(worker, self).__init__(name, age, height)
        self.salary = salary
    
    def __str__(self):
        text = super(worker, self).__str__()
        text += ", salary {}".format(self.salary)
        return text
    
    def calc_yearly_salary(self):
        return self.salary *12
    
worker1 = worker("henry", 40, 176, 3000)
print(worker1)
print(worker1.calc_yearly_salary() )