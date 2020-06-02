""""
    A more developed Vector class for simple 3d vectors. 
    This involves much much more Python syntax and OOP concpts than is needed
    for this course, but is useful for future courses.
"""

import math
class Vector3d(object):
    """
    Simple vector 3d class
    """
    def __init__(self, x, y, z):
        """
        Constructor to form a vector with three components
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self): 
        """
        Method to format a vector as a string (implments the str() function) 
        """
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

    def copy(self):
        """
        Method to return a copy of current vector
        """
        return Vector3d(self.x,self.y,self.z)

    def magnitude(self):
        """
        Return the magnitude
        """
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def distance(self,b):
        """
        Distance from self to vector b
        """
        dx = self.x - b.x
        dy = self.y - b.y
        dz = self.z - b.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)


    def normalise(self):
        """
        Normlaise current vector so its magnitude is 1.0 (unit vector)
        """
        mag = self.magnitude()
        if mag != 0.0 :         # if not already zero
            self.x /= mag       # dveive throgh by mag
            self.y /= mag
            self.z /= mag
        return self

    def add(self,b):
        """
        Add a vector b or float to self and return a new vector.
        """
        if isinstance(b,Vector3d):
            x = self.x + b.x           # Local varaible
            y = self.y + b.y
            z = self.z + b.z
        else:
            x = self.x + b
            y = self.y + b
            z = self.z + b
        return Vector3d(x,y,z)     # return a new Vector3d
    
    
    def subtract(self,b):
        """
         Subreatct a a vector b or float to self and return a new vector.
        """
        if isinstance(b,Vector3d):
            x = self.x - b.x           # Local varaible
            y = self.y - b.y
            z = self.z - b.z
        else:
            x = self.x - b
            y = self.y - b
            z = self.z - b
        return Vector3d(x,y,z)     # return a new Vector3d
    
    
    def min(self,b):
        """
        Get the min of self and b
        """
        x = min(self.x,b.x)
        y = min(self.y,b.y)
        z = min(self.z,b.z)
        return Vector3d(x,y,x)
        
    def max(self,b):
        """
        Get the max of self and b
        """
        x = max(self.x,b.x)
        y = max(self.y,b.y)
        z = max(self.z,b.z)
        return Vector3d(x,y,x)

    def addTo(self,b):
        """
        Add a vector b to self in place.
        """
        self.x += b.x              # Update internal varaible
        self.y += b.y
        self.z += b.z
        return self                # Return self (see later why)


    def dot(self,b):
        """
        Form dot product between self and vector b
        """
        return self.x*b.x + self.y*b.y + self.z*b.z

    def cross(self,b):
        """
        Form cross product between self and vector b.
        """
        x = self.y*b.z - self.z*b.y       # Do cross product in local variable
        y = self.z*b.x - self.x*b.z
        z = self.x*b.y - self.y*b.x
        return Vector3d(x,y,z)            # return a new Vector3d

def main():               
    """
    Simple test program to test the vectors
    """
    a = Vector3d(1,2,3)
    b = Vector3d(4,5,6)

    print("Magnitde of a is " + str(a.magnitude()))

    c = a.cross(b)           # Form cross product
    #
    #         the str() function call the __str__(self) method
    print("Cross product of a x b is : " + str(c)) 

# Incomment the line below run the test
# main()

        
