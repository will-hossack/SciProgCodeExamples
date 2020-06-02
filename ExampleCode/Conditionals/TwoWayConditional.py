"""
     Simple two conditional example, to ask for an integer, then if less than 10
     ask for a bigger one.
"""

def main():
    
    a = int(input("Give an integer : "))        # Get an int 

    if a < 10 :                         # Test if < 10
        #              Inside True of conditional
        print("The integer you gave was less that 10, give a bigger one.")
        a = int(input("Give a bigger integer : "))
    else:
        #      Inside false of conditional
        print("The integer you gave was big enough.")

    #      Outside conditional
    print ("The integer you gave was : " + str(a))


# Execute the program
main()
