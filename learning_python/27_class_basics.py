# Chapter 28 of Learning Python: A more realistic example of class

class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __repr__(self):
        return 'Person({}, job={}, pay={})'.format(self.name, self.job, self.pay)

    def __str__(self):
        return '''Instance of class person with attributes:
        Name: {},
        Job: {},
        Pay: {}'''.format(self.name, self.job, self.pay)

    def last_name(self):
        return self.name.split(' ')[-1]

    # @rangetest(percent=(0.0, 1.0))
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def give_raise(self, percent, bonus=0):
        ''' A BAD WAY would be the following:
        self.pay = int(self.pay * (1 + percent + bonus))
        remember to pass instance manually'''
        Person.give_raise(self, percent + bonus)


class Department:
    '''Composite class combined with inheritance'''
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Manager('Bob Smith', pay=120000)
    sue = Person('Sue Johnes', job='dev', pay=90000)
    jon = Person('John Stark', job='qa',  pay=70000)
    ana = Person('Ana Belov',  job='ux',  pay=80000)
    sue.give_raise(0.15)
    bob.give_raise(0.12, bonus=0.05)
    print(bob.__dict__, '\n', sue.__dict__)

    it = Department(bob, sue, jon)
    it.add_member(ana)
    it.give_raises(0.05)
    it.show_all()

    # Stopped at page 840 of Learning Python. Continue tomorrow
