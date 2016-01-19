# Purpose To take eight points (two lines), find the intersection point, and display
# this data in a graphics window.
# Preconditions: The user must enter eight points. (x1, y1), (x2, y2) for both lines.
# Postconditions: To calculate two slopes, two y-intercepts, show equations for both lines,
# then show the intersecting point between the two lines.

from graphics import *
def main ():
    print("The Great Intersection Finder")
    print()
    win= GraphWin( "Lab6window", 400,500)
    #Point one and two for line one.
    print("Enter the x and y for the first point on line 1")
##    line1point1x, line1point1y = eval(input("X1, Y1  "))
    line1point1=win.getMouse()
    circ1= Circle(line1point1,3)
    circ1.setFill("red")
    circ1.draw(win)
    line1point1x=line1point1.getX()
    line1point1y=line1point1.getY()
    print("Enter the x and y for the second point on line 1")
    
##    line1point2x, line1point2y = eval(input("X2, Y2  "))
    line1point2=win.getMouse()
    line1point2x=line1point2.getX()
    line1point2y=line1point2.getY()

    circ2= Circle(line1point2,3)
    circ2.setFill("red")
    circ2.draw(win)
    # first line
    line= Line(line1point1,line1point2)
    line.draw(win)



    
    
    #Point one and two for line two.
    print("Enter the x and y for the first point on line 2")
##    line2point1x, line2point1y = eval(input("X1, Y1  "))
    line2point1=win.getMouse()
    circ3= Circle(line2point1,3)
    circ3.setFill("red")
    circ3.draw(win)

    line2point1x=line2point1.getX()
    line2point1y=line2point1.getY()
    print("Enter the x and y for the second point on line 2")
##    line2point2x, line2point2y = eval(input("X2, Y2  "))
    line2point2=win.getMouse()
    line2point2x=line2point2.getX()
    line2point2y=line2point2.getY()

    line= Line(line2point1,line2point2)
    line.draw(win)

    
    circ4= Circle(line2point2,3)
    circ4.setFill("red")
    circ4.draw(win)
    #Calculating the slopes of the lines.
    line1slope = (line1point2y - line1point1y) / (line1point2x - line1point1x)
    line2slope = (line2point2y - line2point1y) / (line2point2x - line2point1x)

    #Calculating the y-intercepts of the lines.
    # y1 - m * x1
    line1yint = line1point1y - (line1slope * line1point1x)
    line2yint = line2point1y - (line2slope * line2point1x)

    #Calculate where the two lines intersect.
    intersectx = (-line1yint + line2yint) / (line1slope - line2slope)
    intersecty = line1yint + (line1slope * intersectx)
    cir5= Circle(Point(intersectx,intersecty),5)
    cir5.setFill("green")
    cir5.draw(win)
    #Show what line 1 and 2 points are, their lines, and point of intersection.
    print("Line 1: (", line1point1x, ",", line1point1y,") and (", line1point2x, ",", line1point2y,")")
    print("Equation of Line 1: y =", line1slope,'x + ', line1yint)
    print("Line 2: (", line2point1x, ",", line2point1y,") and (", line2point2x, ",", line2point2y,")")
    print("Equation of Line 2  y =", line2slope,'x + ', line2yint)
    print()
    print("Point of intersection = ( ", intersectx,",", intersecty, ")")
    print()

    print("Click to end")
    win.getMouse()
    win.close()
main()  
    
           
