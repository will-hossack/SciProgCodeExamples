"""
   Program to read in a complex number and print out which
   quadrant it is in using a if: elif chain inside a function.

   Try with various complex numbers


"""


def quadrant(z):
    """
    Function to determine which quadrant a complex number is in.
    """
    if z.real >= 0 and z.imag >= 0:
        return 1

    elif z.real < 0 and z.imag >= 0:
        return 2

    elif z.real < 0 and z.imag < 0:
        return 3

    else:
        return 4



def main():
    #      Get a complex number from the keyboard
    z = complex(input("Give a complex number : "))
    print("Typed number is : " + str(z))

    #          We are able to just use the fuction inside the str()
    print("It is in quadrant : " + str(quadrant(z)))



# run program
main()
