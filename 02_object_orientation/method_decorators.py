import logging
import requests

# initialize logger and formatter for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

# attach a file handler
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:

    nr_emp = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: float) -> None:
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay

        # class variables
        Employee.nr_emp += 1
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def fullname(self):
        """Return the full name of an Employee
        @property is a pythonic way of dealing with private values
        will call a setter every time value is assigned
        """
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last  = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@smallville.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        """Altering functionality of method for classwide ..."""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Alternative constructor from a string"""
        first, last, pay = emp_str.split('-')
        pay = int(pay)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """Use the weekday method of dates (1...6) to check if workday"""
        if day.weekday() in range(0, 5):
            return True
        return False

    # special methods and operator overloading
    def __repr__(self):
        """
        Fix printing the vague Employee object when printing out
        Unambiguous representation of object
        Used for Debugging, Logging (Seen by other devs)
        Display smth that you can copy-paste to create the object
        """
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        """
        Readable representation of an object, display to the user
        Has __repr__ as fallback
        """
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        """Add programming language as attribute of programmers"""
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_language = prog_lang


class Manager(Employee):

    def __init__(self,  first, last, pay, employees=None):
        # Never want to pass mutable structures as default arguments
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname(), 'with salary of', emp.pay)


if __name__ == "__main__":
    # part 1: classes and instances
    emp_1 = Employee(first='Jason', last='Bourne', pay=60000)
    # part 2: class variable, classmethods and staticmethods
    emp_3 = Employee.from_string('Clark-Kent-60000')

    # part 3: inheritance
    # print(help(Developer))
    dev_4 = Developer(first='Lana', last='Lang', pay=60000, prog_lang="Python")
    dev_5 = Developer(first='Chloe', last='Lane', pay=70000, prog_lang="Java")

    # part 4: dunder methods and overloading
    # print(repr(emp_1))
    # print('Total salary is', emp_1 + dev_4, '$')
    # print('Jasons fullname is', len(emp_1), 'letters long')
    man_1 = Manager(first='Lex', last='Luthor', pay=100000, \
        employees=[emp_1, dev_4])
    # print(isinstance(man_1, Manager))
    # print(isinstance(man_1, Developer))

    # part 5: property decorator, i.e getter, setter, deleter
    emp_1.first = 'Jim'
    emp_1.fullname = 'Corey Taylor'
    print(emp_1.__dict__)
    print(emp_1.email)

    del emp_1.fullname
    print(emp_1.__dict__)
