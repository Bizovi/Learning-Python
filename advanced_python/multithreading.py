# mutlithreading.py: concurrency in python
#   1. order of execution
#   2. sharing resources
# threading # only one processor
# parallel programming -> CPU intensive tasks (both have stack trace OS managed)
#   1. multiprocessing (ulimit and tests) (do not share memory!)
#   2. mutlithreading (I/O tasks, wait for e.g. http calls)
#       (shares memory & CPU) on Python Single core
#       IRQ interrupt -> Queue and executes when its time
#       Content switch (move cpu to a process to other)
# next: async programming and streaming (performance comparison)
#   managed by the program
# profiling to see what bocks (process -> forking / decoupling)
#   IO bound (threading/async)
#   CPU bound (multiprocessing)
#   memory bound

import threading
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG,
    format="(%(threadName)-10s)%(message)s")

def work_to_do(val):
    print('Execute work in a thread')
    print('Echo {}'.format(val))
    return

# thread interference
class BankAccount:
    def __init__(self):
        self.bal = 0

    def deposit(self, amt):
        balance = self.bal
        self.bal = balance + amt

    def withdraw(self, amt):
        balance = self.bal
        self.bal = balance - amt

# idea of thread lock on memory location, ops, unlock ... foreach thread
# loss of performace, gain in safety
# mutable: oh well
# immutable: tuple() -> copies + garbage collector (functional programming)
# IOhttp and Flask can support async

class Counter():

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
            return self.value
        finally:
            self.lock.release()
            logging.debug('Release lock')

def worker(c): # outside of the class
    print(i)
    pause = random.random()
    logging.debug('Sleeping {}'.format(pause))
    time.sleep(pause)
    print(c.increment())
    # print(c.increment)
    logging.debug('DONE')


if __name__ == '__main__':
    # second example ----, check out mysql pull connection!
    # pull connection is thread safe!
    counter = Counter()
    for i in range(5):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    # first example ----
    val = "some_text"
    # some kind of context, should be pickable (val,) tuple with one value!
    t = threading.Thread(target=work_to_do, args=(val,))
    t.start() # starts a context
    # waits for them to complete, for DAEMONS (vs processes)
    # parent (first), dies, orphan, OS closes it
    # if we declare the child as daemon/zombie
    # daemon when program runs in background (services) when init.sh and close

    # if you don't put join, it will wait for a default time
    t.join() # if we have more threads, waits for them to finish, barrier

    # if a thread dies, stacktrace & continue ... as finished by join
    # if waits for IO -> infty: IMPORTANCE OF TIMEOUTS, try-except!!

    # create bank account, memory -> 1st thread, try to access same memory
    # trying to make changes (bad), allocate manually, don't care about order
    # without waiting and allocating memory -> extract the max out of threads
    b = BankAccount()
    t1 = threading.Thread(target=b.deposit, args=(100,))
    t2 = threading.Thread(target=b.withdraw, args=(100,))

    # Global interpreter Lock (internal lock)
