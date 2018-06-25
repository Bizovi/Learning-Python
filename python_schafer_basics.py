# basics of python from Corey Schafer
import os
import sys
import getpass
import math
import datetime
import calendar
import pytz
import random
import argparse

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

def cyl_vol_fun(r):
    '''
    Function that returns another functions
    Very useful trick in data analysis
    '''
    def volume(h):
        return math.pi * r * r * h
    return volume


if __name__ == '__main__':

    # String formatting and neat tricks --------------------------------
    # ------------------------------------------------------------------
    # name = str(raw_input('What\'s your name'))
    # age  = int(raw_input('What\'s your age'))
    # user = getpass.getuser()
    # password = getpass.getpass()

    # a list is similar 0[index] and 1[index] and class 0.name, 0.age
    person = {'name':'Jenny', 'age':23, 'education':'higher'}
    sentence = 'My name is {name} and I am {age} years old'.format(**person)
    # sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
    print(sentence)

    print('Pi is equal to {:.4f}'.format(math.pi))
    print('1 Mb is equal to {:,.2f} bytes'.format(1000**2))
    my_date = datetime.datetime(2018, 9, 24, 12, 30, 45)
    print('{:%B %d, %Y}'.format(my_date)) # October 01, 2018
    # indicate the placeholders to use the same object, otw out of range err
    print('{0:%B %d, %Y} fell on a {0:%A} and was {0:%j} day of the year'.format(my_date))
    print('\n')
    # bashrc or bash_profile `export DATABASE_NAME=smart`
    name = os.environ.get('DATABASE_NAME')


    # Working with lists and basic data structures ----------------------
    # --------------------------------------------------------------------

    my_list = [x**2 for x in range(10)] # new_list = [expression for x in list]
    print(my_list[0], my_list[1:-2:2], my_list[-1])
    print(my_list[::-1]) # my_list[start:end:step], negative step => Backwards
    # weird behavior of lambdas in list comprehensions
    # a = [(lambda x: x * i) for i in (1, 2)]
    # outer's lambda y=i
    a = [(lambda y: (lambda x: y * x))(i) for i in (1, 2)]
    print('f_1(x=1)={} and f_2(x=1)={}'.format(a[0](1), a[1](1)))

    '''
    Due to the way the Python C-level APIs developed, a lot of built-in
    functions and methods don't actually have names for their arguments,
    i.e. python functions usually allow arbitrary named arguments
    '''

    courses = ['economics', 'mathematics', 'statistics', 'algorithms']
    courses_ext = ['optimization', 'cybernetics']
    # __builtins__
    courses_sort = sorted(courses) # to keep the original list intact
    nums = [1, 5, 3, 32, 1 , 3, 5]
    print(min(nums), max(nums), sum(nums))

    # notice that all these methods are in-place
    courses.append('game theory')
    courses.insert(0, 'ethics')
    courses.extend(courses_ext) # otherwise we end up with list of lists
    print('Removed', courses.pop(), 'from list') # removes the last values, returns it
    courses.reverse()
    print('Reverse list', courses)
    courses.sort(reverse=False)
    print('Sorted list', courses)

    print(courses.index('economics')) # in operator for just checking
    for index, course in enumerate(courses, start=0):
        print(index, course, end='\n')

    course_str = ', '.join(courses)
    course_lfs = course_str.split(', ')
    print(course_str)
    print(course_lfs)

    # tuples are immutable, some more examples of sets
    cs_courses = {'history', 'math', 'physiscs', 'compsci'}
    art_courses = {'history', 'math', 'art', 'design'}
    # set.union() set.difference()
    print('Common courses are', cs_courses.intersection(art_courses))
    print('\n')


    # Dictionaries and key-value pairs (hash maps, associative arrays)
    student = {'name':'John', 'age':25, 'courses':courses}
    student['phone'] = '555-5555-555'
    student['age'] = 26
    student.update({'name':'Johnny', 'age':26, 'phone':'222-2222-222'})
    for key, value in student.items():
        print(key, value)

    print(student.get('phone', 'Not Found')) # None
    # del student['age'] or student.pop('age')


    print(student_info('Math', 'Art', name='John', age=23))
    print(student_info(*['Math', 'Art'], **{'name':'John', 'age':23}))


    # Standard library modules -----------------------------------------
    # ------------------------------------------------------------------

    # print(dir(os)) get methods and attributes
    random_course = random.choice(courses)
    print(random_course)

    today = datetime.date.today()
    print(today)
    print(calendar.isleap(2020))

    print(os.getcwd(), __file__)
    # os.path.dirname, os.path.basename, os.path.split, os.path.exist,
    # os.path.isdir/isfile(), os.path.splittext('/tmp/text.txt')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())
    # print(os.listdir())

    # os.mkdir() # here you create one by one
    # os.makedirs() # can deal with hierarchies
    # os.path.join(os.environ.get('HOME'), 'test.txt')
    mod_time = os.stat('poem.txt').st_mtime
    print(os.stat('poem.txt').st_size,
     datetime.datetime.fromtimestamp(mod_time))

    '''
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print(dirpath)
        print(dirnames)
        print(filenames)
    '''

    # Working with dates
    # naive dates: no timezone / daylight savings details
    # aware dates: enough information of timezones / daylight savings
    d = datetime.date(2018, 6, 25)
    tday = datetime.date.today()
    print(d, tday.year, tday.day, tday.weekday(), tday.isoweekday())
    tdelta = datetime.timedelta(days=7)
    print(tday + tdelta, tday - tdelta)

    # recommended working with utc timezones
    dt = datetime.datetime(2018, 6, 25, 12, 30, 45, tzinfo=pytz.UTC)
    dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
    print(dt_utcnow, dt)

    dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
    ny_tz = pytz.timezone('US/Eastern')
    dt_ny = ny_tz.localize(datetime.datetime.now())
    print(dt_utcnow, dt_ny.strftime('%B %d, %Y'))

    dt_str = 'July 26, 2018'
    dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
    print(dt)

    # for tz in pytz.all_timezones:
    #     print(tz)


    # Handle error and exceptrion ------------------------------------
    # ----------------------------------------------------------------

    try:
        f = open('poem.txt')
        if f.name == 'corrput_file.txt':
            raise Exception # goes to the except Exception line
        # var = bad_var # unexpected error
    except FileNotFoundError as e :
        # be as specific as possible (catch expected errors)
        print('Sorry. This file doesn\'t exist')
        print(e)
    except Exception as e:
        # more general exceptions go last
        print('Sorry, something went wrong')
        print(e)
    else:
        # if try doesn't raise an exception
        print(f.read())
        f.close()
    finally:
        # this code runs anyway, regardless what happens in try-except
        # e.g. close down the databases
        print('Executing Finally...')

    vol_ten = cyl_vol_fun(r=10)
    print('Cylinder volume is', vol_ten(h=5))


    # Argument parsing --------------------------------------------------
    # -------------------------------------------------------------------

    parser = argparse.ArgumentParser()
    parser.add_argument('number1', help='First number')
    parser.add_argument('number2', help='Second number')
    parser.add_argument('operation', help='operation', \
        choices=['add', 'subtract', 'multiply'])
    args = parser.parse_args()

    print(args.number1)
    print(sys.argv)
