#classes and objects

class person:

    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        print("name: {}, age: {}, height: {}".format(self.name, self.age, self.height))

person1 = person ("mike",30, 180)
print(person1.name)
print(person1.age)
print(person1.height)

person1.name = "henry"
print(person1.name)