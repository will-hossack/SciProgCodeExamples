"""

    Python program to demonstrate multiple and divide by logs. 
    
    Try for various vales, what happens if the numbers are negative ?
"""
import math     # get the maths functions

def main():
    
    # Read in two floats
    a = float(input("Value a : "))
    b = float(input("Value b : "))
    
    #   Calcualte the natural log of each
    al = math.log(a)
    bl = math.log(b)
    
    #    Do a multiply by logs 
    c = math.exp(al + bl)
    #    Print out the result
    print("Multiply by logs : " + str(c) + " and by normal multiply : " + str(a*b))
    
    #    Do a divide by logs
    c = math.exp(al - bl)
    #     Print out tghe result.
    print("Divide by logs : " + str(c) + " and by normal divide  : " + str(a/b))

#   run the main() 
main()