# Write a program that takes the radius of a sphere ( a floating-point number)
# as input and then outputs the sphere's:
# Diameter, Circumference, Surface Area, Volume.
# in that order, separated by spaces.

import math  # import the math module


def main():
    radius = float(input("Enter the radius of the sphere: ")) # get the radius from the user
    diameter = radius * 2  # calculate the diameter
    circumference = 2 * math.pi * radius # calculate the circumference
    surface_area = 4 * math.pi * radius ** 2 # calculate the surface area
    volume = 4 / 3 * math.pi * radius ** 3 # calculate the volume
    print("Diameter:", diameter) # print the diameter
    print("Circumference:", circumference) # print the circumference
    print("Surface Area:", surface_area) # print the surface area
    print("Volume:", volume) # print the volume


main() # call the main function to run the program










