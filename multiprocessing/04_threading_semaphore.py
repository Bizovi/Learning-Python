# concurrency.py
# thread queue (put(), get(), task_done() # fully processed, join())
import threading
from queue import Queue # thread safe (communication between queues)
import time

semaphore = threading.BoundedSemaphore(5)
# semaphores ----
# debug with login or print!!
def worker():
    with semaphore:
        print(threading.current_thread().getName(), 'Starting')
        time.sleep(2)
        print(threading.current_thread().getName(), 'Existing')

# SEMAPHORE: how many threads can use a function? -----
# e.g. bunch of servers rolling, can't use all at once (by 10s wo join)
# at a given time only 10 threads action on it

# semaphore = threading.Semaphore()
# semaphore.acquire()
# ... access resources e.g. 6 installing operations
# semaphore.release

# Do not be specific on Except clause!!
# -> threads breaks, semaphore releases, threads die after app ..
# can lead to the server crash .. (curious case)

if __name__ == "__main__":
    threads = []
    for i in range(7):
        t = threading.Thread(name="worker-name: " + str(i), target=worker)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
