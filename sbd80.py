#barrier object
import threading
import time

def worker(barrier, name):
    print(f"{name} is doing some work")
    time.sleep(1)
    print(f"{name} is waiting at the barrier")
    barrier.wait()
    print(f"{name} passed the barrier")

barrier = threading.Barrier(3)

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(barrier, f"Thread-{i}"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
