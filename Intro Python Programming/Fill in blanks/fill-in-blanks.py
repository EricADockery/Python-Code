#  Fill in the blanks in the code below.

from graphics import *

def main():
    # read scores from file, 0 through 9
    # produce a bar chart which has a
    #     bar for each number 0-9, which is as tall as
    #     the number of that score seen in the file
    #  must have a list of 10 counters, one for each score
    
    counts = [0] * 10     # counters for each score
    inf = open("scores.txt", "r" )  # for reading
    for line in inf:  # assumed one number per line
        score = int(line)
        counts[score]=counts[score]+1 # add one to appropriate counter
                   # previous line does NOT require an if!
    inf.close()
    win = GraphWin("Bar Chart", 500, 600)
    win. setCoords (-1, -3, 11, max(counts) + 5)
                   # previous line sets origin point and scale

    for i in range(10):
        r = Rectangle(Point(i, counts[i]), Point(i+1, 0))
        r.setFill("blue")
        r.draw(win)

    for i in range(10):
        t = Text(Point(i+.5, -1), str(i))
        t.draw(win)

    print("click to close window")
    win.getMouse()
    win.close()

main()
    
        
