import multiprocessing
import threading
import time

"""The purpose of this script is to emphasize the difference
between threading and multiprocessing and the overhead of 
context switching

Multiprocessing - for CPU intensive tasks
Threads - for I/O task (although we have `asyncio`)
    Overhead from GLI and context swithching
"""

nr_repeat = 10

def complex_operation():
    """An operation which takes some time"""
    a = []
    for x in range(999999):
        a.append(x)
    return None


if __name__ == "__main__":
    # naive implementation running time: 0.84s
    t1 = time.time()
    for _ in range(nr_repeat):
        complex_operation()
    print(time.time() - t1)

    # Multiprocessing implementation running time: 0.02s
    tm = time.time()
    pool = multiprocessing.Pool(processes=nr_repeat)
    for _ in range(nr_repeat):
        results = pool.map(complex_operation, ())
    print(time.time() - tm)

    # Multithreading implementation: 0.85
    tt = time.time()
    threads = []
    for _ in range(nr_repeat):
        t = threads.append(threading.Thread(target=complex_operation))

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    print(time.time() - tt)
