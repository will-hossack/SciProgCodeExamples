"""
   Exmaple to format floats using .format() method. 
   
   Note: this is not needed for the course but is a nice extra.
   
   The concept is the same as ising str(), you form a string that you then print.
"""
import math
import random

def main():



    # Form a string with the .format, 0:.8f = format first argument in fixed format with 
    # 8 figures after the .
    s = "Value of pi with 8 figures after the point is : {0:.8f}".format(math.pi)
    print(s)
    
    #     Format of large number with exp <x.y>e<n> notation and and by default format
    big = math.pi*1e6
    print("Format big with exp with 4 places after point : {0:8.4e} and in default : {1}".format(big,big))

    #      Form three random numbers bertween 0 > 1
    x = random.random()
    y = random.random()
    z = random.random()

    # Print them in a nice way, not the use of the \n character to give new lines
    print("\nThe three random numbers are :\nx = {0:6.4f}\ny = {1:6.4f}\nz = {2:6.4f}".format(x,y,z)) 

main()