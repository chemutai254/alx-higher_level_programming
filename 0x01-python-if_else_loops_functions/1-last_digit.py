#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)
if number < 0:
    last_digit = number * -1
    last_digit = last_digit % 10
elif:
    last_digit = number % 10
    print('Last digit of {}'.format(number), end=' ')
if last_digit > 5:
    n = 'Last digit of {} is {} and is greater than 5'
elif last_digit < 6 and last_digit != 0:
    n = 'Last digit of {} is d} and is less than 6 and not 0'
elif last_digit == 0:
    n = 'Last digit of {} is {} and is 0'
print(n.format(number, last_digit))
