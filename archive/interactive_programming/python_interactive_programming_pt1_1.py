# Rock Paper Scissors Lisard Spock
import random

'''
Payoffs from Row perspective
    Sc  Pa  Ro  Li  Sp
Sc  *   -   -   -   -
Pa  -1  *   -   -   -
Ro  +1  -1  *   -   -
Li  -1  +1  -1  *   -
Sp  +1  -1  +1  -1  *
'''

# note that with a more modern approach one could use even pandas for mapping
def name_to_number(name):
    '''
    Helper function to convert from name to numbers
    '''
    name = name.lower()
    if name == 'rock':
        number = 0
    elif name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print('Wrong name of action')
    return number

def number_to_name(number):
    '''
    Helper function to convert from numbers to names
    '''
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print('Wrong number of action')
    return name


def game(player_choice):
    '''
    A single line representing clock logic replaces 25 cases
    (i - j) modulo 5 in [1, 2] i wins
    (i - j) modulo 5 in [3, 4] j wins
    '''
    # Nicities and conversions
    player_choice = player_choice.lower()
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    print('Player chooses {}'.format(player_choice))
    print('Computer chooses {}'.format(comp_name))

    # Calculate the winner: basically whole script is a wrapper for this line
    test_stat = (comp_number - player_number) % 5
    if test_stat == 0:
        print('Player and computer tie!')
    elif test_stat in [1, 2]:
        print("Computer wins")
    elif test_stat in [3, 4]:
        print("User wins")
    else:
        print('Some other kind of error')


if __name__ == '__main__':
    # test the game
    print(game('rock'), game('spock'), game('paper'), game('lizard'), game('scissors'))
