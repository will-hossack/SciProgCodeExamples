"""
   Read a text file and print out to the print out to terminal.
   Note the two methods of removing the extra newline characters at the end of lines.
   
   Try with "burn.txt" for first verse of Tam O-Shanter
"""

def main():
    
    
    #   Get the name of the to open, and open it for raedimng
    filename = str(input("Input file name : "))
    filein = open(filename, "r")            # Open file for reading

    #    Read the data into list of strings
    inputData = filein.readlines()         # Read in data as list of strings
    filein.close()                          # Close the file (optional but good practive)
                                            # Note the file has been read into list of strings
                                            
    for line in inputData:                 # Scan through writing lines
        print(line,end="")                  # Note the (end = ""), this remove the automatic "\n"


    # or an alternate way is to remove the last character BEFORE you print, 
    for line in inputData:
        print (line[:-1])               # This removes the last character.

#   Run the main program
main()
