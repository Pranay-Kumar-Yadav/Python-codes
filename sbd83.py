#genertors suppose you have a list of numbers and you want to filter out even numbers, square the filtered even numbers,and then sum them up.

def filter_even(seq):
    for num in seq:
        if num in seq:
           if num%2==0: 
            yield num

def find_squares(seq):
   for num in seq:
      yield num*num            

numbers = [1,2,3,4,5,6,7,8,9,10]
g = filter_even(numbers)
g1 = find_squares(g)
print(next(g1))
print(next(g1))
print(next(g1))