"""
    Starter Python programm with main() to read in and print a floating point number
    
    Try this program with program with inputs of:
        4, 3.56, -5.67, 3.45e7, 6.62e-34 and rubbish!
"""

#        Creat main() to hold the program, NOTE: the code inside main() is indented.
def main():
    #           Read in a float Note: the float() converts 
    x = float(input("Type in a floating point number : "))

    #           Print it out, Note the str() to convert the flat to a string.
    print("The float number is : " + str(x))

#    Now run the main() proggram
main()
