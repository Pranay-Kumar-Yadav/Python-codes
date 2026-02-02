#exception handling
num1=int(input("enter first number:"))
num2=int(input("enter second number"))
try:
    div=num1/num2
    print(div)
except:
    print("something went wrong")
else:
    print("an exception didn't occur")
finally:
    print("always executed")
print("rest of code")