# concurrency_problem.py
import multiprocessing
import threading
import time

nr_repeat = 10

def complex_operation():
    a = []
    for x in range(999999):
        a.append(x)
    return None


if __name__ == "__main__":
    t1 = time.time()
    for _ in range(nr_repeat):
        complex_operation()
    print(time.time() - t1)


    tm = time.time()
    # CPU intensive tasks
    pool = multiprocessing.Pool(processes=nr_repeat)
    for _ in range(nr_repeat):
        results = pool.map(complex_operation, ())
    print(time.time() - tm)


    # Overhead from GLI and context swithching
    # In python multithreading only for IO
    tt = time.time()
    threads = []
    for _ in range(nr_repeat):
        t = threads.append(threading.Thread(target=complex_operation))

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    print(time.time() - tt)
