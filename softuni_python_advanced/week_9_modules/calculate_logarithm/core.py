from math import log

def calculate_log(number, base):
    if base == 'natural':
        return f"{log(number):.2f}"
    else:
        return f"{log(number, 10):.2f}"