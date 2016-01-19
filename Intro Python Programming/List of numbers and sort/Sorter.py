#Name: Eric Dockery, Brent Dawson, David Tooley, George Grote
#Section: 01
#Team: 2
#Date 2/29/2012
#Email: eric.dockery283@hotmail.com
#Purpose:
    #Take user inputed list of numbers and list the largest, smallest, average
    # and sort the list from least to greatest.
#Preconditions:
    #User will input 6 numbers to form a list
#Postconditons:
    #Prompt user for 6 numbers
    #Show the numbers in a list
    #Display the largest, smallest,and average
    #Display the new list sorted
#Design:
    
def main():

    #1 Starting list with all zero's 
    list1=[0]*6
    #3 Use a for loop to run a new list
    for i in range (6):
        list1[i]=eval( input("Enter a number "))
    print()

    #4 Print list
    print(list1)

    #5 Find max
    large=max(list1)
    print("The largest number in the list is ",large)

    #6 Find min
    small= min(list1)
    print("The smallest number in the list is ", small)

    #7 Find average using sum and len
    average= sum(list1) / len(list1)
    print("The average of the list is ", average)

    #8 Print sorted list
    print("Sorted: ", sorted(list1))
    print()
    mylist2=[]
    for i in range (6):
        n=eval( input("Enter a number "))
        mylist2=mylist2+[n]
    print()
    print(mylist2)

    #9 Find max
    large=max(mylist2)
    print("The largest number in the list is ",large)
    
    #10 Find min
    small= min(mylist2)
    print("The smallest number in the list is ", small)

    #11 Find average using sum and len
    average= sum(mylist2) / len(mylist2)
    print("The average of the list is ", average)

    #12 Print sorted list
    print("Sorted: ", sorted(mylist2))
    print()    
        
main()
