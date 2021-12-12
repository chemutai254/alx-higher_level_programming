#!/usr/bin/python3
def safe_print_division(a, b):
	result = a / b
	try:
	    print('{:d}'.format(a, b, result))
	    return result
	except (ValueError, TypeError):
	    print('Check the type of data')
	    return Null
