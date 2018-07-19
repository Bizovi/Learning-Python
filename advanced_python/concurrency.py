# concurrency.py
# thread queue (put(), get(), task_done() # fully processed, join())
import threading
from queue import Queue # thread safe (communication between queues)
import time

def example_job(worker):
    time.sleep(2)
    print(threading.current_thread().name, worker)

q = Queue()
def consumer():
    while True:
        worker = q.get()
        example_job(worker)
        q.task_done()


if __name__ == "__main__":
    # get blocks until the next put in the queue
    # a producer is rarely a single for (many put many get)
    # consumer
    for x in range(10):
        t = threading.Thread(target=consumer
        t.daemon = True # such that it won't stop
        t.start()

    # if before we passed arguments, now it's too much
    # have to use a queue
    start = time.time()
    # 20 jobs assigned
    # producer
    for worker in range(20):
        q.put(worker)

    # outside put!
    q.join() # wait until thread terminates
    print('Entire job took', time.time() - start)
