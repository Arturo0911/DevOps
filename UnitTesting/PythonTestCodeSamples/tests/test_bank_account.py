#!/usr/bin/env python

import unittest

from src.bank_account import *

class BankAccountTests(unittest.TestCase):
    
    def test_deposit(self):
        account = BankAccount(balance=1000)
        new_balance = account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        account = BankAccount(balance=3000)
        new_balance = account.withdraw(1200)
        assert new_balance == 1800
