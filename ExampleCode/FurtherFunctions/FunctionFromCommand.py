"""
    Example program to show that you read in a fucntion name from the
    command line and then ececute it

    Try with fnOne, fnTwo, it it also works for math.cos, math.sin, math.log etc
"""

import math


def fnOne(y):
    """
        Create a function
    """
    print("Funcion one called with y = " + str(y))
    return y     # Just return the given vaue


def fnTwo(y):
    """
        Create a second function
    """
    print("Funcion two called with y = " + str(y))
    return 2*y   # Just return double the value


def main():

    while True:     # Keep in a loop
        fn = eval(input("function : "))    # Read in functioon name NOTE: eval()
        y = float(input("y value : "))     # Get a parameter value

        z = fn(y)                          # Call function read in
        print("Value returned is : " + str(z))


if __name__ == "__main__":
    main()
