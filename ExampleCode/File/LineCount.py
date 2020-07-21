"""
     Example program to open a file and count the number of lines in the file.
     This example also show how to trap the most common (and annoying) problem of typing
     the wrong filename. If you are new to coding, ignore this and come back an look at it
     at the end of the course.

    Try with "burns.txt"
"""



def main():

    #        Prompt for file name and open it for reading
    #        This has a more compplex stucture to trap errors

    while True:                # Go into infinite loop
        try:                   # try: which traps errors for errors
            file = str(input("Filename : "))   # Prompt for name
            filein = open(file, "r")           # Open file
            break                              # If here, success, so break out of loop
        except FileNotFoundError :             # Catch the specific error, so failed to open file
            print("Failed to open file : {0:s}".format(file)) # Print error message then back to loop

    #         Read in the data to a list of strings.
    data = filein.readlines()
    filein.close()        # Close file, optional, but good pratcice

    print("Number of lines in file is :" + str(len(data)))

#   Run the program
main()
