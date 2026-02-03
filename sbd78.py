#daemon thread
import threading
import time

def background_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

# Create daemon thread
t = threading.Thread(target=background_task, daemon=True)
t.start()

print("Main thread sleeping...")
time.sleep(3)
print("Main thread exiting")
