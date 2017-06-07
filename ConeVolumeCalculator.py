# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)

from math import pi

# Define Function below

def calculateConeVolume(r,h):
    return round(pi * (r**2) * (h / 3),2)

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
