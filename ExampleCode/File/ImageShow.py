"""
        Example to read a image file using the matplotlib image module
        and display it. It will work with all common image formats

        Try with the supplied "stones.jpg" file. (stones on a Scottish beach)
"""

import matplotlib.pyplot as plt
import matplotlib.image as img     # Import image module

def main():
    filename = str(input("Graphics file : "))

    image = img.imread(filename) # Read the jpeg
    plt.imshow(image)                  # render it in plot axis
    plt.show()                         # display it

main()
