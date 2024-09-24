#!/usr/bin/env python


import unittest
from src.calculator import *


class CalculatorTests(unittest.TestCase):

	def test_sum(self):
		assert sum(2, 3) == 5

	def test_substract(self):
		assert substract(5, 3) == 2

	def test_multiply(self):
		assert multiply(4, 7) == 28
  
	def test_divide(self):
		assert divide(28, 1) == 28
