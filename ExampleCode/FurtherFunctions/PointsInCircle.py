
"""
    Use a function to get x,y position of random points in a circle
    and plot out the restuls with a few more new MatPlotLib features
"""

import random
import matplotlib.pyplot as plt       # Standard Matplotlib import
from matplotlib.patches import Circle # Add circle from the patches module

def getpoint(radius = 1.0):
    """
    Function to get a random point in a circle of specified radius and return
    [x,y] as a list of floats

    :param radius: the circle radius (Default = 1.0)
    :type radius: float
    :return: [x,y]
    """
    while True:       # Go round loop forming x,y point
        x = random.uniform(-radius,radius)
        y = random.uniform(-radius,radius)
        if x*x + y*y <= radius*radius:  # In in circle, sucess break out of loop
            break

    return x,y         # Return the x,y point as a list


def main():
    #        Get number of points and radius of circlde
    npoint = int(input("Number of points : "))
    radius = float(input("Radius : "))

    xData = []        # Lists to hold x,y coordinates
    yData = []

    #      Go round while loop getting point
    while npoint > 0:
        xpt,ypt = getpoint(radius)    # use function to get point
        xData.append(xpt)             # Add points to lists
        yData.append(ypt)
        npoint -= 1


    #      Some more complex Matplot lib plotting (more flexible)
    fig,ax = plt.subplots()           # Get figure and axis of default plot
    ax.scatter(xData,yData)           # Plot points in axis as scatter plot
    #      Add a unfilled circle at (0,0) of colour "r"
    ax.add_artist(Circle((0,0),radius,color = "r",fill = False))
    ax.axhline(y=0, color='r')        # Add horizonal line though y = 0
    ax.axvline(x=0, color='r')        # Add vertical line though x = 0
    ax.axis("equal")                  # Set scale of axis to be equal in x,y
    plt.title("Scatter Plot")         # Add a ittle to the main plot
    plt.show()                        # Show the plot

main()
