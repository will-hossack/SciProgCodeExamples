"""
        Python program to read in angle in degree, convert to radians, and calcualte sin()
        and cos() of the angle.

        Try with various angles and check with your calcualtor.

"""

#      Add the maths funcyions
import math

def main():
    #         get angle from keyboard
    theta = float(input("Angle in degrees : "))

    #         Convert to radians and calcualte sin() and cos()
    #         Remember sin / cos work in radians.
    theta = math.radians(theta)
    sin = math.sin(theta)
    cos = math.cos(theta)

    #         Do a sanity check, should be 1.0
    s = sin**2 + cos**2

    print("Angle: " + str(theta) + " Sin: " + str(sin) + " Cos: " + str(cos) + " check : " + str(s))

#    Run the program
main()

