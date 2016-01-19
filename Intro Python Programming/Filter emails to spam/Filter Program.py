# Name: Eric Dockery
# Date: 3/7/2012
# Section: 01
# Email: eric.dockery283@hotmail.com

#Purpose:
    # Create a program that will intake a file of emails and filter the spam
    # emails using a preset coded guide.
#Preconditions:
    #User will enter the name of the file that is to be filtered.
    #User will give their email address
#Postconditions:
    # Program will take the email that was sent and either inport them into the
        #file accepted or the file rejected based on the guidelines:
        #if the From line shows it is from anywhere in New Zealand,
            #add 10 to the score. (country code for New Zealand is .nz)
        #if the To line shows that it is not addressed to the person filtering
        #if the first character of the From line is a digit, add 30 to the score.
        #if the Subject line contains the word "large", add 10 to the score.
        #if the Subject line contains the word "money", add 20 to the score.
        #if the To line contains more than one address (hint - a comma would
            #be between the addresses), add 20 to the score.
    # The total score of the file will be accepted if the file is less than
        # or equal to 30 pts.
    # The total of the emails filtered will be displayed.
    # The total of the emails accepted.
    # The total of the emails rejected.
    # The average score of the emails in the file will be displayed.
#Design:
    # Prepare for graphics
from graphics import *
def main():
    #1 Ask for input file name
    InputFileName = input("Enter a file name: ")
    #2 open input file
    InputFile = open(InputFileName,'r')
    #3 open rejected email file to output into
    rej= open("rejected.txt","w")
    #4 open accepted email file to output into
    accp= open("Goodones.txt", "w")
    #5 Ask for users email
    youremail= input("What is your email?")
    #6 Set accumulator totals

    #7 Set a email score total to zero
    total=0
    #8 Set a rejected email counter to zero
    rejcnt=0
    #9 Set a accepted email counter to zero
    accpcnt= 0
    #10 set a email total score sum to zero
    totalsum=0
    #11 Set list counter for scores
    Graphicschart= [0]*11
    #12 use a for loop for input file:
    for line in InputFile:
        #12.1 This returns the From line
        
        #use if line.find(".nz) returns greater than -1 add 10 to total
        rule1=line.find(".nz")
        if rule1 > -1:
            total+=10
        #12.2 use if line.find rule3[0].isdigit() true add 30 to total
        rule3=line
        rule3_1=rule3[0]
        if rule3_1.isdigit():
            total+=30
        #12.3 use readline the To line in file
        nextline=InputFile.readline()
        #12.4 use if Toline.find( Youremail) is -1 add 10 to total
        rule2=nextline.find(youremail)
        if rule2 == -1:
            total+=10
        #12.5 use if to find (",") if >-1 add 20 to total
        rule6=nextline.find(",")
        if rule6 > -1:
            total+=20
        #12.6 use readline to find Subject line in email
        lastline=InputFile.readline()
        #12.7 use find("large") and if > -1 add 10 to total
        rule4=lastline.find("large")
        if rule4 > -1:
            total+=10
        #12.8 use find ("money) and if > -1 add 20 to total
        rule5=lastline.find("money")
        if rule5 > -1:
            total+=20
        #12.9 if total <= 30 output into accepted file and count the
        #file to rejected total and show on shell
        if total <= 30:
            print(line, end="")
            print(" Accepted, Score=", total)
            print(line,nextline,lastline, "Score = ", total,sep="",file=accp)
            accpcnt+=1
        
        #12.10 else total < 30 output into accepted file and count the
        # file to accepted total and show on shell
        else:
            print(line, end= "")
            print(" Rejected, Score=", total)
            print(line,nextline,lastline, "Score = ", total,sep="",file=rej)
            rejcnt+=1
        #12.11 Sum the total to totalsum counter and the  score counter
        Graphicschart[total//10]=Graphicschart[total//10]+1
        totalsum+=total
        #12.12 reset total to 0
        total=0
    #13 Show how many emails were filtered, how many were rejected and how
    #  many were accepted
    if accpcnt+rejcnt > 0:
        totalemails= accpcnt+ rejcnt
        totalsavg=totalsum/totalemails
    else:
        totalemails= 0
        totalsavg = 0
    print("")
    print( "There were",totalemails, "emails filtered")
    print(rejcnt, "were rejected")
    print(accpcnt, "were accepted")
    print("")
    #14 Show the average score of the emails
    print("The average score of",totalemails, "emails was", totalsavg)
    #15 close all files
    InputFile.close()
    accp.close()
    rej.close()
    #16 Draw Graphics window
    win=GraphWin("Spam Filter",550,600)
    #17 reset coordinates to making bar chart easier to plot
    win.setCoords(-1,-1,12,5)
    #18 use for loop to set the vertical and horizonal txt on the Graph
    for i in range (11):
        horz=Text(Point(i+.75,0),(i*10))
        horz.draw(win)

    for i in range ((max(Graphicschart))+2):
        vert= Text(Point(0,i+.25),(i))
        vert.draw(win)

    #19 use lines to set base of bar chart
    xplane=Line(Point(0.25,0.25),Point(11,0.25))
    xplane.draw(win)

    yplane=Line(Point(0.25,0.25),Point(0.25,(max(Graphicschart)+2.25)))
    yplane.draw(win)
    #20 use the total score for each file to make bar chart on the Graph
    for x in range(11):

        Bar=Rectangle(Point((x+.25),(Graphicschart[x]+.25))
                      ,Point(x+1.25,.25))
        Bar.setFill("blue")
        Bar.draw(win)
    #21 graphic window using getMouse()
    print("click to close window")
    win.getMouse()
    win.close()
main()
