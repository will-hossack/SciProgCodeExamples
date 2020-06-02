""" 
    Here is an example of how NOT to use globals.
    Look as this an try an find out what went wrong
"""


vals = []

def add_values(vals):
    x = 0.0          # Local variable
    for y in vals: # Sum up values in list
        x += y
    return x         # return local value


def main():
    
    localVals = vals         # want to make a localVals
    for i in range(0,10):
        x = 5.0*i
        localVals.append(x)  # Append to localVals
        vals.append(x)       # Append to vals
        
    x = add_values(localVals) # Sum up with function
    print("Sum of values is : " + str(x))   # Print
    
    # Contents of vals is
    
    print("Local vals is : \n" + str(localVals))
    print("Global vals is : \n" + str(vals))
    
    # Try and disentangle what is happending here; its syntactically correct Python
    # but it illustartes how dargerous globas can be...... this is real bug found in
    # a piece of student code (after a lot of searching)

    

main()
