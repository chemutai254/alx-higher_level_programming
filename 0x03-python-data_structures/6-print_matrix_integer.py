#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        m = 0
        for n in row:
            len_matrix = len(row)
            m += 1
            print("{:d}".format(n), end="")
            if m != len_matrix:
                print(" ", end="")
        print("")
