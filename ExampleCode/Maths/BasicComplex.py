"""
Example program, to read in two complex from the keyboard, form product and ratio
and print oout also form.

Extperiment with what type of input is accepted.
Note a complex number MUST NOT contain spaces.

"""

import cmath                 # Import ccomplex maths

def main():

    #      Read in two complex, these must be is a+bj format with NO spaces.
    a = complex(input("Complex a : "))
    b = complex(input("Complex b : "))

    #      Form pooduct and ratio
    c = a*b
    d = a/b
    #       Print out in default format
    print("Product is : " + str(c) + " Ratio is : " + str(d))

    #       Get complex in polar radius / phase format. Note it returns TWO values
    r,phi = cmath.polar(c)
    #        Print out what we get
    print("Product in polars, r: " + str(r) + " phi: " + str(phi))

main()