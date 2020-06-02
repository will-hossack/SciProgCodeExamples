"""
    Simple demo to show that test on float numbers is a VERY bad idea.
    It also inclues the correct way to do this.
    
    Try with 2.0 and 4.0 and a random set of others and see what happens.
    (then don't put this is a program) 
     
"""

import math

def main():

    #          make 
    
    x = float(input("Value : "))
    y = math.sqrt(x)**2

    if y == x:
        print("math.sqrt({0:4.2f})**2 = {0:4.2} so maths works".format(x))
    else:
        print("math.sqrt({0:4.2f})**2 != {0:4.2} so maths fails".format(x))

    delta = y - x
    print("Difference between the numbers is : " + str(delta))
    
    # Here this the correct way to do this with the math.isclose() function.
    # this ONLY works on Python 3.5 or newer
    
    if math.isclose(x,y):
        print("The math.isclose() test works")
    else:
        print("The math.isclose() test fails")
    
#   Execute the program

main()
