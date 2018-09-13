"""
Plecand de la a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
folosind lambda, reduce si map calculati suma pe fiecare lista din interiorul listei a,
rezultatul o sa fie o lista care contine suma numerelor pe fiecare lista.
Din aceasta lista extrageti o alta lista care contin doar numere impare folosind lambda, filter.
"""
from functools import reduce

import numpy as np
a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

# the below works
# sums = list(map(lambda x: np.sum(x) , a))
# [15, 40, 65, 90] as output

sums = list(map(lambda x: reduce(lambda x, y: x + y, x) , a))
print(sums)

filtered = list(filter(lambda x: x % 2, sums))
print(filtered)