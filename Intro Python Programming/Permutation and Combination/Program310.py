#Name: Eric Dockery and Joe Schmoetzer
#Assignment: Program a file read for Permutations and Combinations.
#           Get information from infile.dat file
#           Display results in output.dat file
#Language Python 3.0
import math

def Permutations(Array, r):
    temp = []
    output = open("output.dat", "a") 
    y = len(Array)
    print (y)
    print (r)
    output.write(str(Array))
    output.write(str("\n"))
    for i in range(int(math.floor(math.factorial(y)/(math.factorial(y-r)))/(y-1))):
        for j in range(y-1):
            temp = Array[y-1-j]
            Array[y-1-j] = Array[y-2-j]
            Array[y-2-j] = temp
            output.write(str(Array))
            output.write(str("\n"))
    output.write(str("\n"))


    return Array
def Combinations(combo, r):
    
    #number of combinations
    if r:
        for x in range(r - 1, len(combo)):
            for y in Combinations(combo[:x], r - 1):
                yield y + (combo[x],)
    else:
        yield tuple()   

 

def main():
    #open infile.dat
    data = open("infile.dat","r")
    output = open("output.dat", "a") 
    Array_data = []
    for line in data:
        line = line.strip('\r\n')
        Array_data.append(line)
    data.close()
    #first integer to see how many programs
    How_Many_Programs =Array_data[0]
    #move array to new array for easier loop variables
    New_Array_data = []
    for i in range (len(Array_data)-1):
        New_Array_data.append([])
        New_Array_data[i] = Array_data[i+1]
    #set up while loop for the number of programs
    x = 0
    a = 0
    Programs_Ran = 1
    How_Many_Programs = Array_data[0]    
    while (Programs_Ran <= int(How_Many_Programs)):
        Program_Line = []
        Program_Line = str(New_Array_data[x]).split(' ')
        
        n = int(Program_Line[1])
        r = int (Program_Line[2])
        thisSet = []
        #get each set of values separated from the main file
        for i in range (n):
            thisSet.append([])
            thisSet[i] = New_Array_data[a+1]
            a+=1
        x = x+n+1
        a+=1
        if (Program_Line[0] == 'P'):
            permArray = []
            arrayPerm = sorted(thisSet)
	    #getting array into lexigraphic order
            permArray = Permutations(arrayPerm, r)
            #feeding that into the permutation function
            #outputting to a file in a nice happy format
            comboPerm = list(Combinations(arrayPerm,r))
            for combo in comboPerm:
                permArray= Permutations(list(combo),r)
            output.write("\n")

        elif (Program_Line[0] =="C"):
            comboArray = []
            arrayCombo = sorted(thisSet)
            #getting array into lexigraphic order
            comboArray = list(Combinations(arrayCombo,r))
            #feeding that into the combination function
            #outputting to a file in a nice happy format
            for combos in comboArray:
                output.write(str(combos))
                output.write("\n")
            output.write("\n")

        else:
            print("File read Error")
            break
        #increment number of runs
        Programs_Ran+= 1
    output.close()
main()
