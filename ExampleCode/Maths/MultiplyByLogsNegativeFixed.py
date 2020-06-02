
"""

    Python program to demonstrate multiple and divide by logs. 
    Modified to deal with negative numbers, note that 
    math.copysign(x,y) gives abs(x) with the sign if y.
    
"""
import math     # get the maths functions

def main():
    
    # Read in two floats
    a = float(input("Value a : "))
    b = float(input("Value b : "))
    
    #   Calcualte the natural log of abs() each so -ve values dont fail
    al = math.log(abs(a))
    bl = math.log(abs(b))
    
    #    Do a multiply by logs, and put the signs back in with math.copysign() 
    c = math.copysign(1.0,a)*math.copysign(1.0,b)*math.exp(al + bl)
    #    Print out the result
    print("Multiply by logs : " + str(c) + " and by normal multiply : " + str(a*b))
    
    #    Do a divide by logs and put the signs back in with math.copysign()
    c = math.copysign(1.0,a)*math.copysign(1.0,b)*math.exp(al - bl)
    #     Print out tghe result.
    print("Divide by logs : " + str(c) + " and by normal divide  : " + str(a/b))

#   run the main() 
main()