# find hcf or gcd
def computeHCF(x,y):
    smaller = 0
    if (x < y):
        smaller = x
    else:
        smaller = y
    hcf = 0
    for i in range(1,smaller + 1): 
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf        

number1 = 12
number2 = 14

print("the HCF of 2numbers {} and {}".format(number1, number2, computeHCF(number1,number2)))