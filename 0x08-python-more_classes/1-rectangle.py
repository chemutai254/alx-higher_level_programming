#!/usr/bin/python3
# 1-rectangle.py
"""class Rectangle that defines a rctangle based on 0-rectangle.py"""


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        try:
            if width != integer:
                if width < 0:
                    except ValueError:
                        print('width must be an integer')
                    except TypeError:
                        print('width must be >= 0')
