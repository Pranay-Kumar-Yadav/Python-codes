#callable
class Add(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self):
        print("hello")
a1=Add(10,20)
a1()      #a1.__call__()
print(callable(a1))   