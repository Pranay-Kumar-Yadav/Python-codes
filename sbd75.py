#join method 
from threading import Thread
from time import sleep
def upload():
    print("Uploading starts")
    sleep(3)
    print("video uploaded")

def notification():
    print("sending notification to subscribers code")

t1=Thread(target=upload)
t2=Thread(target=notification)
t1.start()
t2.start()
#main thread code 
for i in range(4):
    print("hello")    
