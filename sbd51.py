#encapsulation
class finance:
    def __init__(self):
        self.__revenue=100000     #private data
        self.__number_of_sales=114  #private data

    def display(self):
        print(f"revenue is: {self.__revenue} and number of sales: {self.__number_of_sales}")
        self.__revenue=200000
        print(f"revenue is: {self.__revenue} and number of sales: {self.__number_of_sales}")
f1=finance()
f1.display()        