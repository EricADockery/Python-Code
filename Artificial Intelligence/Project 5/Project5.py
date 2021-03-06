#Project: Project 1 AI
#Creator: Eric Dockery
#Assignment Details: Genetic Algorithm 
#Format of data:
    #NAME: concorde100
    #TYPE: TSP
    #COMMENT: Generated by CCutil_writetsplib
    #COMMENT: Write called for by Concorde GUI
    #DIMENSION: 100
    #EDGE_WEIGHT_TYPE: EUC_2D
    #NODE_COORD_SECTION
    #1 87.951292 2.658162
    #2 33.466597 66.682943
    #3 91.778314 53.807184
    #4 20.526749 47.633290
    #ect...


#import math - sqrt and operator - location of min path

import math
import operator
import random
#imageing imports
from tkinter import *
#from PIL import Image, ImageTk
from datetime import datetime
start_time = datetime.now()

#graphics
def plotPoints(Array, distance, name):
    
    #Make a GUI
    Map = Tk()
    w = Canvas(Map, width=1000, height=500, bg ="white")
    text = Label( Map, text =name )
    text.pack()
    #image = Image.open("Map_Westeros_political.gif")
    #photo = ImageTk.PhotoImage(image)
    Map.title("The Travel Map")
    Map.geometry("1500x880")
    #Map.image=photo

    #for loop for oval
    for i in range(len(Array)):
        #plot points
        w.create_oval((float(Array[i][1])+45)*3, (float(Array[i][2])+45)*3,
                      ((float(Array[i][1]))+57)*3,((float(Array[i][2]))+57)*3)
        #add point numbers
        w.create_text((float(Array[i][1])+48)*3,(float(Array[i][2])+50)*3, text= Array[i][0] )

    for i in range(len(Array)-1):
        #drawLines
       w.create_line((float(Array[i][1])+50)*3, (float(Array[i][2])+50)*3,
                     (float(Array[i+1][1])+50)*3,(float(Array[i+1][2])+50)*3)

    w.create_rectangle(600,300,900,400, outline="red")
    w.create_text(700,350, anchor=W, font="Purisa", text= distance)
    #finish image
    w.pack()
     
    

#distance formula
def distanceFormula(Array):
    # d = sqrt( (x2-x1)^2 +(y2-y1)^2)
    #this will be the 2ed deminsional values that are used to calculate the distance
    #Array format [[Num, X, Y], [Num ,X,Y] ...
    #i = [Num, X, Y]
    distance = 0
    #array of distance values the same length of the values
    whoIsCloser =[0] *(len(Array)**2)
    
    #display each permutation
   # print("This Permutation Set: ")
   # print(Array)
    if (len(Array) <=1):
        distance = 0
    #for each value calculate the distance value
    j = 0
    k =0
    for i in range(0,(len(Array)**2)):
        #comparing each linear object
        if (j == len(Array)):
            j = 0
            k+=1
           # print(Array[j][1])
           # print(Array[i][1])
        whoIsCloser[i] = math.sqrt((float(Array[j][1])-float(Array[k][1]))**2 + (float(Array[j][2])-float(Array[k][2]))**2)
  #      print(whoIsCloser[i])
        j+=1
        
    #Display the distance for that permutation
  #  print(whoIsCloser)
    return whoIsCloser

#Make a Parent
def CreateParent(SentArray):
    #this will make the first gen parents
    Array = [0] *(len(SentArray)+1)
    for i in range(len(SentArray)):
        Array[i] = SentArray[i]
    traveledArray = [0]*len(Array)
    #all nodes are selected at random
    for i in range(len(Array)-1):
        #get the next city
        nextSpot = random.randrange(len(Array))
        
        #while the next city has been taken
        while (Array[nextSpot-1] == 0):
            nextSpot = random.randrange(len(Array))
        #set the random city to the traveledArrays
        traveledArray[i] = Array[nextSpot-1]
        #if at the beginning add it to the last value
        if( i == 0):
            traveledArray[len(Array)-1] = Array[nextSpot-1]
        #remove the value from the Array
        Array[nextSpot-1] = 0

    #find the distance
    distanceArray = [0]*(len(Array))
    #gives n^2 distances
    distanceArray = distanceFormula(traveledArray)
    #get total distance
    totalDistance = 0
    j=1
    for i in range(0,len(Array)):
        #if we are at the end add the first city back to the distance
        if (j == len(Array)):
            j=0
            totalDistance+= distanceArray[j]
        #else add the distance of the next node to the total
        else:
            totalDistance+= distanceArray[j]
            j+=1
    #store the travel path and the total distance
       # print(totalDistance)
    FinishedArray = [0,0]
    FinishedArray[0] = traveledArray
    FinishedArray[1] = totalDistance
  #  print(FinishedArray)
    return FinishedArray
    

#make a Child
def Child(ParentArray):
    print("child")
    j =0
    NewParents = []
    #print(ParentArray)
    #fitness function for the children randomly selected
    fitnessSpot = random.randrange(len(ParentArray))
 #   print(fitnessSpot)
    fitnessValue = ParentArray[fitnessSpot][1]
  #  print(fitnessValue)
    #get rid of those greater than the fitnessValue in distance
    for i in range(len(ParentArray)-1):
    #    print(ParentArray[i][1])
        if (int(ParentArray[i][1]) <= fitnessValue):
     #       print("first if")
            if (j == 0):
      #          print("inner if")
                NewParents.append(0)
                NewParents[0] = ParentArray[i]
                j+=1
            else:
       #         print("else")
                #append a empty spot 0
                NewParents.append(0)
                #j will be the new spot
                NewParents[j]= ParentArray[i]
                j+=1
 #   print(NewParents)
