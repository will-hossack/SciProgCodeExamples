"""     
    Example of estimating pi by monte-carlo similation with graphical
    output.
    
"""
import math
import random
import matplotlib.pyplot as plt


def main():
    
    #               Get number of points in the simulation
    maxPoint = int(input("Number of points : "))
    plotInterval = maxPoint/100    # How often to plot the estimate
    
    #                Two lists to hold the estimages
    xData = []
    yData = []

    #                 Two counter, one for no of points, one for number instide 
    point = 0
    inside = 0
    
    while point < maxPoint:
        point += 1
        x = random.uniform(-1.0,1.0)    # Random between -1 -> 1for both x and y
        y = random.uniform(-1.0,1.0)    # Area of square is 4.0

        if x*x + y*y <= 1.0:   # Test if inside unit circle
            inside += 1        # Record point in circle

        if point % plotInterval == 0:   # Calcualte estimate for plot
           estimate = 4.0*inside/point
           xData.append(point)
           yData.append(estimate)


    estimate = 4.0*inside/maxPoint
    print("Estimate for PI after " + str(maxPoint) + " is " + str(estimate)) 
    
    #     Plot the graphs
    plt.plot(xData,yData)      # Plot the estimate
    plt.plot([0,maxPoint],[math.pi,math.pi]) # Plot Pi as a line. 
    plt.ylim(3.0,3.3)          # Limit graph range
    plt.title("Plot of estimate of Pi again points")
    plt.show()


main()
