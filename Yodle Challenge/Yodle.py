# Author: Eric A Dockery
# Date: 04/06/2014
# Purpose: Better my resume chance
#Program Juggle Fest
#Input: File with Circuit (C) and Juggler (J) lines defining what they want to
#preform
#Output: Circut and Jugglers with the dot product of each score ordered from
#highest to lowest


def main():
    
    #Read in the file to an whole file array using a while loop
    Input_File = open('input.txt', 'r')
    Whole_Array=[]
    Array_For_Circuits=[]
    Array_For_Juggler=[]
    Temp_Array=[]
#This holds the whole file
    i=0
    for line in Input_File:
        
        Whole_Array.append(line)
        i+=1
    Input_File.close()

    #Split the array by spaces and sort into Circuits and Jugglers
    for i in range(0, len(Whole_Array)):
        Temp_Array.append(Whole_Array[i].split(" "))
        if Temp_Array[i][0] == "C":
            Array_For_Circuits.append(Temp_Array[i])
        elif Temp_Array[i][0]== "J":
            Array_For_Juggler.append(Temp_Array[i])
    #Divide the number of Jugglers by the number of Circuits to see how many
    # Jugglers are in each Circuit. (By definition a whole number without remainder)
    Number_of_Circuits= len(Array_For_Circuits)
    Number_of_Jugglers=len(Array_For_Juggler)
    Total_per_Circuit= Number_of_Jugglers/Number_of_Circuits
    #Calculate the dot product for each Juggler and Circuit combination
    #Sort those Circuits and Jugglers accordingly
    print (Number_of_Circuits)
    print (Number_of_Jugglers)
    print( Total_per_Circuit)
    #Find the prefered spot for each Juggler
    Prefrence=[]
    Ideal=[]
    string= " "
    Juggler_Value=[]
    Temp_Array=[]
    for i in range ( 0, len(Array_For_Juggler)):
        Prefrence.append(Array_For_Juggler[i][5].split(","))
        string= Array_For_Juggler[i][1]
        Juggler_Value.append(string)
        for j in range(0, 10):
            Temp_Array.append(Prefrence[i][j].strip())
            print(Temp_Array)
    Ideal.append(Temp_Array)
    
    Temp_Array=[]
    #Dot product sum of Each Jugglers list


    #Find Each Circuit Value
    Temp_Array=[]
    Temp_Array2=[]
    Each_Circuit_Value_Array= []
    Contest_Array=[]
    for i in range(0, len(Array_For_Circuits)):
        Contest_Array.append(Array_For_Circuits[i][1])
        Temp_Array.append(Array_For_Circuits[i][2].split(":"))
        Temp_Array.append(Array_For_Circuits[i][3].split(":"))
        Temp_Array.append(Array_For_Circuits[i][4].split(":"))
    for i in range(0, len(Temp_Array)):
        Temp_Array2.append(int(Temp_Array[i][1]))
        if (i+1)%3 == 0:
            Each_Circuit_Value_Array.append(Temp_Array2)
            Temp_Array2=[]
     #Find Each Juggler Value

    Temp_Array=[]
    Each_Juggler_Value_Array= []
    for i in range(0, len(Array_For_Juggler)):
        Temp_Array.append(Array_For_Juggler[i][2].split(":"))
        Temp_Array.append(Array_For_Juggler[i][3].split(":"))
        Temp_Array.append(Array_For_Juggler[i][4].split(":"))

    for i in range(0, len(Temp_Array)):
        Temp_Array2.append(int(Temp_Array[i][1]))
        if (i+1)%3 ==0:
            Each_Juggler_Value_Array.append(Temp_Array2)
            Temp_Array2=[]
#### THEN REMOVE ONE
    Temp_Array=[]
    Array_Dot_Product=[]
    for i in range (0,len(Each_Juggler_Value_Array)):
        for j in range(0,Number_of_Circuits):
            Temp_Array.append(Each_Juggler_Value_Array[i][0]*Each_Circuit_Value_Array[j][0])
            Temp_Array.append(Each_Juggler_Value_Array[i][1]*Each_Circuit_Value_Array[j][1])
            Temp_Array.append(Each_Juggler_Value_Array[i][2]*Each_Circuit_Value_Array[j][2])
            Array_Dot_Product.append(int(Temp_Array[0])+int(Temp_Array[1])+int(Temp_Array[2]))
            Temp_Array=[]


### combine each number back in a pair with its Juggler value
    Juggler_Dot_Array=[]
    temp_number=0
    for i in range (0, len(Juggler_Value)):
        for j in range (0,Number_of_Circuits):
            Temp_Array.append([Juggler_Value[i], Contest_Array[j], Array_Dot_Product[temp_number]])
            temp_number+=1
        Juggler_Dot_Array.append(Temp_Array)
        Temp_Array=[]
## Sort the Juggler_Dot_Array into its Ideal preformance
    Finished_Sort_Array=[]
    for i in range(0, Number_of_Jugglers):
        for l in range (0,3):
            for j in range(0, Number_of_Circuits):
                if(Ideal[i][l] == Juggler_Dot_Array[i][j][1]):
            
                  Finished_Sort_Array.append(Juggler_Dot_Array[i][j])
    print(Finished_Sort_Array)
    
##Find the best matches of jugglers per circuit:



    print ()
 
        
        
                                    
main()
