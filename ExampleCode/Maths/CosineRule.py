
"""
       Python programm to calculate the third side of a triangle by the Cosine Rule
       and the three angle of the trangle by the Sin Rule.
"""

import math

def main():
    
    #    Get the lengths of two sides and angle between them
    a = float(input("First side of triangle : "))
    b = float(input("Second side of triangle : "))
    theta_c = float(input("Angle between them : "))
    
    #      Convert theta_c to radians
    theta_c = math.radians(theta_c)
    
    #       Calculate length of side c by the cosine rule
    #       Note the order of operators and minimal use of brackets.
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta_c))

    print("Length of third side by cosine rule is : " + str(c))
    
    #      Use sin rule to calcuate angle. 
    #     Note all angle converted back to degree to make them humanly readable.
    ratio = c/math.sin(theta_c)
    theta_a = math.degrees(math.asin(a/ratio))
    theta_b = math.degrees(math.asin(b/ratio))
    theta_c = math.degrees(theta_c)
    
    print("Angles are A: " + str(theta_a) + " B:" + str(theta_b) + " C: " + str(theta_c))
   
#    Run the program
main()