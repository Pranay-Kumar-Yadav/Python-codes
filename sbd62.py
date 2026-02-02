#static method
class Bank:
    bank_name='BOI'
    rate_of_interest=12.25
    @staticmethod
    def simple_interest(prin,n):
        si=(prin*n*Bank.rate_of_interest)/100
        print(si)

prin=float(input("enter principle amount:"))
n=int(input("enter number of year:"))
Bank.simple_interest(prin,n)        