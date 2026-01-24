import cmath

a = float(input("enter value of a : "))
b = float(input("enter value of b : "))
c = float(input("enter value of c : "))

d =(b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("\nRoot 1 : ",root1)
print("\nRoot 2 : ",root2)