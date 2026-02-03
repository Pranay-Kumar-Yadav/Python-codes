#timer object
import threading

def say_hello():
    print("Hello after 5 seconds!")

timer = threading.Timer(5.0, say_hello)
timer.start()
