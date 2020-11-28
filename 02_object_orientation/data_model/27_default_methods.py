# Chapter 27 of Learning Python: A more realistic example of class
from typing import Optional, Tuple


class Employee:
    """An employee with a job title and salary"""
    def __init__(self, name: str, job: Optional[str] = None, pay: float = 0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def __repr__(self) -> str:
        """Returns a command of how a class is instantiated"""
        return 'Employee({}, job={}, pay={})'.format(self.name, self.job, self.pay)

    def __str__(self) -> str:
        return '''Instance of class person with attributes:
        Name: {},
        Job: {},
        Pay: {}'''.format(self.name, self.job, self.pay)

    def last_name(self) -> str:
        """Splits the first and last name by space and returns last name"""
        return self.name.split(' ')[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Employee):
    """A class Manager inheriting from Employee"""
    def __init__(self, name: str, pay: float) -> None:
        Employee.__init__(self, name, 'manager', pay)

    def give_raise(self, percent: float, bonus: float =0) -> None:
        """ A BAD WAY would be the following:
        self.pay = int(self.pay * (1 + percent + bonus))
        remember to pass instance manually"""
        Employee.give_raise(self, percent + bonus)


class Department:
    """Composite class combined with inheritance"""
    def __init__(self, *args) -> None:
        self.members = list(args)

    def add_member(self, employee: Employee) -> None:
        self.members.append(employee)

    def give_raises(self, percent: float) -> None:
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Manager('Bob Smith', pay=120000)
    sue = Employee('Sue Johnes', job='dev', pay=90000)
    jon = Employee('John Stark', job='qa', pay=70000)
    ana = Employee('Ana Belov', job='ux', pay=80000)

    sue.give_raise(0.15)
    bob.give_raise(0.12, bonus=0.05)
    print(bob.__dict__, '\n', sue.__dict__)

    it = Department(bob, sue, jon)
    it.add_member(ana)
    it.give_raises(0.05)
    it.show_all()
