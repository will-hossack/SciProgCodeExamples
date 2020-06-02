"""
   Form a plot of a function using a function plotting function.

   This program contains the more complex concept of a function
   taking a function as an argument and returning two lists.

"""
import math
import matplotlib.pyplot as plt     # Import the plot package as plt

def exampleFunction(x):
    """
    Define a function of a single variable that returns a single float
    """
    return math.log(x) + math.atan(x)


def functionPlot(min,max,npts,fn):
    """
    Function to form the x/y from a function, note that fn() must be a function.
    """
    #     Form the plot parameters
    delta = (max - min)/npts
    x = min

    #     Creat two empty lists to hold the data
    x_data = []
    y_data = []

    #
    #        Fill the x/y arrays using the supplied function.
    while x <= max:
        x_data.append(x)         # Append the x value to the x list
        y = fn(x)                # Call fucntion supplied in the argument list
        y_data.append(y)         # Appled the value
        x += delta               # Increment x

    #       Return the x and y lists
    return x_data,y_data

def main():

    #    Get the x and y lists from the plot function
    #    Look carefully at this argument list, note exampleFunction is a function.
    #    It also returns two list, so data is a two element list.
    data = functionPlot(1.0,4.0,100,exampleFunction)

    #     Plot them not that data[0] is xdata and data[1] is ydata, but
    #     note new *data syntax that expands to data[0],data[1]
    plt.plot(*data,"b")                # Default plot in blue
    plt.title("Plot of Function")       # Add title/lables
    plt.xlabel("x value")
    plt.ylabel("y value")
    plt.show()                           # show the actual plot

# run the actual program
main()

