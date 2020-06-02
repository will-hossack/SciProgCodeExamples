"""     Solution to Checkppoint 6 to calcualte the volume of
        molecule by Monte Carlo integration.

        This is rather more complex program than you are expect to create at this stage
        and introduces a number of new progrmming and Python concepts.
"""

import random
from Vectors import Vector3d       # Impirt the Vector3d from external file in same directory
import matplotlib.pyplot as plt


class Atom(Vector3d):
    """
    The Atom class to extends the Vector3d that hold position.
    New concept of exending a class which inherits variable and method.
    """

    def __init__(self,x,y,z,r):
        """
        Constructor to form an atom with x,y,z,r parameters
        """
        Vector3d.__init__(self,x,y,z)    # set underlying Vector3d
        self.radius = float(r)           # add radius of atom

    def __str__(self):
        """
        Implemnts str() (this overwrite the one in Vector3d)
        """
        return "Atom : r = " + str(self.radius) + " at " + Vector3d.__str__(self)

    def isInside(self,v):
        """
        isInside method, returns True if Vector3d v in inside atom.
        (Note distance() inherited from Vector3d)
        """
        return self.distance(v) <= self.radius

class Molecule(list):
    """
    Molecule, being a list to hold Atoms
    """
    def __init__(self,*args):
        """
        Constrcutor to form a Molecule with optional arguments each one assume to be an Atom
        Note *args syntax, new concept.
        """
        list.__init__(self)      # Init underlying list
        for a in args:           # Append any args to list, note args will be a list
            self.append(a)

    def __str__(self):
        """
        Format string of all atoms
        """
        s = ""
        for a in self:
            s += str(a) + "\n"
        return s

    def inInside(self, v):
        """
        Method to check if vector is inside moleule.
        """
        for a in self:
            if a.isInside(v):
                return True   # Jump out as soon as inside an atom.

        return False           # if here then outside

    def fromFile(self,file):
        """
        Read Atoms from a file
        """
        for line in file.readlines():
            if len(line) > 0 and not line.startswith("#"):  # Ignore blank lines and comments
                tokens = line.split(",")
                r = float(tokens[1])            # ignore first token with name
                x = float(tokens[2])
                y = float(tokens[3])
                z = float(tokens[4])
                self.append(Atom(x,y,z,r))      # Form Atom and append to self
        return self

class BoundingBox(object):
    """
    Class to define a  bounding box class round the molecule.
    This class involves several new Python features.
    (This is the most complex class in the whole program)
    """
    def __init__(self, m):
        """
        The Conctructor, which takes molecule or an atom.
        This uses recursion to call itsself if needed.
        """

        if isinstance(m,list):       # If a list given ,its a moleculte
            # Set initial box a two infinite vectors
            self.min  = Vector3d(float("inf"),float("inf"),float("inf"))
            self.max  = Vector3d(float("-inf"),float("-inf"),float("-inf"))

            #        Now add it atoms one at a time
            for a in m:
                #     Note recalling the BoundingBox for each atom (recursion)
                self.addBox(BoundingBox(a))

        else:                    # Assume its an atom
            self.min = m.subtract(m.radius)
            self.max = m.add(m.radius)


    def addBox(self,box):
        """
        Method to add a box, used the min/max methods in Vector3d
        """
        self.min = self.min.min(box.min)
        self.max = self.max.max(box.max)



    def volume(self):
        """
        Get the volume of the box
        """
        d = self.max.subtract(self.min)
        return d.x*d.y*d.z    # Return the volume

    def getRandomPoint(self):
        """
            Get a random point in the bounding box as a Vector3d.
        """
        x = random.uniform(self.min.x,self.max.x)
        y = random.uniform(self.min.y,self.max.y)
        z = random.uniform(self.min.z,self.max.z)
        return Vector3d(x,y,z)


def main():
    """    Main program to do the simulation"
    """

    file = open(str(input("File : ")),"r")   # Open file
    mol = Molecule().fromFile(file)              # Read in molecule
    print("Molecule is \n" + str(mol))           # Print out info
    box = BoundingBox(mol)                       # Form Bounding box

    maxpoint = float(input("Number of points : ")) # Max number of points
    plotInterval = maxpoint/100                    # Plot internal for monitoring
    xData = []                                     # Data liost for graph
    yData = []

    # counters for number inside box total number of time round loop
    inside = 0
    p = 0

    while p < maxpoint:                          # Loop counting internal points
        p += 1
        # Test if a random point is inside the molecule
        if mol.inInside(box.getRandomPoint()):
            inside += 1

        if p % plotInterval == 0:               # Store graphical data (100 point only)
            xData.append(p)
            yData.append(box.volume()*inside/p)

    estimate = box.volume()*inside/p            # Print out final estimage
    print("Final estimate is : " + str(estimate))


    plt.plot(xData,yData)                       # Draw graph (with default plot)
    plt.ylim(0.9*estimate,1.1*estimate)
    plt.title("Estimate of volume for " + str(maxpoint) + " points.")
    plt.show()

main()


