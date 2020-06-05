"""
    Example program to create a list of fucntions and then call them from
    a loop.

    This program illustrated the flexibility of functions, also that you can have
    list of anything, in this case you have a list of functions !!

    This is a rather dangerous language feature and while it shows the flexibility of lists and
    functions, it is not an advised progarmming method since the scope for obscure code is
    unlimited.

"""


import math

def myFn(y):
    #       Create own local function that returns a value
    return 1 - math.erf(y)

def main():

    #      Make a list of, both from math library and lovcal
    functions = [math.cos,math.sin,math.tan,myFn]


    x = float(input("X value : "))    # Read in float from command line

    for fn in functions:               # Access the list of functions
        y = fn(x)                      # Use each elemenst of the list as a function.

        print("Value from " + str(fn) + " is : " + str(y))
        #     Note str(fn) gives the correct information but in rather messeg way.



main()

