'''
Texts, lists and tables together are called trains. […]
The FOR command also works generically on trains.
CONTAINER: list, tuple, collections.deque (hold references to objects)
FLAT: str, bytes, bytearray, memoryview, array.array
'''

# list comprehensions as an introduction to ``generator expressions``
# its sole purpose is to build a new list!
symbols = '$¢£¥€¤' # want unicode codepoints
codes = [ord(symbol) for symbol in symbols]
print(codes)
