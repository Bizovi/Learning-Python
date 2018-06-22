# byte_of_python.py
import os
import io
import pickle

# working with exceptions ----
class ShortInputException(Exception):
    '''User defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('End of file')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' + \
     '{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception was raised')








# working with files ----
os.chdir(os.path.dirname(os.path.abspath(__file__)))

poem = '''
When, after all, the great deluge was over
The seas came back within their coastal lines,
And off the foam of retreating water
Love crept so quietly upon the shore
And vanished into air waiting for her time
To wander for forty lives
'''

with open('poem.txt', 'w') as file:
    file.write(poem)

verse = '''
Even today, some oddish still appear,
Who breathe in this mixture with no fear,
Awaiting no reward, nor grieving,
And thinking they're breathing just like that,
They suddenly fall into the beat
Of the same uneven breathing
'''

with open('poem.txt', 'a') as file:
    file.write(verse)

f = open('poem.txt', 'r')
lengths = []
while True:
    line = f.readline()
    lengths.append(len(line))
    if lengths[-1] == 0 and lengths[-2] == 0:
        break
    print(line)
f.close()

# elementary pickling ----
file_list = 'shoplist.data'
shop_list = ['apple', 'orange', 'juice']

f = open(file_list, 'wb')
pickle.dump(shop_list, f)
f.close()

f = open(file_list, 'rb')
retrieved_list = pickle.load(f)
print(retrieved_list)
# f.close()

# goddamn encodings ----
f = io.open('poem.txt', 'at', encoding='utf-8')
f.write(u"\n by Vladimir Vysotsky")
f.close()

text = io.open('poem.txt', encoding='utf-8').read()
print(text)
