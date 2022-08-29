# A program that finds the slope of a line given two points
# and finds the point-slope from of the line given two points
# and finds the slope-intercept of the line given two points
# And finds the standard from Ax+By=C


import math # import the math module


def main():
    x1 = float(input("Enter the x1: ")) # get the x1 from the user
    y1 = float(input("Enter the y1: ")) # get the y1 from the user
    x2 = float(input("Enter the x2: ")) # get the x2 from the user
    y2 = float(input("Enter the y2: ")) # get the y2 from the user
    print("The slope of the line is: ", (y2-y1)/(x2-x1)) # print the slope of the line
    print("The point-slope form of the line is: ", y1/x1, "x+", y2/x2) # print the point-slope form of the line
    print("The slope-intercept form of the line is: ", (y2-y1)/(x2-x1), "x+", (y1*x2-y2*x1)/(x2-x1)) # print the slope-intercept form of the line
    print("The standard form of the line is: ", (y2-y1)/(x2-x1), "x+", (y1*x2-y2*x1)/(x2-x1), "=0") # print the standard form of the line


main() # call the main function to run the program




