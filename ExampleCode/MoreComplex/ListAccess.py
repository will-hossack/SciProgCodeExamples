"""
     A more advanced program that shown news ways to access list data
     without using the range() function. 

"""

import math

def main():
    
    
    #        Create a list of numbers fro 0->4pi 
    #
    nPoints = 50
    thetaData = []
    theta = 0.0
    maxTheta = 4*math.pi
    dtheta = maxTheta / nPoints
    
    while theta < maxTheta:
        thetaData.append(theta)
        theta += dtheta
     
    # Assess the list with the enumerate function that returns the 
    # element index and element value as a two element truple
    for i,theta in enumerate(thetaData):
        print("Element : " + str(i) + " has value : " + str(theta))
        
        
    #     Make a second list of cos Data        
    cosData = []    
    for theta in thetaData:
        cos = math.cos(theta)
        cosData.append(cos)
        
    #     Now access the two list in parallel with the zip function
    #     to merge them into truples, one from each list.              
    for theta,cos in zip(thetaData,cosData):
        print("Theta: " + str(theta) + " Cos(theta) " + str(cos))
          
        
main()