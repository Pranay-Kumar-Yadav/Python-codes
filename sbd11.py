# a string is palindrome or not
num = input("enter a number")
if num == num[::-1]:
    print("yes its a palindrome")
else:
    print("no its not a palindrome")