#Prolog
# Author: George Grote
#Section 001
# 1/22/12
# Purpose: Program to convert pints to quarts, and quarts to gallons
# Preconditions (input)
#       User supplies the number of pints
# Postconditions (output)
#       User is given the number of quarts and gallons based on number of pints

#Goal: Calculate the number of quarts and gallons in a given number of pints.

#  1. Get the needed piece of data, number of pints.
def main():
    pints = eval( input( " How many pints? "))
# 2. Calculate (and store) number of quarts by dividing pints by 2. (2 pints in a quart)
    quarts = pints / 2
    
#3. Calculate (and store) number of gallons by dividing quarts by 4. (4 quarts in a gallon)
    gallons = quarts / 4
    
#4. Output the results of the calculations

    print ( pints, "pints is ", quarts, " quarts." )
    print ( quarts, "quarts is ", gallons, "gallons.")

main()
