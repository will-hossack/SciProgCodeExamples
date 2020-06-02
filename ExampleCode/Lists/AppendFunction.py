"""
       Demonstration of Append function that works for any variable type.
"""

def append(first,second):
    """
    A generic append function
    """
    l = first + second
    return l

def main():
    #          Form two lists
    fl = [1,2,3,5]
    sl = [6,7,8,9,10]
    #           Append with a function abvobe
    nl = append(fl,sl)
    
    #       Print out the three lists
    print("First list : " + str(fl))
    print("Second list : " + str(sl))
    print("Combined list : " + str(nl))

    #          Can also be used to append any variable type, so if arguments are int
    #          it will simplly add
    x = 10.0
    y = 11.0
    z = append(x,y)
    print("Value of z is : " + str(z))

main()
