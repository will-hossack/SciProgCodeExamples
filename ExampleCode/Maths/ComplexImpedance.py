"""
   Exmaple to deminstrate the use of complex maths to calcalate the impedance
   of a LRC circuit.

   See fully plotting program ImpedancePlot.py in Plotting section.
   You will also see the theory for this in Physics of Fields in semesterv 2

"""

import cmath        # Import complex

def main():

    #     Get values as floats
    resistor = float(input("Resistor : "))
    capacitor = float(input("Capicitor : "))
    inductor = float(input("Inductor : "))
    frequency = float(input("Frequency : "))
    omega= 2*cmath.pi*frequency     # angular freqiency (note cmath.pi is a float)

    #    Form complex impedance using complex numbers
    z = resistor + complex(0,-1.0/(capacitor*omega)) + complex(0,inductor*omega)
    print("Complex impedance is : " + str(z))

    #    Calculate modulus and phase of complex number
    modulus = abs(z)
    phase = cmath.phase(z)
    print("Modulus is : " + str(modulus) + " phase is : " + str(phase))


    #   Run the program
main()