#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        if result != 0:
            print('Result equals: {}'.format(result))
            return result
        else:
            print('Check the type of data')
            return Null
