#printing exception information in output

import sys
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
try:
    div=num1/num2
    print("Division is:",div)
except:    
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])   #<class

print("Rest of code")
#ZeroDivisionError: Divison by zero
