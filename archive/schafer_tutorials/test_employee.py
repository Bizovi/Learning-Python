# test the classes in python_oop.py
from python_oop import Employee
import unittest
from unittest.mock import patch # decorator or context manager
# mock an object during the test, restored after test is range

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Working with classes rather than instances
        Useful for something done only once, e.g. in DB reading
        '''
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        '''Runs its code before every test'''
        self.p1 = Employee(first='Jason', last='Bourne', pay=90000)
        self.p2 = Employee(first='Lex', last='Luthor', pay=80000)

    def tearDown(self):
        '''Runs its code after every test'''
        pass

    def test_email(self):
        self.assertEqual(self.p1.email, 'Jason.Bourne@smallville.com')
        self.assertEqual(self.p2.email, 'Lex.Luthor@smallville.com')

        self.p1.first = 'Vasiliy'
        self.p2.first = 'Martin'
        self.assertEqual(self.p1.email, 'Vasiliy.Bourne@smallville.com')
        self.assertEqual(self.p2.email, 'Martin.Luthor@smallville.com')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname, 'Jason Bourne')
        self.assertEqual(self.p2.fullname, 'Lex Luthor')

        self.p1.first = 'Vasiliy'
        self.p2.first = 'Martin'
        self.assertEqual(self.p1.fullname, 'Vasiliy Bourne')
        self.assertEqual(self.p2.fullname, 'Martin Luthor')

    def test_apply_raise(self):
        self.p1.apply_raise()
        self.p2.apply_raise()

        self.assertEqual(self.p1.pay, 93600)
        self.assertEqual(self.p2.pay, 83200)

    def test_monthly_schedule(self):
        '''For things outside our control, e.g. when website is down,
        we could use mocking, instead of going to the website'''
        with patch('python_oop.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.p1.monthly_schedule('May')
            # make sure it was called with the correct URL
            mocked_get.assert_called_with('http://company.com/Bourne/May')
            # make sure it returned the correct test
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.p2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Luthor/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
