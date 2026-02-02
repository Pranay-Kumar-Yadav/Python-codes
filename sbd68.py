#decorator
class decorator(object):
    def __init__(self,func):
        self.function=func

    def __call__(self,a,b):
        result=self.function(a,b)
        return result**2

def add(a,b):
    return a+b
add=decorator(add)

print(add(1,2))        #add.__call__(a,b)