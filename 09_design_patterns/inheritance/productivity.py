class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print("")


class ManagerRole:
    """This can explode pretty quickly in an unamanageable mess
    But if using multiple inheritance have to manually relolve mro
    MyClass.__mro__ (Method resolution order)
    Try to avoid the diamond problem from the design phase!
    """
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")


class SecretaryRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


class FactoryRole:
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')
