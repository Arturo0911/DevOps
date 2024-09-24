#!/usr/bin/env python3


def sum(a, b):
	return a + b

def substract(a, b):
	return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("The division by 0 is not permitted")
    return a / b
