"""
   Program to extimate the volume of a sphere by counting the
   number of randon point that fall inside compated with the
   number of points in a box round the sphere.
"""
import math
import random


def random_point(max_range):
    """
    Return a random 3d poin in range +/max_range
    """
    x = random.uniform(-max_range,max_range)
    y = random.uniform(-max_range,max_range)
    z = random.uniform(-max_range,max_range)

    return x,y,z

def point_in_sphere(radius,x,y,z):
    """
    Check of a point is within a sphere specified.
    """
    if x*x + y*y + z*z <= radius*radius:
        return True
    else :
        return False

def main():
    """
    Main program
    """
    
    points = int(input("Number of points : "))        # Ask for initial conditions
    radius = float(input("Radius of sphere : "))
    
    #               Counters for number inside and look variable
    inside, p  = 0 , 0
    while p <= points:                     # Loop over number of trial points
        x,y,z = random_point(radius)       # Random point in cube round sphere
        if point_in_sphere(radius,x,y,z) : # Is it inside, if so count it
            inside += 1
        p += 1 

    #         Estimated volume is given by ratio of number of points inside
    #         times volume of cube round sphere
    #
    estimate = float(inside)/float(points)*math.pow(2*radius,3)
    vol = 4.0*math.pi*math.pow(radius,3)/3.0

    print("Estimate volume is : " + str(estimate) + " real volume is : " + str(vol))


main()
