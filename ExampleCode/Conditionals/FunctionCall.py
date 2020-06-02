"""
     Example of calling functions within if satements.
     Work through this carefully and understand why the funcions get called when they do.
"""

def FnOne() :                     # Define a fucntion than return False
    print("Function One Called ")
    return False

def FnTwo():                     # Define a function that returns True
    print("Function Two Called")
    return True

def main():
    
    #      Use the functions with an "and" 
    print("Result of call with `and' ")
    if FnOne() and FnTwo():
        print("Success")
    else:
        print("Failure")

    
    #      Use the functions with an "or"
    print("\n\nResult of call with `or'")
    if FnOne() or FnTwo():
        print("Success")
    else:
        print("Failure")


#   execute the program
main()
