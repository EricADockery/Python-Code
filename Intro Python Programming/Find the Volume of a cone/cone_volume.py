# Prolog
# Author:  Eric Dockery
# Section: 001
# Date:   1/18/2012
# Purpose:
#  Program to find the volume of a right cone given the length
#       of the radius of the base and the height
# Preconditions: (input)
#       User supplies radius and height of the cone (as numbers, no error checking done)
# Postconditions:  (output)
#       User greeted with a message
#       Cone volume displayed
#### Design
#   1. greet the user
#   2. ask the user for the radius and height and read them in
#   3. calculate the area using the formula for volume (pi * radius * radius * height  / 3)
#   4. output the results with an appropriate label


from math import *

def main():
    print ("Hello Human!")
    radius = eval(input("Enter the radius of the base of the cone "))
    height = eval(input("Enter the height of the cone "))
    volume = pi * radius * radius * height / 3  # volume of a cone
    print ("The volume of the cone is ", volume)

main ()
