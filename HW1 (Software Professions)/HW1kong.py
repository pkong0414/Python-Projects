import numpy as np

'''
	homework1 (intro software profession).py

    This game will create a number of non-intersecting circles on the board ( 1 - 10 ).

    An input file will be used.

    input = HW1infile.txt

    This file will contain two things: N and K.

    N will be 2 - 10 inclusive. K will be positive integers.

    N = arr[ 0 ]
    K = arr[ 1 ]

    we will use a dictionary to assign a numbered circle to a numbered circle it points to.

    { n start circle: n other circle }

    example of an input file:
    This would be from the example of diagram 3

    4
    5
    1 4
    1 2
    1 3
    2 1
    3 1
    
    
    note: the number of visits should not exceed the number of arrows involved. 
    There is an initial count tally for 1 since this is where the game should start at, so please account for that.
    
    When checking between visit and arrows use: ( visit - 1 ) to discount the initial tally for 1.

    output file will be: HW1kongOutfile.txt
    output file will contain the following:
    
    Number of circles
    Number of arrows used
    Total number of checks for all circles combined
    Average number of visits for each circle
    Max number of visit for any one circle
'''

input = "HW1infile.txt"

file = open(input, 'r')

## This is the input validation! ##

# This will give me the N number of circles and K number of arrows
# as well as give me the rest of the numbers that the game intends on traveling to and fro.

lineCount = 0
arr = []
arr2 = []

count = 0
# This will just get N and K to get the array started
for i, line in enumerate(file):
    arr = [x.strip("\n") for x in line.split(" ")]
    for i, k in enumerate(arr):
        print( arr[i] )
        arr2.append( arr[i] )

file.close()
print( "\ndone\n" )

#N will hold the number of circles used
N = int( arr2[ 0 ] )

#K will hold the number arrows used
K = int( arr2[ 1 ] )

# testing output
# print("printing array 2 \n")
# print( arr2 )

circleList = np.zeros( N )

# #testing output
# print( "printing circleList" )
# print( circleList )

#taking out the beginning 2 numbers which is unneeded right now
arr2.pop( 0 )
arr2.pop( 0 )

if int(arr2[0]) == 1:
    circleList[ 0 ] = circleList[ 0 ] + 1
for i in range( len( arr2 ) ):
    print( arr2[i] )
    if int(arr2[ 0 ]) != 1:
        print( "Error: improper format. Initial position must start at 1!")
        exit()
    if (i + 1) % 2 == 0:
        #creating tally for each circles visited
        circleList[ int(arr2[i]) - 1 ] = circleList[ int(arr2[i]) - 1] + 1

#printing circleList after the game is over
print( "printing new circleList" )
print( circleList )

#initializing visit counts
visitCount = 0
for j in range( len(circleList)):
    visitCount = int( visitCount + circleList[ j ] )

#testing output
print( "visit counts: ", visitCount )

if( visitCount - 1 ) > K:
    print( "number of visit must be equal to arrows used!" )
    exit()
else:
    #making average number of checks for each circle
    avgCirVisit = float( (visitCount - 1) / int(N) )
    #max number of visits for any circle
    maxVisit = max( circleList )

# TODO create test cases
# To check we will take the circle number arr[ i ] and traverse through the arrow number arr[ i + 1 ]

# we will need to develop a method to handle same values to prevent repeat travels!

# then use the arrow number to search for the next number.

# TODO create the write output file section

output = "HW1kongOutfile.txt"

outFile = open(output, "w+")

outFile.write( "Number of circles: %s\n" % N )
outFile.write( "Number of arrows used: %s\n" % K )
outFile.write( "Total number of checks for all circles combined: %d\n" % visitCount )
outFile.write( "Average number of visits for each circle: %.2f\n" % avgCirVisit )
outFile.write( "Max number of visit for any one circle: %d\n" % maxVisit )


outFile.close()