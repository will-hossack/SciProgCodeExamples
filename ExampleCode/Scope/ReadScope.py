""""
    Example to show reading a global variable across main and a function.
    Note in this case wavelength is only read and not altered; 
    
    This is a possible use for a global but in this case it is better style and easier
    to follow, if wavelength was are agrument to the function planck() and was passed
    in from main()
"""
import math
wavelength = 0.65          # Define a global float



def planck(temperature):
    c_one = 5.029e6               #     2 h c^2 
    c_two = 1.44e4                #     hc/k
    #
    #            Can access wavelength inside function
    val = c_one/math.pow(wavelength,5)*(1.0/(math.exp(c_two/(wavelength*temperature)) - 1.0))
    return val

    

def main():
    #
    #           Can access wavelength inside main
    print("Plank intensity at : " + str(wavelength))
    for t in range(300,340):
        val = planck(t)
        print("Value at : " + str(t) + " is " + str(val))

main()
