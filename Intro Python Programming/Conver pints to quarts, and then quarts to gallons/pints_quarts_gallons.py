# Prolog
# Author: Eric Dockery
# Section: 001
# Date: 1/20/12
# Purpose:
#   Program to find the number of quarts and gallons in a given number of pints.
#   Preconditions: (input)
#       User supplies number of pints (as numbers, no error checking done)
#   Postconditions: (output)
#           User asked how many pints
#           Number of quarts displayed
#           Number of gallons displayed
####    Design
#   1. ask the user for the number of pints
#   2. calculate the number of quarts using the formula (pints / 2)
#   3. calculate the number of gallons using the formula ( quarts / 4)
#   4. output the results with appropriate phrase

from math import *

def main():
    pints = eval(input ( "How many pints? "))
    quarts= (pints /2) # number of quarts
    gallons=(quarts / 4 ) # number of gallons
    print (pints, "pints is", quarts,"quarts")
    print (quarts, "quarts is", gallons, "gallons")

main() 
