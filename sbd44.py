#synchronizing threading
import threading
import time

x = 8192

lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("reached the maximum!")
    lock.release()

def ha1ve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
        print("Reached the minimum!")
        lock.release()

t1 = threading.Thread(target=ha1ve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()