#    print(j)
    #finished selecting the parents now it is time to crossover or mutate
    crossover(NewParents)


    return(NewParents)

   
#mutation of the Parent
def mutate(Array):
    #randomly change the order of two points
    print("mutate")
    #Array is list of points [[city, x, y],[city, x, y]....[city, x, y]]
    TempArray = [0] * len(Array)
    #for all values
    for i in range( len(Array)):
        #reverse the values
        TempArray[i] = Array[len(Array)-1]
    #put back in array
    for i in range(len(Array)):
        Array[i] = TempArray[i]

    
    
#crossover of the Parents
def crossover(Array):
    print("crossover")
    #Array format the same as before.
    print(len(Array))
    FinishedGeneration = [0]*(len(Array)+1)
    FinishedChild = [0]*(2)
    #if even
    gencounter =0
    #if( (len(Array)-1)%2 == 0):
    
        #for each 2 sets of parents
    for i in range(0,len(Array)-1, 2):# dont test the backtrack point
        
            FirstParent = Array[i]
            Child = FirstParent
            SecondParent = Array[i+1]
            print(FirstParent)
            print(SecondParent)
            #switch if 1/3 citys traveled is shorter
            switchValue =1 #currently at 1/5th of the value will increase when 100
            if (switchValue <0):
                switchVaule = 0
            #for each set of switchValues
            for i in range(0, len(Child)-2, switchValue): #check every 5th guy
                for j in range(len(Child)):
                    #when  secondparent is the 5th guy
                    print(SecondParent[0][j][0])
                    if(FirstParent[0][i][0] == SecondParent[0][j][0] ):
                        TestParent1 = [0,0]
                        TestParent2 = [0,0]
                        for k in range (2):
                            TestParent1[k] = FirstParent[0][i+k]
                            TestParent2[k] = SecondParent[0][j+k]
                       # print(TestParent1)
                        TestD1 = distanceFormula(TestParent1)
                        TestD2 = distanceFormula(TestParent2)
                        if (TestD2 < TestD1):
                            #This switches if testD2 len is less that testD1 for those nodes
                            Child[i] = SecondParent[0][j]
                            TravelHolder = Child[i+1]
                            Child[i+1] = SecondParent[0][j+1]
                            
                            #This will add that next one for i to the j+1 guy
                            for l in range(len(Child)):
                                #for every value in child find the double
                                if (Child[i+1] == Child[l] and l != i+1):
                                    #replace the double with the TravelHolder
                                    Child[l] = TravelHolder

                           
                            
                            
                            
                        
                        
            #finished creating the child
              #  print(Child)
           
                FinishedChild[0] = Child[i]
                FinishedChild[1] = distanceFormula(Child[i])
           
                mutateChance = random.randrange(2)
                if (mutateChance == 1):
                    mutate(FinishedChild[0])

                FinishedGeneration[gencounter] = FinishedChild
                
                gencounter+=1
                print(gencounter)
    return FinishedGeneration
            
    
    
#program Main:
def main():
    #Array of Parents:
    AofP = [0]* 10
    
    #Read lines 0-6 with no cord data
    filename = input("What is the file name? ")
    with open(filename) as f:
        #read and strip the '\n'
        content = [line.rstrip('\n') for line in open(filename)]
        
    #line 7 starts the important information
    startCords = 0
    #seperate the values into a dictionary with the key being the first
    #value of the strings starting on line 7
    parsedContent = [0] * (len(content)-7)
 
    counter = 0
    #parsedContent [['object', 'X', 'Y']]
    for i in range(7,len(content)):
        parsedContent[counter] = content[i].split()
        counter+=1

    #distanceFormula calculates all of the distances in one array and returns it
    theDistanceArray = distanceFormula(parsedContent)
    #print(theDistanceArray) #distance Array has n^2 distances
    parentArray= [0]*(len(parsedContent)*10)
    #temp Values for graphics
    tempDistance = 0
    tempArray = [0]
    tempName = "Temp"
    #create double the len parents
    for i in range(len(parsedContent)*10):
        #parentArray format [[[city1,city2,...,cityn], totaldistance], ....]
        parentArray[i] = CreateParent(parsedContent)
        
        
        tempDistance = parentArray[i][1]
        tempArray = parentArray[i][0]
        tempName = "Parent" + str(i)
        #printCheck
    #    print(tempName)
   #     print(tempArray)
  #      print(tempDistance)
        #draw each parent
        if( i == 0):
          #  print(parentArray[i])
            plotPoints(tempArray, tempDistance, tempName)
 #   print(parentArray)   
    #After all gen 1 is created we make children
    #while we have more than 2 parents make children

    j = 1
    while (len(parentArray) > 1):
         parentArray = Child(parentArray)
         for i in range(len(parentArray)):
             tempDistance = parentArray[i][1]
             tempArray = parentArray[i][0]
             tempName = "Generaton" + str(j) +"Child" + str(i)
        #printCheck
    #    print(tempName)
   #     print(tempArray)
  #      print(tempDistance)
        #draw each parent
             
             j+=1
             
    #last value
    plotPoints(tempArray, tempDistance, tempName)
    print(parentArray)
    print(j)
main()
