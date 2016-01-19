#Name: Eric Dockery
#Date: 2/08/12
#Section: 01
#Email: eric.dockery283@hotmail.com
#Purpose:
#   Manipulation of the graphics libary to produce a graphical image of a
#   building.
#Preconditions:
#   No preconditions
#Postconditions:
#   Code will produce the graphical image of a building
#   Shell statement of "click to end program"
#
#Design:
from graphics import *
def main ():
    
    win= GraphWin( "Erics' House", 500, 500)
    win.setBackground("lightblue")

    circ1= Circle(Point(250,600), 250)
    circ1.setFill("darkgreen")
    circ1.setOutline("yellow")
    circ1.draw(win)

    Body= Rectangle(Point(100,400),Point(385,200))
    Body.setFill("blue")
    Body.draw(win)

    Door= Rectangle(Point(225,400),Point(250,350))
    Door.setFill("black")
    Door.draw(win)

    Doorknob= Circle(Point(245,380),2)
    Doorknob.setFill("gold")
    Doorknob.draw(win)

    Window1=Rectangle(Point(310,335),Point(340,365))
    Window1.setOutline("orange")
    Window1.setWidth(3)
    Window1.setFill("white")
    Window1.draw(win)

    Window1line1= Line(Point(325,365),Point(325,335))
    Window1line1.setWidth(3)
    Window1line1.setFill("orange")
    Window1line1.draw(win)

    Window1line2= Line(Point(310,350),Point(340,350))
    Window1line2.setWidth(3)
    Window1line2.setFill("orange")
    Window1line2.draw(win)

    Window2=Rectangle(Point(130,335),Point(160,365))
    Window2.setOutline("orange")
    Window2.setWidth(3)
    Window2.setFill("white")
    Window2.draw(win)

    Window2line1= Line(Point(130,350),Point(160,350))
    Window2line1.setWidth(3)
    Window2line1.setFill("orange")
    Window2line1.draw(win)

    Window2line2= Line(Point(145,335),Point(145,365))
    Window2line2.setWidth(3)
    Window2line2.setFill("orange")
    Window2line2.draw(win)


    Window3=Rectangle(Point(130,250),Point(160,280))
    Window3.setOutline("orange")
    Window3.setWidth(3)
    Window3.setFill("white")
    Window3.draw(win)
    
    Window3line1= Line(Point(130,265),Point(160,265))
    Window3line1.setWidth(3)
    Window3line1.setFill("orange")
    Window3line1.draw(win)

    Window3line2= Line(Point(145,250),Point(145,280))
    Window3line2.setWidth(3)
    Window3line2.setFill("orange")
    Window3line2.draw(win)
    
    Window4=Rectangle(Point(310,250),Point(340,280))
    Window4.setOutline("orange")
    Window4.setWidth(3)
    Window4.setFill("white")
    Window4.draw(win)

    Window4line1= Line(Point(310,265),Point(340,265))
    Window4line1.setWidth(3)
    Window4line1.setFill("orange")
    Window4line1.draw(win)

    Window4line2= Line(Point(325,250),Point(325,280))
    Window4line2.setWidth(3)
    Window4line2.setFill("orange")
    Window4line2.draw(win)
    

    Slide1=Rectangle(Point(240,230),Point(210,300))
    Slide1.setOutline("orange")
    Slide1.setWidth(3)
    Slide1.setFill("black")
    Slide1.draw(win)
    
    Slide2=Rectangle(Point(240,230),Point(270,300))
    Slide2.setOutline("orange")
    Slide2.setWidth(3)
    Slide2.setFill("black")
    Slide2.draw(win)

    rail1= Line(Point(210,280),Point(270,280))
    rail1.setWidth(3)
    rail1.setFill("green")
    rail1.draw(win)
    
    rail2= Line(Point(210,300),Point(270,300))
    rail2.setWidth(3)
    rail2.setFill("green")
    rail2.draw(win)
    
    rail3= Line(Point(210,300),Point(210,280))
    rail3.setWidth(3)
    rail3.setFill("green")
    rail3.draw(win)

    rail4= Line(Point(270,300),Point(270,280))
    rail4.setWidth(3)
    rail4.setFill("green")
    rail4.draw(win)
    
    rail5= Line(Point(230,300),Point(230,280))
    rail5.setWidth(3)
    rail5.setFill("green")
    rail5.draw(win)

    rail6= Line(Point(260,300),Point(260,280))
    rail6.setWidth(3)
    rail6.setFill("green")
    rail6.draw(win)

    rail7= Line(Point(250,300),Point(250,280))
    rail7.setWidth(3)
    rail7.setFill("green")
    rail7.draw(win)

    rail8= Line(Point(240,300),Point(240,280))
    rail8.setWidth(3)
    rail8.setFill("green")
    rail8.draw(win)

    rail9= Line(Point(220,300),Point(220,280))
    rail9.setWidth(3)
    rail9.setFill("green")
    rail9.draw(win)

    Roof= Polygon(Point(85,200),Point(245,50),Point(400,200))
    Roof.setFill("orange")
    Roof.setOutline("black")
    Roof.draw(win)

    Moon= Circle(Point(70,50),40)
    Moon.setFill("lightgray")
    Moon.draw(win)
    
    Cloud1= Circle (Point(50,75),20)
    Cloud1.setFill("white")
    Cloud1.draw(win)

    Cloud2= Circle (Point(65,70),20)
    Cloud2.setFill("white")
    Cloud2.draw(win)

    Cloud3= Circle (Point(45,60),20)
    Cloud3.setFill("white")
    Cloud3.draw(win)

    Cloud4= Circle (Point (52,70),20)
    Cloud4.setFill("white")
    Cloud4.setOutline("white")
    Cloud4.draw(win)
    

    Cloud5= Circle (Point (30,75),20)
    Cloud5.setFill("white")
    Cloud5.draw(win)
    
    Cloud6= Circle (Point (45,70),20)
    Cloud6.setFill("white")
    Cloud6.setOutline("white")
    Cloud6.draw(win)

    Cloud7= Circle (Point(90,75),20)
    Cloud7.setFill("white")
    Cloud7.draw(win)

    Cloud8= Circle (Point(105,70),20)
    Cloud8.setFill("white")
    Cloud8.draw(win)

    Cloud9= Circle (Point(85,60),20)
    Cloud9.setFill("white")
    Cloud9.draw(win)

    Cloud11= Circle (Point (92,70),20)
    Cloud11.setFill("white")
    Cloud11.setOutline("white")
    Cloud11.draw(win)
    

    Cloud10= Circle (Point (70,75),20)
    Cloud10.setFill("white")
    Cloud10.draw(win)
    
    Cloud12= Circle (Point (85,70),20)
    Cloud12.setFill("white")
    Cloud12.setOutline("white")
    Cloud12.draw(win)
    
    print ("click to end program")
    win.getMouse()
    win.close()

    
main () 
                  
