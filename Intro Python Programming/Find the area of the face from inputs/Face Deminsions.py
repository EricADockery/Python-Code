
# Name: Eric A Dockery
# Section: 01
# Date: 1/27/2012
# Email: eric.dockery283@hotmail.com
# Purpose:
#   Program to find the area of the face in the given picture.
# Preconditions:
#   Given area is calculated.

## Design
from math import *

def main():
    
#   1. Measure the length of the given face.
        Length = eval( input( "Enter the length of the face in inches " ))
#   2. Measure the width of the given face.
        Width = eval( input( "Enter the width of the face in inches "))
#   3. Calculate the area of the face as a whole using formula Area= Length* Width
        Area_whole_face = Length * Width
#   4. Measure the diameter of the right eye( circle)
        diameter_right= eval(input( "Enter the diameter of the right eye in inches "))
#   5. Calculate the Area of the right eye using formula Area= pi*((diameter/2)**2)
        Area_right_eye = pi*(diameter_right/2)**2
#   6. Measure the diameter of the left eye( circle)
        diameter_left = eval(input( "Enter the diameter of the left eye in inches "))
#   7. Calculate the Area of the left eye using formula Area= pi*((diameter/2)**2)
        Area_left_eye = pi*(diameter_left/2)**2
#   8. Measure the lenght of one side of the square nose 
        Nose = eval(input( "Enter the measurement of one side of the nose in inches "))
#   9. Calculate the area of the nose using the formula Area= side**2
        Area_Nose = Nose ** 2
#   10. Measure the base of the Mouth (isosceles triangle)
        Base_Mouth = eval(input( "Enter the measurement of the base of the mouth in inches "))
#   11. Measure the height of the Mouth (isosceles triangle)
        Height_Mouth = eval(input ( "Enter the measurement of the hight of the mouth in inches "))
#   12. Calculate the area of the Mouth using formula Area = (1/2)* Base * Height
        Area_Mouth = (1/2)*Base_Mouth*Height_Mouth
#   13. Total the Area of the Mouth, Nose, Right eye, Left eye then subtract it from the Area of the face
        Face_real = (Area_whole_face-(Area_right_eye + Area_left_eye + Area_Nose + Area_Mouth))//1
        print ( "The Total area of the face is" , Face_real, " square inches")
main()
# Total area of the face is 97013.0 square inches.
