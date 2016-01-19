#Created by: Eric Dockery
# Triangle Designer
# take clicks from the mouse and form a tringle
# using three points
from graphics import *
from math import *
def main():
    print ( "Triangle Designer")

    win=GraphWin("Triangles",500,500)
    print ("Click the first point for your triangle")
    p1= win.getMouse()
    print ("Click the second point for your triangle")
    p2= win.getMouse()
    print ("Click the last point for your triangle")
    p3=win.getMouse()
    
    cir1=Circle(p1,5)
    cir1.setFill("yellow")
    cir1.draw(win)
    cir2=Circle(p2,5)
    cir2.setFill("yellow")
    cir2.draw(win)
    cir3=Circle(p3,5)
    cir3.setFill("yellow")
    cir3.draw(win)

    tri1=Polygon(p1,p2,p3)
    tri1.setFill("red")
    tri1.draw(win)

    x1=p1.getX()
    y1=p1.getY()
    x2=p2.getX()
    y2=p2.getY()
    x3=p3.getX()
    y3=p3.getY()

    a= sqrt( (x2-x1)**2+(y2-y1)**2)
    b= sqrt( (x3-x2)**2+(y3-y2)**2)
    c= sqrt( (x1-x3)**2+(y1-y3)**2)

    perimeter=  a+b+c
    print ( "The perimeter of the triangle is ", perimeter)

    s= (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print( "Ther area of the triangle is ", area)

    print( "click to end")
    win.getMouse()
    win.close()

main()
