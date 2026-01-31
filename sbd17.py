# prime or not
num = int(input("enter a number :"))
count = 0
fact = 1
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print(num,"is prime number")
else:
    print(num,"is not prime number")