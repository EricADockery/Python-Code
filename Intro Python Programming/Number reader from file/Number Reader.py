

#write a program that will read in 3 numbers
#from each line of a file.
#it will report the total of the first NINE numbers
#(i.e. the first three lines of data)
#you can assume the number of lines in the file
#will be a multiple of three
#and there will be 3 numbers on each line

def main():
# Ask user for filename
    fn = input("Enter a file name ")
# open file for reading
    inf = open(fn, "r")

# get all lines of data from the file and process them
#  three lines at a time
# the body processes 3 lines of data
    for line in inf:

#  first line just read in by "for" statement
#  set accumulator for total of 9 numbers
         tot = 0

#  break up the first line (remember, it's a string)
#  into individual strings  "1 2 3" becomes ["1","2","3"]
         for i in line.split():
#  add individual strings after processing with eval
             tot += eval(i)

#  to handle the following two lines of data
#  x is only used to make the loop execute twice
         for x in range(2):
#         get a line from the file
             line = inf.readline()
#         break into individual strings with split
             for i in line.split():
#         add to the same accumulator as first line was
                  tot += eval(i)

#  after those two lines have been processed, give total 
         print("Total is", tot)
#  bottom of loop processing data in file

#  after all lines have been processed, close the file
    inf.close()

main()

 
