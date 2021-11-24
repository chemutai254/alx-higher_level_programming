#!/usr/bin/python3
def mutliple_returns(sentence):
    count = len(sentence)
    if count == 0:
        first = None
        return count, first
    else:
        first = sentence[0]
        return count, first
