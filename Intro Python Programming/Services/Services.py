# Name: Eric Dockery
# Date: 3/7/2012
# Section: 01
# Email: eric.dockery283@hotmail.com
# Purpose:
    # using if statements to calculate a bills total
# Preconditions:
    # user will input a y or n for each service wanted.
# Postconditions:
    #Program will sum the totals of each service and thank the costumer.
    # Assuming only y or n answers.
# Design:

def main():
    #1 Set values for each type of wash
    bew=15
    eed=15
    cw=5
    vf=10
    #2 Print out the choice options
    print("Enter your choices as y or n.")
    print()
    #3 Set total to 0
    z=0
    #4 Ask if user wants Basic Exterior Wash and if y add to total
    x=input ("Do you want a Basic Exterior Wash? ")
    if x== "y":
        z=z+bew
    #5 Ask if user wants Extra Exterior Detailing and if y add to total
    y= input ("Do you want a Extra Exterior Detailing? ")
    if y== "y":
        z=z+eed
    #6 Ask if user wants Windows Cleaning and if y add to total
    c= input ("Do you want Windows Cleaning? ")
    if c== "y":
        z=z+cw
    #7 Ask if user wants Vacumming and if y add to total
    a= input("Do you want Vacumming? " )
    if a== "y":
         z=z+vf
    #8 Print the total for the services and thank the user for its business
    print()
    print ("The total for your services is ","$", z,".",sep="")
    print( "Thank you for your business!")
main()

          
