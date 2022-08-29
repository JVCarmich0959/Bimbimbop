# Write a program that lets the user input the initial height of the ball as a float, the bounciness index of the ball as a float,
# and the number of times the ball is allowed to continue as an int.
# Calculate the total distance traveled by the ball using the user inputs
# print the output of the total distance traveled by the ball.
# Note that the distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance as the ball comes back up.

import math # import the math module


def main():
    height = float(input("Enter the height from which the ball is dropped: ")) # get the initial height from the user
    bounciness = float(input("Enter the bounciness: ")) # get the bounciness index from the user
    bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: ")) # get the number of times the ball is allowed to bounce from the user
    distance = 0 # initialize the distance traveled to 0
    for i in range(bounces): # for each bounce
        distance += height # add the height to the distance traveled
        height = 0.6 * height # calculate the height of the ball after the bounce
        if height < 0.5: # if the height is less than 0.5
            height = 0.5 # set the height to 0.5
    print("Total distance traveled is: ", distance) # print the total distance traveled


main() # call the main function to run the program


