#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as op
    from sys import argv as lol
    import sys
    a = len(lol)
    if a != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(lol[1])
    b = int(lol[3])
    if lol[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, op.add(a, b)))
    elif lol[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, op.sub(a, b)))
    elif lol[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, op.mul(a, b)))
    elif lol[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, op.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
