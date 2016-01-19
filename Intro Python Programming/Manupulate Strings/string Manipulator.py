# Name : Eric A Dockery
# Date: 02/28/2012
# Section: 01
# Email: eric.dockery283@hotmail.com
# Purpose:
    #Manupulate strings and use if statments to get desired output.
# Preconditions:
    # String from the user
# Postconditions:
    # Prompt lines.
    # Every other letter on the same line.
    # Short if the string is 5 characters.
    # First 2 characters of the string followed by the last 2.
    # With if statement creat new string with "ing" or "ly" on the old string
# Design:
def main():
    #1.starting code asking for string:
    string= input("Enter a string: ")
    print()
    x= len(string)
    #2. for loop printing ever other letter:
    print("Every other charater")
    for i in range(0,x,2):
        print(string[i], end="")
    print()
    print ()
    #3. for loop pring string backwards:
    print("String backward")
    for i in range(x-1,-1,-1) :
        print (string[i],end="")
    print()
    #4. if statement if string is less than 5 characters
    print()
    if len(string)<= 5:
        print("short")
    print()
    #5. first and last two characters:
    z=string[0:2]+string[x-2:x]
    print("first and last 2 characters",z)
    
    print()
    #6. new string suffix using if statement:
    u=len(string)-3
    p=(string[u:len(string)])
    if p.find("ing")> -1:
        y=string+ "ly"
    else:
        y=string+"ing"
        
    print("new string with suffix",y )
main()

        
