""""
    Example to demonstrate changing a list inside a fundtion
    
    This examplte is rather more complex, there will be more about passing
    lists into functions 
        
"""

def sortit(ls):
    """     Function to sort a list
    """
    ls.sort()
    return ls  # Return the sorted list 

def main():
    
    vals = [2,9,1,5,6,3,0]    # Create a list of integers
    nl = sortit(vals)         # Sort using function and return value
    print(str(vals))          # Print contents of original list
    print(str(nl))            # Print retured list

    vals.append(99)           # Add extra element to original list
    print(str(vals))          # Print and see what has happend...
    print(str(nl))            # this will be expalined later !!!


main()
