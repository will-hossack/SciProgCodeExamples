"""   
    Demonstrate a logical function to test if  a point is inside or
    outside of a sphere of give radius.
    
    This concept of using a to to the work is good way to stucture code
    and is one of the key schemes to making complex programs readable and understandable.
    
"""



def inside(radius, x, y, z):
    """
    Function to check if point x,y,x is inside a sphere of radius r
    """
    lenSqr = x*x + y*y + z*z      # length squared; this avoids sqrt() for efficiency.
    if lenSqr <= radius*radius :  # Is inside sphere
        return True               # Return logical True
    else:                         # Else outside
        return False              # Return logical False


def main():
    radius = 5.0      # set radius 
    
    #       Prompt for a position in 3 dimensions
    x = float(input("X value : "))
    y = float(input("Y value : "))
    z = float(input("Z value : "))

    if inside(radius,x,y,z):    # Use the function above to do the work
        print("Point is inside sphere of radius : " + str(radius))
    else:
        print("Point is outside sphere of radius : " + str(radius))

main()

    
