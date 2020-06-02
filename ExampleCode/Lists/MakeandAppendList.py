"""
     Make a simple list and append an extra element on the end
"""

def main():
    
    # make an inital list of integers
    myList = [0,1,4,9,16,25,36]
    
    # Print out the list and its length
    print("Initial list is : " + str(myList))
    print("Length of list is " + str(len(myList)))

    # Append an extra elements on the end
    myList.append(49)
    
    #   Print out the list and its new length
    print("List after appending an element is : " + str(myList))
    print("New length of list is " + str(len(myList)))


# Execute the code
main()
