"""
   Example of a function to calculate the value of a quadratic.
   

"""

def quadratic(a , b, c, x):
    """
    Function to calcuate a quadratic of for a*x**2 + b*x + c and return a float value.
    Note contents of function are indented.
    """
    #     Do the calcualtion 
    y = a*x**2 + b*x + c
    #     Return the value of y at a float
    return float(y)


def main():
    
    #     Create the three coefficients as floats of specified values
    aval = 4.0
    bval = 6.0
    cval = -10.0
    
    #      get a x value from the keyboad
    xval = float(input("Give x value : "))
    
    #     call the quadratic function with the specified values
    #     Note: the varable names are diffent; its the value that is passed.
    yval = quadratic(aval,bval,cval,xval)
    
    # print the returned value.
    print("Value of quadratic is : " + str(yval))

main()
