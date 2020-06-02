"""
     Example to shown scope of variable in a main() program.

"""

ag = 34.56            #     Define in three global values.
bg = 41.45
x = 100.0

def main():
    """
    The main programme
    """
    global ag         # Make ag writable within main() 
    #       Print out values, not bg can be read.
    print("Value of ag in main is : " + str(ag) + " and  bg is : " + str(bg))

    ag +=  10         # Undate value of ag inside main()
    print("New Value is ag is : " + str(ag))

    x = 30.0          # Declare x inside main (note NEW variable) and NOT global.
    print("Internal value of x is : " + str(x))
    
#      Run main rogram
main()
#      Do an external print to check globals.
print("External value of ag is : " + str(ag))
print("External value of x is : " + str(x))
