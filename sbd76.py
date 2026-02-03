#lock in multithreading

from threading import*
from time import sleep
mylock=Lock()  #step-1

def task(mylock,msg):
    mylock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
    mylock.release()

t1=Thread(target=task,args=(mylock,'hello world'))
t2=Thread(target=task,args=(mylock,'welcome'))
t1.start()
t2.start()
