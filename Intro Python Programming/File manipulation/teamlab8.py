#Names: Eric Dockery, 
#Section:01
#Team:02
#Date: 3/5/2012
#Preconditions:
    #Input name of file
#Postcondtions:
    #Total the numbers in the file lines 3 at a time until file is finished.
#Design:

from graphics import *
def main():
    #1. Input file name:
    t=input("Enter a file name: ")
    #2. Open file
    s=open(t,"r")
    #3. Create list of the lines.
    a=s.readlines()
    #4. calcualte the range of the string using division of 3 to get desired
        # range for the three sets of lists.
    c=0
    for i in range (len(a)//3):
    #5. use accumulator to get each string varaiable as a interger and sum.
        y=0
        for i in range (3):
            x=a[c].split()
            for z in range (3):
                y=eval(x[z])+y
            c=c+1
    #6. Print total for each set of 3
        print("Total is ",y)
    s.close()
    
main()
