"""
   Example to demonstrate a range loop to write theta and cos theta
   to output file of specified name to your current directory.
   
"""

import math

def main():
    
    #     Get filename
    filename = str(input("Output file : "))
    fileout = open(filename,"w")    # Open file for writing (note "w" flag)

    #      Paramteres of the plot of 50 points as step between points
    nPoints = 50
    dtheta = 2*math.pi/nPoints   

    #       Go round a look, calcualting theta / cos aod write out
    for i in range(0,nPoints + 1):
        theta = i*dtheta                # Form theta
        cos = math.cos(theta)           # Form cos
        # write out line as string, note the "\n" at the end as comparted to print()
        fileout.write(str(theta) + " , " + str(cos) + "\n")

    fileout.close()      # finished loop, so close the file (good practice)


main()
