#multithreading
#import thread class
from threading import Thread
#create a function containing code to be executed parallaly
def display(n,msg):
    for i in range(n):
        print(msg)
#create new thread here
t1=Thread(target=display,kwargs={'n':4,'msg':"hello world"})
#start the new thread
t1.start()

for i in range(4):
    print("welcome")