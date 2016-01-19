#CECS 310 Fall 2013 programming assignment
#Code by Eric Dockery and Joe Schmoetzer
#language is Python 2.7
#sources used: stackoverflow.com
#			   docs.python.org
import sys

def project1():   
	data = open("infile.dat","r")  #opens the infile.dat
	contents = []
	for line in data:				#reads each line of the file
		line = line.strip('\r\n')	#strips off the carriage return if there is one
				#itemizes each string on the newline
		contents.append(line)		#and stores into contents
	data.close()		
	return contents

#takes contents of file and busts the strings of data into useful parts
def buster(stuff):
	ops = map(int, stuff[0])	#getting that first integer to tell how many
	newArray = []				#P and C to look for

	for i in range(len(stuff)-1): # breaking up the array into
		newArray.append([])		  #into pieces that can be used
		newArray[i] = stuff[i+1]

	x = 0
	a = 0
	#This is the main loop that controls most of the program
	for z in range(ops[0]): #This is where the first integer is used
		#Breaking up the P/C n r lines and filling the variables
		do = str(newArray[x]).split(' ')
		n = int(do[1])
		r = int(do[2])
		thisSet = []
		#getting each set of values separated from the main file
		for i in range(n):
			thisSet.append([])
			thisSet[i] = newArray[a+1]
			a +=1		#using some fun math here
		x = x + n + 1
		a+=1

		#This is for getting a permutation
		if (do[0] == 'P'):	
			permArray = []
			arrayPerm = sorted(thisSet)	#getting array into lexigraphic order
			permArray = permutation(arrayPerm, r) #feeding that into the permutation function	
			#outputting to a file in a nice happy format
			for combo in permArray:
				output.write(str(combo))
				output.write("\n")
			output.write("\n")
		#This is for getting a combination		
		elif (do[0] == 'C'):
			comboArray = []
			arrayCombo = sorted(thisSet) #getting array into lexigraphic order
			comboArray = list(combinations(arrayCombo,r)) #feeding that into the combination function
			#outputting to a file in a nice happy format
			for combos in comboArray:
				output.write(str(combos))
				output.write("\n")
			output.write("\n")
			
		else:
			break

#This function, as per it's name, is used if asked to use permutations.
#Takes the array fed to it and returns all the permutations of that array.
#Depending on the r value set, it out the lenght of the permutations, for
#this project the r value is given from the infile.dat
def permutation(perm, r):
	setValues = tuple(perm)
	x = len(setValues)
	r = x if r is None else r
	if r > x:
		return
	indents = range(x)
	cycles = range(x, x-r, -1)
	yield tuple(setValues[i] for i in indents[:r])
	while x:
		for i in reversed(range (r)):
			cycles[i] -= 1
			if cycles[i] == 0:
				indents[i:] = indents [i+1:] + indents[i:i+1]
				cycles[i] = x - i
			else:
				k = cycles[i]
				indents[i], indents[-k] = indents[-k], indents[i]
				yield tuple(setValues[i] for i in indents[:r])
				break
		else:
			return

#This function, as per it's name, is used if asked to use combinations.
#Takes the array fed to it and returns all the combinations of that array.
#Depending on the r value set, it out the lenght of the combinations, for
#this project the r value is given from the infile.dat
def combinations(combo, r):
    setValues = tuple(combo)
    x = len(setValues)
    indents = range(r)
    yield tuple(setValues[i] for i in indents)
    while True:
        for i in reversed(range(r)):
            if indents[i] != i + x - r:
                break
        else:
            return
        indents[i] += 1
        for j in range(i+1, r):
            indents[j] = indents[j-1] + 1
        yield tuple(setValues[i] for i in indents)

if __name__ == "__main__":
	output = open("output.dat", "w") #Setting up the output.dat file
	test = project1() #opening the input file and getting the data into
					  #an array of lines
	work = buster(test) #passing that array to the buster function to work with it
	output.close()	#closing the file to conclude the program
