"""
   Example to demonstrate a while loop to write theta and cos theta
   to a lists.
   
   This is an alternative way to write the RangeLooptoList.py example program
   
"""

import math


def cosvalue(theta,offset):
    """
    Function to calcuate cos with an offset phase ansd angle    
    """
    return math.cos(theta + offset)

def main():
    n_points = 50
    dtheta = 2.0*math.pi/n_points  # theta increment
    theta = 0.0                    # theta start
    thetaData = []                 # empty list 
    cosData = []                   # empty list


    while theta <= 2.0*math.pi:              # while loop
        thetaData.append(theta)             # Add theta value to list
        cosData.append(cosvalue(theta,math.pi/2)) # Add cos with offset pi/2
        theta += dtheta                # increment theta

    #         Do a default print (not very tidy output, replace this and 
    #         a loop and make it nicer)
    print(str(thetaData))
    print(str(cosData))


main()
