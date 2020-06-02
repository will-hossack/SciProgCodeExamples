"""
     Three way conditional if elif else. 
     
     Try with different valus if input and make sure you understand 
     that ONLY ONE section of the if elif else structor is every executed.
"""

import math

def main():
    
    #       Get a float valus
    a = float(input("Give a float : "))
    
    
    
    if a > 4.0 :          # Test if > 4
        #         Inside if
        b = 4.0 - math.sqrt(a)
        a = 2.0*(b - 3.0)
        print("if statements executed")
    elif a > 0 :          # Test if > 0
        #         Inside else is
        b =  1.0 + math.sqrt(a)
        a = (b - 1.0)
        print("elif statements  executed")
    else :                  # Everything else
        #         Inside else
        b = 4.0 - 3.0*math.sqrt(-a)
        a = 7.0*(b - 3.0)
        print("else statements executed")

    #              Outside conditional, print the final values
    print("The value of a is : " + str(a) + " and b is : " + str(b))

main()
