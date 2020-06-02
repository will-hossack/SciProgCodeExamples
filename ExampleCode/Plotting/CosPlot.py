"""
   Form a cos(theta) plot in range 0 -> 4pi

   This example shown the main method to plot data by creating two lists
   for the x and y data which are then plotted.

   There are better ways to do this, but learn the simple way first.

"""
import math
import matplotlib.pyplot as plt     # Import the plot package as plt

def main():

    #       Specify the plot parameters.
    plotRange = 4.0*math.pi           # Range of plot
    plotPoints = 100                  # Number of point
    increment = plotRange/plotPoints  # Increment between points

    thetaData = []                    # lists to hold the data
    cosData = []

    # Fill up the two list with data using a range loop.

    for i in range(0,plotPoints):
        theta = increment*i            # value of theta
        cos = math.cos(theta)
        thetaData.append(theta)        # add theta value to list
        cosData.append(cos)            # add cos value to list


    # Start of plot
    plt.plot(thetaData,cosData,"g")      # Default plot in green
    plt.title("Plot of cosine")          # Add title/labels on axis
    plt.xlabel("Angle theta")
    plt.ylabel("Cos(theta)")
    plt.show()                           # show the actual plot

# run the main()
main()
