# calculate the area of triangle

a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

#calculare the semi-perimeter
s = (a + b + c) / 2

#calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("the area of the triangle is %0.2f" % area)