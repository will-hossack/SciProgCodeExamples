"""
    Starter Python programm with main() to read a float and an int, do some simple
    processing and print output.
"""

# Creat a main() to hold the program. Note all code inside main() is indented.
def main():
    #           Read in a float and and int
    x = float(input("Type in a floating point number between 5 and 10 : "))
    ix = int(input("Type in an integer between 10 and 20 : "))

    #     Do a simple divide
    y = x/ix

    print("Float: " + str(x) + " divided by " + str(ix)  + " is " + str(y))

    # Do an integer divide (note the //) and a normal divide 
    iz = ix//5
    z = ix/5

    #    Print out the two 
    print("The integer : " + str(ix) + " integerd divide  by integer 5 is: " + str(iz))
    print("and divided normal divide by 5  is : " + str(z))

#    Now run the main()
main()
