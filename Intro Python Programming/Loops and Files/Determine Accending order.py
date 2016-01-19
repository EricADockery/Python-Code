# Names: Eric Dockery
# Section: 01
# Team: 02
# Purpose:
    #Write a loop using a file determining if the file is in accending order
    # Use the largest number and Test if it is True or False using the statement
    # If the first number is greater than the second True and if the
    # Second number is greater than the first then False
#Preconditions:
    #none
# Postconditions:
    # yes or no
#Design

def main():
    # Open file
    a=open("Teamlab9.txt","r")
    
    # Set starting number False
    Flag= True
    # Set Starting number as firstline
    num1= eval(a.readline())
    # Start loop with file
    for line in a:
        # Set second file number
        num2=eval(line)
        # Determine if the second number is less than the first
        if num2 < num1:
            # Set it to false if true
            Flag=False
            # Set the first number to the second number
        num1=num2
        # Print yes if true and no if false
        # Yes means the file is in accending order
        # No means the file is not in accending order
    if Flag:
        print("yes")
    else:
        print("no")
    a.close
main()
            
