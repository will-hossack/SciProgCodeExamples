"""
   Program to plot the Plack radiation spectrum with the Plank radiation
   spectrun as a function.
"""
import math
import matplotlib.pyplot as plt


def planck_spectrum(temperature,wave_length):
    """
    Function to calcualte the black body plank spectrum with parameters:
    param: temperture float the temperture in Kelvin   
    param: wave_length float the wave_length in microns
    return float the planks spectrum value
    """
    c_one = 5.029e6               #     2 h c^2 
    c_two = 1.44e4                #     hc/k

    val = c_one/math.pow(wave_length,5)*(1.0/(math.exp(c_two/(wave_length*temperature)) - 1.0))
    return val
    
def planck_data(temperature,wave_list):
    """
    Function to return a list of plank specturn values for the specified temperture
    values and the wave lengths supplied in the list.
    param: temperature float temperature in Kelvin
    param: wave_list, list of floats, the wavelengths
    return: float list of planck spectrum values the same length as wave_list
    """
    data = []
    for wavelength in wave_list:
        planck = planck_spectrum(temperature,wavelength)
        data.append(planck)

    return data

def main():
    """
    Plot out the Planck spectrum for a specified temperture
    """

    temperature = float(input("Temperature : "))
    npoint = 100
    short_wavelength = 0.25
    long_wavelength = 2.0
    delta_wavelength = (long_wavelength - short_wavelength)/npoint


    #       Make the wavelength list
    wavelength = short_wavelength
    wave_list = []
    while wavelength <= long_wavelength:
        wave_list.append(wavelength)
        wavelength += delta_wavelength
    
    #       Get the planck values in a list  
    planck_list = planck_data(temperature,wave_list)

    #       Do a baic plot
    plt.plot(wave_list,planck_list,"r")
    plt.show()

    
main()
