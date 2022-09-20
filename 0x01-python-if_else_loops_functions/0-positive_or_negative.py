#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (not(number % 2 == 0)):
	print(f"{number:d} is negative")
elif (number == 0):
	print(f"{number:d} is zero")
print(f"{number:d} is positive")
