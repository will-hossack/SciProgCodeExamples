"""
   Example of extarcting a sublist and adding lists together, all works as you would
   expect.
   
   
"""

def main():

    #        Make two lsits (all int, but works for any type)
    a_list = [1,2,3,4,5,6,7,8]
    b_list = [9,10,11,12,13]

    #        Make a third list being a_list + elemets 3,4,5 of b_list
    c_list = a_list + b_list[3:6]
    print("The c_list is : " + str(c_list) + " of lenght " + str(len(c_list)))

    #        Make a fourth list being elements 4:end of a + 0,1,2 of list b
    d_list = a_list[4:] + b_list[:3]
    print("The d_list is : " + str(d_list) + " of length " + str(len(d_list)))



main()
