#decorator
def decor(printer):
    def inner():
        printer()      #existing functionality
        #add new functionality
        print("welcome!")
    return inner
@decor
def printer():
    print("welcome!")
    print("welcome!")

printer()