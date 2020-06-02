"""
    Starter Python programm with main() to read in and print a 10^6 times the number then
    the square of that.
    
     Try this wth the inputs of: 4, -10.0, 67.0, 4e10, 4e-11 (see what happens)
    
"""

#      Create a main() which holds the program.
def main():
    #           Read in a float
    x = float(input("Type in a floating point number : "))

    # Do back arithmetic to change x and create new variable y
    x = x*1.0e6
    y = x**2

    #           Print out the two results converting x and y to strings.
    print("1 million time is : " + str(x) + " and the square of this is : " + str(y))
    
#        Now run main() 
main()
