#classes and objects

class person:

    amount = 0

    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height = height
        person.amount += 1

    def __del__(self):
        person.amount -= 1
    
    def __str__(self):
        return "name: {}, age: {}, height: {}".format(self.name, self.age, self.height)
    def get_order(years):
        self.age += years
    

person1 = person ("mike",30, 180)
print(person1)

person2 = person("sara", 40, 176)

print(person.amount)