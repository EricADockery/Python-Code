# Name: Eric Dockery
# Section: 01
# Email: eric.dockery283@hotmail.com
#Purpose:
#   Input 3 observers' locations and calculate where a lightouse is
#   based on a circle, find the center and the radius.
# Preconditons: (input)
#   Enter the x and y of the first observer:
#   Enter the x and y of the second observer:
#   Enter the x and y of the third observer:
# Postconditions: (output)
#   Supply program prolog
#   Restate the three observers points
#   Calculate and show the center of the circle
#   Calculate and show the radius of the circle
# Design:
from math import *
def main():
    #1. Display introductory message.

    print ("****Lighthouse Location Calculator****")

    print ("")

    #2. Ask user to enter the x and y cordinates of the first observer.

    a, b= eval( input( "Enter the x and y of the first observer: "))

    #3. Ask user to enter the x and y cordinates of the second observer.

    c, d= eval( input( "Enter the x and y of the second observer: " ))

    #4. Ask user to enter the x and y cordinates of the third observer.

    e, f = eval(input( "Enter the x and y of the third observer: " ))

    #5. Calculate the center of the circle using the distance formula
    #   on a given point and the center

    X = 0.5 *(((a**2+b**2)*(f-d)+(c**2+d**2)*(b-f)+(e**2+f**2)*(d-b)) \
              /((a*(f-d))+(c*(b-f))+(e*(d-b))))

    Y = 0.5 *(((a**2+b**2)*(e-c)+(c**2+d**2)*(a-e)+(e**2+f**2)*(c-a))\
              /((b*(e-c))+(d*(a-e))+(f*(c-a))))
    

    #6. Calculate the radius of the circle using the distance formula
    #    using one of the given points and the coordinates of the center
    r = sqrt( (a-X)**2+(b-Y)**2)

    #7. Output to the shell the location of all observers.

    print ("")

    print ("The three observers are at")
    
    print ((a,b))

    print ((c,d)) 

    print ((e,f))

    print ("")

    #8. Output to the shell the location of the center of the circle

    print( "The center of the circle is at", ( X, Y))

    #9. Output to the shell the radius of the circle.

    print( "The radius of the circle is ", r)

main ()
