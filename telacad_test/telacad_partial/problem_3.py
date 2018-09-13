from functools import reduce
import time
import threading
import multiprocessing

""""
Use threading and multiprocessing to solve performance issues
"""

start = time.perf_counter()
t = range(99999, 100003)
a = []

for i in t:
    v = 1
    for z in range(1,i+1):
        v = v*z
    a.append(v)
end = time.perf_counter()

print("Factorial de numerele respective au fost generate in {}".format(end-start))

start = time.perf_counter()
for i in zip(t,a):
   with open(str(i[0]) + ".txt", 'w') as file:
       file.write(str(i[1]))
end = time.perf_counter()

print("Numerele factorial generate au fost scrise in fisiere in {}".format(end-start))