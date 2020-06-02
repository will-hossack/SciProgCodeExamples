"""
   Simple converter between Fahrenheit and centegrade using functions.
   
   
"""

def fahrenheit(f):
    """
    Convert to centegrade to fahrenheit
    """
    return 9.0*f/5.0 + 32.0

def centegrade(c):
    """
    Convert fahrenheith to centegrade
    """
    return 5*(c - 32.0)/9


def main():           # Main program

    # Two temperatures in centegrade
    freezing = 0.0
    boiling = 100.0
    
    #   Print out Deg C and Def F for both
    print("Water freezes as : " + str(freezing) + " C or " + str(fahrenheit(freezing)) + " F")
    print("Water boils as : " + str(boiling) + " C or " + str(fahrenheit(boiling)) + " F")

    # Two temperatures in Farenheight
    normalbody = 98.2
    deathvalley = 134.0
    
    #   print out in Def F and Deg C
    print("Normal body temperature is : " + str(normalbody) + " F or " + str(centegrade(normalbody)) + " C")
    print("Death Valley record is : " + str(deathvalley) + " F or " + str(centegrade(deathvalley)) + " C")


main()
