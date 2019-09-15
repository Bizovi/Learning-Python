# ctx.py
# still buggy, need to work on it
from sqlite3 import connect # context manager itself
'''
Metaphor: clear and unambiguous -> suggests sequencing
    SETUP action
    TEAR DOWN action
In a nutshell:
# x = ctx().__enter__()
# try:
#     pass
# finally:
#     x.__exit__()
'''

def temptable(cur):
    self.cur.execute('create table points(x int, y int)')
    yield
    self.cur.execute('drop table points')



class contextManager:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        print('__enter__')
        # don't need the previous table
        self.cur.execute('drop table points')
        self.cur.execute('create table points(x int, y int)')

    def __exit__(self, *args):
        print('__exit__')
        self.cur.execute('drop table points')

if __name__ == '__main__':
    with connect('test.db') as conn: # with temptable(cur)
        csr = conn.cursor()
        with contextManager(csr):
            # csr.execute('create table points(x int, y int)')
            csr.execute('insert into points (x, y) values(1, 1)')
            csr.execute('insert into points (x, y) values(1, 2)')
            csr.execute('insert into points (x, y) values(2, 1)')
            csr.execute('insert into points (x, y) values(2, 2)')
            for row in csr.execute('select x, y from points'):
                print(row)
            for row in csr.execute('select sum(x + y) from points'):
                print(row)
            # csr.execute('drop table points')

print(row)
