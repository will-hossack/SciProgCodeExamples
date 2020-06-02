"""
   Form a plot of a quadratic in the range 0 -> 10.
   
   This program used a while look rather than range, both are suitable alternatives.
   
"""
import matplotlib.pyplot as plt     # Import the plot package as plt

def quadratic(a,b,c,x):
    """
    Define a quadratic
    """
    return a*x**2 + b*x + c

def main():
    
    #    Read in the a,b,c coefficients
    aval = float(input("a value : "))
    bval = float(input("b value : "))
    cval = float(input("c value : "))
    
    #    Calcualte the plot parameters, 
    plotRange = 10.0           # Range of plot
    plotPoints = 100                   # Number of point
    increment = plotRange/plotPoints   # Increment between points

    xData = []                    # lists to hold the the x/y data
    yData = []

    x = 0.0                        # start with x = 0.0
    while x < plotRange:
        xData.append(x)                   # append x to xData
        yData.append(quadratic(aval,bval,cval,x))  # append value fron function to yData
        x += increment                    # increment x and go back round loop


    plt.plot(xData,yData,"r")            # Default plot in red
    plt.title("Plot of quadratic")       # Add title/lables
    plt.xlabel("x value")
    plt.ylabel("y value")
    plt.show()                           # show the actual plot


main()
