#closures

def outer():
    def inner():
        x=200
        return x 
    return inner

inner=outer()
print(inner())