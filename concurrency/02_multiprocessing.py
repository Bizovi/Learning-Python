# concurrency.py
# Gil individual for each process, sidesteps gil, synchronization
# higher memory footprint (have to specify it), expensive context switches
import multiprocessing

def work_to_do(val):
    print("some work in thread")
    print("echo: {}".format(val))
    return

def do_work(data):
    return data ** 2

# Pool, blocant
def start_process():
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
