"""
   Example to open and write text strings, (and add a bit of culture)
"""

def main():
    fileout = open("burns.txt","w")

    fileout.write("When chapman billies leave the street,\n")
    fileout.write("And drouthy neebors, neebors meet,\n")
    fileout.write("As market-days are wearing late,\n")
    fileout.write("An' folk begin to tak the gate;\n")
    fileout.write("While we sit bousing at the nappy,\n")
    fileout.write("And getting fou and unco' happy,\n")
    fileout.write("We think na on the lang Scots miles,\n")
    fileout.write("The mosses, waters, slaps and styles,\n")
    fileout.write("That lie between us and our hame,\n")
    fileout.write("Whare sits our sulky sullen dame,\n")
    fileout.write("Gathering her brows like gathering storm,\n")
    fileout.write("Nursing her wrath to keep it warm.\n")
    fileout.write("\nRobert Burns\n")

    fileout.close()


main()
