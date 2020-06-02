"""
        Yet another version to plot cos in the range 0 -> 4pi using Numpy
        (the numerical package) to do all the work

        This is beyond this course, but you will learn Numpy next year.
"""
import matplotlib.pyplot as plt
import numpy as np

def main():

    thetaData = np.linspace(0,4.0*np.pi,300)     # Create a linear space from 0->4pi with 300 points

    #             Use numpy functions np.degrees and np.cos that both return numpy arrays
    plt.plot(np.degrees(thetaData),np.cos(thetaData))
    #              Add the title
    plt.title("Cos Plot using Numpy")
    plt.xlabel("Angle in degrees")
    plt.ylabel("Cos")
    plt.show()    # Do the actual plot

main()

