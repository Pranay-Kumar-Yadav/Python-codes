#overloading > operator
class Hotel:
    def __init__(self,name,fare):
        self.name=name
        self.fare=fare


    def __gt__(self,other):  #(h1,h2)
       return self.fare>other.fare     #h1.fare.h2.fare

h1=Hotel('Taj Hotel',20000)
h2=Hotel('panchrantna',10000) 

print(h1>h2)   #true