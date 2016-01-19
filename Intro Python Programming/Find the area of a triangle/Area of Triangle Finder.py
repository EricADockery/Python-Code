#Name: Eric Dockery
#Section: 01
#Email: eric.dockery283@hotmail.com

from math import *
def main():
    total_A=0
    n=0
    for i in range (3):
        a=eval(input("Enter side of triangle: " ))
        area=sqrt(3)/4*(a**2)
        print ("Area of the triangle is ", round(area,10-n))
        n=n+1
        print ("")
        
        total_A= total_A+area
    print( "Total area is ", round(total_A,8))
main()
        
