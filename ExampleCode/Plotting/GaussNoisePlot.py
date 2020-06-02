"""
   Plot a histgram of Gaussian noise. 
   This program introduces the new matlibplot method hist() to generate a 
   histogram
   
   
"""

import random                       
import matplotlib.pyplot as plt     # Import the plot package as plt

def main():

    #        Set up data
    point = 10000                        # Number of points
    gaussData = []                       # list to hold points
    mean = 20.0                          # mean of noise
    sd = 2.0                             # standard deviation of noise

    #        Fill up the gaussData list with the output of the
    #        gaussian random numbre generator
    while point >= 0:                   # Fill list with gauss randoms
        gaussData.append(random.gauss(mean,sd))
        point -= 1

    #            Plot histogram with 40 bins and range of mean +/- 3sd
    #            Note syntax of named keywords, this is new, also range take a 
    #            two element list of [min,max]
    plt.hist(gaussData, bins = 40, range = [mean - 3*sd , mean + 3*sd])
    plt.title("Histogram of Gaussian Noise")
    plt.xlabel("value")
    plt.ylabel("Number of events" )
    plt.show()

main()
