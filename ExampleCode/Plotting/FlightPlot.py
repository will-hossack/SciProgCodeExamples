"""
   Form a plot the flight of a particle given initial velocity
   and acceleartion.

   Note the graph here is distance against time.


"""
import matplotlib.pyplot as plt     # Import the plot package as plt

def distance(u,a,t):
    """
    Function to calcualte distance given initual velocity, accelaration and time
    """
    x = u*t + 0.5*a*t**2         # Calcualte distance
    return x                     # Return distance

def main():

    #     Get the parameters
    uStart = float(input("Inital velocity : "))
    acc = float(input("Accelearion : "))
    maxTime = float(input("Maximium time : "))

    plotPoints = 100                   # Number of point
    increment = maxTime/plotPoints     # Increment between points

    tData = []                    # lists to hold the data
    xData = []

    for i in range(0,plotPoints): # Start of loop
        t = increment*i            # Time
        x = distance(uStart,acc,t)        # Get distance
        tData.append(t)           # Append to t list
        xData.append(x)           # Append to x list


    plt.plot(tData,xData,"g")          # Default plot in green
    plt.title("Flight of particle")    # Add title/lables
    plt.xlabel("Time in secs")
    plt.ylabel("Distance in m")
    plt.grid()                        # Add a grid to the plot
    plt.show()                        # show the actual plot


main()
