# the nitty gritty of error handling and exceptions

# allows for the program to continue.
# Dangerous in threads, have to assure you catch all
# Semaphores and barriers
# When modules have different names based on the version

# Beautiful soup vs XPATH (more powerful)

try:
    import _foo
except ImportError:
    print('Module could not be found')

try:
    print(1 / 0)
except ZeroDivisionError:
    print('Can\'t divide by zero')
