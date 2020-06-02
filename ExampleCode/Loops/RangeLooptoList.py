"""
   Example to demonstrate a range loop to write theta and cos theta
   to a lists.
   
   This in the main may to make lists and will be used in plotting programs
   in the b ext section.
"""

import math


def main():

    n_points = 50                  # Number of point in list
    dtheta = 2*math.pi/n_points    # gap between poingts
    thetaData = []                 # empty list 
    cosData = []                   # empty list


    for i in range(0,n_points):
        theta = i*dtheta                    # Set theta
        cos = math.cos(theta)
        thetaData.append(theta)             # Add values to list
        cosData.append(cos)

    #         Do a default print (not very tidy output, replace this and 
    #         a loop and make it nicer)
    
    print(str(thetaData))
    print(str(cosData))



main()
