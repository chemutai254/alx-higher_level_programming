#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    name = dir(hidden_4)

    for n in range(len(name)):
        if name[n][:2] != '__':
            print(name[n])
