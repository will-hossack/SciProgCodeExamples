"""
    Example program to plot out the current and phase for a LRC circuit in two plots
    
    Physics student will see the theory in Physics of Fields next semester.
    
    Try values of:
    Resistor = 0.1
    Capacitor = 0.001
    Inductor = 0.02
    
"""

import cmath
import math
import matplotlib.pyplot as plt

def impedance(resistor,capacitor,inductor,omega):
    """
    Calculate the complex impedance  of a LRC circuit using complex numbers and return
    as a complex
    """
    return resistor + complex(0,-1.0/(capacitor*omega)) + complex(0,inductor*omega)
 
def main():
    
    #        Ask for the three values
    resistor = float(input("Resistor : "))
    capacitor = float(input("Capicitor : "))
    inductor = float(input("Inductor : "))
    
    # Calcuate resonance and quality factors for the circuit and print them out.
    resonance = 1.0/math.sqrt(capacitor*inductor)
    quality = math.sqrt(inductor/capacitor)/resistor
    print("Resonance " + str(resonance) + " Quality : " + str(quality))
    
    # Calcualte the range of the plot with resonance freq at the centre.
    npoints = 300
    omegaMin = 0.5*resonance 
    omegaMax = 1.5*resonance
    domega = (omegaMax - omegaMin)/npoints  # Separations betewen points 

    #          Thee empty lists to hold the data to be plotted
    omegaData = [] 
    modData = []
    phaseData = []

    #           Fill the three data lists
    for i in range(0,npoints + 1):
        omega = omegaMin + i*domega          # calcuate omega
        omegaData.append(omega)              # store in list
        #       Get complex impedance
        z = impedance(resistor,capacitor,inductor,omega)
        modData.append(1/abs(z))             # Store Current = 1/abs(z)
        phaseData.append(cmath.phase(z))     # Store Phase
        
    
    #     To the plotting
    plt.subplot(2,1,1)              # Make upper subplot
    plt.plot(omegaData,modData)     # Plot in upper graph
    plt.title("LRC with resonance: {0:5.3f} quality: {1:5.3f}".format(resonance,quality))
    plt.ylabel("Current")
    plt.grid()
    plt.subplot(2,1,2)             # Make lower subplot
    plt.plot(omegaData,phaseData)  # Plot in lower graph
    plt.xlabel("Angular Frequency")
    plt.ylabel("Phase")
    plt.grid()
    plt.show()                     # Show the two plots
    
    
main()