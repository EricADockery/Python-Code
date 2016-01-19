# Name: Eric Dockery
# Section: 01
# Email : eric.dockery283@hotmail.com
# Date: 2/3/2012
#Preconditions:( input)
    # Given each statement input the last two values along with the Operator and
    # Constant.
        #A.   3, 5, 7, 9,              11, 13    Operator + Constant 2
        #B.   2, 4, 8, 16,              32, 64   Operator * Constant 2
        #C. 12500, 2500,500, 100,        20, 4   Operator / Constant 5
        #D.   25, 23, 21, 19,           17, 15   Operator - Constant 2
        #E.   7222, 1444, 288, 57,      11, 2   Operator // Constant 5
#Postconditons
    # For each statement write a for loop that will output just those numbers
#Design
from math import *
def main():
        
    print ("A series")
    for a in  range (3,15,2):
        print (a, end=" ")
    print()
    print ("B series")
    bs=2
    for b in  range (6):
        print(bs, end= " ")
        bs=bs*2
    print()
    print ("C series")
    cs= 12500
    for c in  range (6):
        print(int(cs), end= " ")
        cs=cs/5
    print()
    print ("D series")
    for d in  range (25,13, -2):
        print(d, end= " ")   
    print()
    print ("E series")
    es= 7222
    for e in  range (6):
        print (es, end= " " )
        es= es//5
    print()
main()

#A.   3, 5, 7, 9,              11, 13    Operator + Constant 2
#B.   2, 4, 8, 16,              32, 64   Operator * Constant 2
#C. 12500, 2500,500, 100,        20, 4   Operator / Constant 5
#D.   25, 23, 21, 19,           17, 15   Operator - Constant 2
#E.   7222, 1444, 288, 57,      11, 2   Operator // Constant 5
