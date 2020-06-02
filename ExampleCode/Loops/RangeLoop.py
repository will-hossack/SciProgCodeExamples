"""
   Example to demonstrate a range loop to write theta and cos(theta)
   to terminal for theta in range 0 -> 2pi in 50 equal steps
"""

import math

def main():
    n_points = 50                    # Number of point 
    dtheta = 2.0*math.pi/n_points    # delta theta between outputs


    for i in range(0,n_points):   #     Indented code is within the loop
        theta = dtheta*i          #     Calculate theta
        cos = math.cos(theta)     #     Calcuklate cos
        print("Theta is : " + str(theta) + " and cos(theta) is : " + str(cos))

    print("End of loop")          # This is after the loop

# Run the program
main()
