# Names: Eric Dockery, Brent Dawson, George Grote
# Lab 5
# Team:2
# Section:1
# Date 2/6/2012
#Preconditions: (input)
    #User will input three variables.
#Postcondtions
    #Code will print the product of the numbers
    #Code will output the product in its individual digits
    #Code will output the products individual digits in reverse.
#Design:
def main():
    
    x = eval(input("Enter a number "))
    y = eval(input("Enter a number "))
    z = eval(input("Enter a number "))
    num =  (x * y * z) # code to calculate the product of x,y and z

    print("The product of your numbers is ", num)

#  Add code that will
#  calculate, using mathematical operators, the three
#  digits of the number.
#  Assume that it only has three digits.
#  You must deal with num as a number, not a string.
    dig1= num//100%100
    dig2= num//10%10
    dig3= num%10

    print("Your number is", dig1, dig2, dig3)
    print("Your number reversed is ", dig3, dig2, dig1, sep="")

main ()

# Normal Test Cases:
# Test case one:
##Enter a number 9
##Enter a number 9
##Enter a number 9
##The product of your numbers is  729
##Your number is 7 2 9
##Your number reversed is 927
#
# Test Case two:
##Enter a number 8
##Enter a number 8
##Enter a number 8
##The product of your numbers is  512
##Your number is 5 1 2
##Your number reversed is 215
#
# Abnormal Test Case:
##Enter a number 99
##Enter a number 99
##Enter a number 99
##The product of your numbers is  970299
##Your number is 2 9 9
##Your number reversed is 992
# The abnormal test case only gave the first
#three ouput numbers of the
#product due to dig1, dig2, and dig3 only covering the
#output of the first three digits.

