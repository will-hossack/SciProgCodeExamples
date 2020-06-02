"""
    Python program deminstrate how to specify and fomat integers in various bases.
    
    Not needed for this coures but good to know.
    
    
"""

def main():

    #         Make 4 ints
    ad = 785663             # In decimal
    ah = 0x6de2a            # In hex (base 16) note the 0x prefix
    ao = 0o342776           # In octal (base 8) note the 0o prefix
    ab = 0b10000110010110   # In binary (base 2) note the 0b prefix


    # print out each number in decimal, hex, octal and binary
    print("ad in decimal: {0:d} Hex: {0:x} Octal: {0:o} Binary : {0:b}".format(ad))
    print("ah in decimal: {0:d} Hex: {0:x} Octal: {0:o} Binary : {0:b}".format(ah))
    print("ao in decimal: {0:d} Hex: {0:x} Octal: {0:o} Binary : {0:b}".format(ao))
    print("ab in decimal: {0:d} Hex: {0:x} Octal: {0:o} Binary : {0:b}".format(ab))
    
    

# run the program
main()
