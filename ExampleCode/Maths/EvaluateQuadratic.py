
"""
      Python program to demonstrate basic mathematics by evaluation a quadratic
      and print out the value and the square root of the value.

"""

#      Add the additional maths functions
import math 

#      Create a main 
def main():
    
    #          Create three float variable 
    a = 4.0
    b = -13.5
    c = 10.2
    
    #          Ask for a value from the keyboard
    x = float(input("Give x value : "))
    
    #          Calcualte the quadratic and the square root ising the math.sqrt() function
    #          Note you do NOT require brackets.
    y = a*x**2 + b*b + c
    z = math.sqrt(y)
    
    #           Print out the results as a string
    print("Value of quadratic is : " + str(y) +" and its sqrt root is : " + str(z))
    

# Run the main()

main()