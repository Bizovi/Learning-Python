from typing import List
import multiprocessing

"""An example of multiprocess:
* GIL is individual for each process, synchronization
* Processes do not share memory, which is what we often want
* Higher memory footprint
* Expensive context switching
"""

def work_to_do(val: str) -> None:
    print("some work in thread")
    print(f"echo: {val}")
    return

def do_work(data: List) -> List:
    return data ** 2

def start_process():
    """Helper function to see the current process name"""
    print('Starting', multiprocessing.current_process().name)


if __name__ == "__main__":
    val = "text"
    t = multiprocessing.Process(target=work_to_do, args=(val,))
    t.start()
    t.join()

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size,
        initializer=start_process) # kind of semaphore
    inputs = list(range(10))
    
    # interesting to look at map-async: blocking!
    outputs = pool.map(do_work, inputs)

    print('Outputs:', outputs)
    pool.close()
