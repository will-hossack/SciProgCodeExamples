"""
        Example of use of eval() function reading floats and complex.
        Thsi evaluated the string typed 
        
        For float try
        4*(3 -17) will give -56.0
        1.3 + math.cos(math.radians(45)) = 2.007
        
        For complex try
        
        3*(4 + 4j) will give (12+15j)
        cmath.exp(complex(0,math.pi)) will give -1 (with a bit of rounding error)
                                                    
        In Python 2 this was the default operation of input() but this was changed
        in Python 3, so if you want this now you have to call it explicitely as shown
        in the code.

"""

import math
import cmath

def main():
    
    
    s = input("Give a float expression : ")       # Read in a string
    x = float(eval(s))                            # evaluate and return a float
    #                                             Print out the result
    print("Expression typed : " + str(s) + " and value : " + str(x))
    
    s = input("Give a complex expression : ")       # Read in a string
    z = complex(eval(s))                            # evaluate and return a complex
    #                                             Print out the result
    print("Expression typed : " + str(s) + " and value : " + str(z))


    
#    Execute the program
main()