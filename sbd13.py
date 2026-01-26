#reverse a number
num=int(input("enter a number:"))
rev=0
while num!=0:
    dig=num%10
    rev=(rev*10)+dig
    num=num//10
    print("reverse of number is:",rev)