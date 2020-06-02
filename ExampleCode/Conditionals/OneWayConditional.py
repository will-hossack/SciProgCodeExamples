"""
    Simple one way conditional, try for various values if input
"""

def main():

    #       Get a int from the keyboard
    a = int(input("Give an integer (less that 10 ) : "))
    
    if a > 10 :            # Note the ":"
        #                  Statement in inside conditional (nore indentation)
        print("You gave an integer > 10, but OK anyway");

    #   Statment is after conditional 
    print("The integeer you gave was : " + str(a))


#      Execute program
main()
