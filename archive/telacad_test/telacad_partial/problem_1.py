import copy
"""Fix the issues with the script"""

a = [[1,2,3,4],[4,5,6,7]]
# make a deep copy to solve the issue
b = copy.deepcopy(a)

print("a and b before modify")
print(a)
print(b)

a[0][1]=10

print("a and b after modify. b was obtain as a copy of a")

print(a)
print(b)

