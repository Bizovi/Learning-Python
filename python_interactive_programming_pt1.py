# python interactive programming coursera
# import numpy as np
import math
import random

'''
There are 52805280 feet in a mile.
Write a Python statement that calculates and prints the number of feet
in 1313 miles
'''
def feet_to_mile(feet):
    multiplier = 5280
    return feet * multiplier

'''
Write a Python statement that calculates and prints the number of seconds
in 7 hours, 21 minutes and 37 seconds
'''
def to_seconds(seconds, minutes=None, hours=None):
    if hours==None or minutes==None:
        hours = 0
        minutes = 0
    return 3600 * hours + 60 * minutes + seconds

'''
Perimeter of the rectangle 4 by 7 inches
'''
def rect_perimeter(width, height):
    if width==0 or height==0:
        print('Width or length should be nonzero')
    return width * height

'''
Calculate the circumference of a circle
p = 2 \pi r
'''
def circumference(radius):
    if radius==0:
        print('Radius should be nonzero')
    return 2 * radius * math.pi

'''
Calculate the area of the circle
S = \pi * r^2
'''
def circle_area(radius):
    if radius==0:
        print('Radius should be nonzero')
    return math.pi * radius ** 2

'''
Calculate the future value of the deposit at yearly rate of r percent
for y years
p * (1 + 0.01 * r)^y
'''
def future_value(amount, years, rate):
    return amount * (1 + 0.01*rate) ** years

def dist_eu(x, y):
    '''
    The euclidian distance between two points
    Is elementary with numpy, but interesting exercise with base python
    IN: two lists which represent multidimensional data points
    OUT: the distance
    '''
    if len(x) != len(y):
        print('Points should have same number of dimensions')

    sq_dist = 0
    for element in range(len(x)):
        sq_diff = (x[element] - y[element]) ** 2
        sq_dist = sq_dist + sq_diff
    dist = math.sqrt(sq_dist) # or just use ** 0.5
    return  dist

def triangle_area(coord_a, coord_b, coord_c):
    if len(coord_a) != 2 or len(coord_b) != 2 or len(coord_c) != 2:
        print('We\'re not working with hypertriangles here')
    # calculate edge length
    a = dist_eu(coord_a, coord_b)
    b = dist_eu(coord_b, coord_c)
    c = dist_eu(coord_c, coord_a)
    # apply the Heron formula
    s = 0.5*(a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

'''
Write a Python function
print_digits that takes an integer number in the range [0,100)
It prints the message "The tens digit is %, and the ones digit is %"
'''
def print_digits(x):
    if x >= 100 or x < 0:
        print('A number in range [0, 100) needed')
    else:
        tens = x // 10
        ones = x % 10
        message = 'The tens digit is {} and the ones digit is {}'.format(str(tens), str(ones))
        print(message)

'''
Powerball: 6 numbers drawn at random
Players can purchase a lottery ticket with a specific number combination and,
if the number on the ticket matches the numbers generated in a random drawing,
the player wins a massive jackpot.
'''
def powerball():
    # random integers in range [1, 60), allowing for duplicates
    draws = []
    while len(draws) != 6:
        x = random.randrange(0, 60)
        if x not in draws:
            draws.append(x)

    # powerball number in range [1, 36)
    powerball = random.randrange(1, 36)
    print('Today\'s numbers are {}, {}, {}, {}, {}, {}. The powerball number is {}'.format(*draws, powerball))

'''
Pig latin game:
If first letter consonant append consonant + 'ay': 'pig' -> 'igpay'
If first letter vowel append 'way' to the end of the word: 'owl' -> 'owlway'
'''
def pig_latin(word):
    word = word.lower()
    if word[0] not in ['a', 'e', 'i', 'o', 'u']:
        return word[1:len(word)] + 'ay'
    else:
        return word + 'way'

'''
IN: coefficients of ax^2 + bx + c = 0
OUT: solution
This would be more neat with vectorization
'''
def quadratic_eq(a, b, c):
    determinant = b ** 2 - 4*a*c
    if determinant >= 0:
        solution_1 = (-b + math.sqrt(determinant)) / 2*a
        solution_2 = (-b - math.sqrt(determinant)) / 2*a
    else:
        solution_1 = b / (2*a) + complex(0, 1* math.sqrt(abs(determinant))) / (2*a)
        solution_2 = b / (2*a) - complex(0, 1* math.sqrt(abs(determinant))) / (2*a)
    return [solution_1, solution_2]

if __name__ == '__main__':
    print('Number of feet in 13 miles is', feet_to_mile(feet=13), 'ft')
    print('Number of seconds is', to_seconds(seconds = 37, minutes = 21, hours=7), 'sec')
    print('Perimeter of the rectangle is', rect_perimeter(4, 7), 'in')
    print('Circumference of the circle is', round(circumference(8),2), 'in')
    print('Area of the circle is', round(circle_area(8)), 'sq. in')
    print('Future value is', round(future_value(amount=1000, rate=7, years=10), 2), '$')

    # note that the following function also works with tuples
    print('The distance', dist_eu(x=[2, 2], y=[5,6]), 'u.')

    # expected result of the below is (3 ** 2) / 2 = 4.5
    print('The triangle area is',
        round(triangle_area(coord_a=[0, 0], coord_b=[0,3], coord_c=[3,0]), 2), 'sq. in')
    print(print_digits(57))
    powerball()

    # conditionals
    print(pig_latin('Owl'), pig_latin('piG'))
    # expected solution [2, 1]
    print('The solution to q.eq. is', quadratic_eq(a=1, b=-3, c=2))
    # expected solution to following 1/6 +/- i*sqrt(17)/6
    print('The solution to q.eq. is', quadratic_eq(a=6, b=-2, c=3))
