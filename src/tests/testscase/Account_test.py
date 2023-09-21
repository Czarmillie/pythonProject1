import unittest

from tests.Account import Account
from tests import InsufficientAmountException

def get_balance():
    pass

class TestAccountFunction(unittest.TestCase):

    def test_that_account_exists(self):
        self.account = Account("Daniel", "Olanrewaju", 2, 1111)
        self.assertTrue(self.account)

    def test_that_amount_can_be_deposited(self):
        self.account = Account("Daniel", "Olanrewaju", 2, 1111)
        self.account.deposit(20000)
        self.account.get_balance(2)
        self.assertEqual(self.account.get_balance(2), 20000)

    def test_that_money_can_be_withdrawn(self):
        self.account = Account("Daniel", "Olanrewaju", 2, 1111)
        self.account.deposit(20000)
        self.account.withdraw(10000, 2)
        self.assertEqual(self.account.get_balance(2), 10000)

    def test_to_withdraw_twice(self):
        self.account = Account("Daniel", "Olanrewaju", 2, 1111)
        self.account.deposit(20000)
        self.account.withdraw(5000, 2)
        self.account.withdraw(8000, 2)
        self.assertEqual(self.account.get_balance(2), 7000)

    def test_to_withdraw_less_than_balance(self):
        self.account = Account("Daniel", "Olanrewaju", 2, 1111)
        self.account.deposit(5000)

        self.assertRaises(InsufficientAmountException, self.account.withdraw, 10000, 2)
        self.assertEqual(self.account.get_balance(2), 5000)

    def test_can_check_balance(self):
        self.account = Account("Daniel", "Olanrewaju", 2, 1111)
        self.assertEqual(self.account.get_balance(2), 0)