# Name: Eric A Dockery
# Date: 2/22/2012
# Section: 01
# Email: eric.dockery283@hotmail.com
#Purpose:
    #Program to receive three points, draw their endpoints and draw a triangle
    #connecting them and a inverse image, aslo desplay the perimeter and area
    #of the triangles, five times. Then add up and display the total area and perimeter
    #of the triangles and reflected ones.
#Preconditions: (input)
    # user will click to input where the points of the triangles.
#Postconditions: (output)
    #Display title
    #A blank line is shown
    #Ask for the first, second and third point of trianles
    #Draw each point with click with a yellow circle.
    #A blank line is shown
    #Display perimeter of each triangles
    #Display the area of the first triangle
    #A blank line is shown.
    #Repeat steps above 5 times
    #Show the total of the perimeters and areas of triangles and reflected ones
#Design:
from graphics import *
from math import *
def main():
        #1. print "Triangle Designer" title on shell
    print ("Triangle Designer")
        #2. Draw a Graphics window labeled "Triangles" with length of 400 and
            #width of 400.
    win=GraphWin("Triangles",400,400)
        #3 Set total area, total perimeter, and number of triangles equal to zero.
    tri=0
    totalP1=0
    totalarea=0
        #4 Create a loop for 5 triangles using a list of colors that are used.
    for i in ["red","blue","green","pink","black"]:
            #4.1 print ("Click the first point for triangle", loop number)
        tri=tri+1
        print ("Click the first point for triangle",tri)
                #a draw a circle on the first point given by user
        p1=win.getMouse()
        cir1= Circle(p1,5)
        cir1.setFill("yellow")
        cir1.draw(win)
            #4.2 print ("Click the second point for triangle", loop number)
        print("Click the second point for triangle",tri)
                #b draw a circle on the second point given by user
        p2=win.getMouse()
        cir2=Circle(p2,5)
        cir2.setFill("yellow")
        cir2.draw(win)
            #4.3 print ( "Click the last point for triangle", loop number)
        print("Click the last point for triangle",tri)
                #c draw a circle on the last point given by user
        p3=win.getMouse()
        cir3=Circle(p3,5)
        cir3.setFill("yellow")
        cir3.draw(win)
            #4.4 print a space seperating the strings from future strings
        print("")
            #4.5 Draw triangle with set color on loop.
        tri1=Polygon(p1,p2,p3)
        tri1.setFill(i)
        tri1.draw(win)
            #4.6 Calculate the x and y for each point and determine the
            # perimeter and area of triangles
        a=p1.getX()
        b=p1.getY()
        c=p2.getX()
        d=p2.getY()
        e=p3.getX()
        f=p3.getY()
        
        da1=sqrt( (c-a)**2 +(d-b)**2)
        db1=sqrt( (e-c)**2+(f-d)**2)
        dc1=sqrt( (e-a)**2+(f-b)**2)
    
        P1= da1+db1+dc1

        s= (da1+db1+dc1)/2
        area1=sqrt(s*(s-da1)*(s-db1)*(s-dc1))

            #4.7 Draw the mirrior image of the triangles over the x=y axis
        tri2=Polygon(Point(b,a),Point(d,c),Point(f,e))
        tri2.setFill(i)
        tri2.draw(win)
            #4.8 print ("The perimeter of triangle",loop number, "is", perimeter)
        print("The perimeter of triangle",i,"is" , P1)
            #4.9 print ("The area of triangle",i, "is", area)
        print( "The area of triangle",i,"is", area1)
            #4.10 print space between all triangles in loop.
        print("")
            #4.11 caculate the total perimeter and area of all triangles and
            #their mirrior image.
        totalP1= totalP1+P1*2
        totalarea=totalarea+area1*2
        #5 print ("The total perimeter of all triangles including reflected ones,
        #is",totalperimeter)
    print ("The total perimeter of all triangles,",totalP1,"", end="")
    print("including reflected ones, is" )
        #6 print ( The total area of all triangles, including reflected ones,
        #is", totalarea)
    print ("The total area of all triangles,",totalarea,"", end="")
    print ("including reflected ones, is" )
        #7 print ("Click one more time to close")
    print("Click one more time to close")
    win.getMouse()
    win.close()
main()
        
        
