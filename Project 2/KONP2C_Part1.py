'''
    BubbleSort.py
    
    This will perform bubble sort.
    
    <draft this documentation later.>
'''

import numpy as np
import random
import time

def bubbleSort( arr ):
    for i in range( len( arr ) ):
        for j in range( 0, len( arr ) - i - 1 ):
            if arr[ j ] < arr[ j - 1 ]:
                #we swap arr[ j ] with arr[ j-1 ]
                
                #temp value is stored
                temp = arr[ j ]
                
                #the actual exchange
                arr[ j ] = arr[ j-1 ]
                arr[ j-1 ] = temp
    return arr
                
def randomList( arrSize ):
    #This function will create an array of random numbers
    randomArr = np.zeros( arrSize )
    for i in range( arrSize ):
        randomArr[ i ] = random.randint( 0, arrSize )
    return randomArr

def sortedList( arrSize ):
    #This function will create an array of sorted numbers
    sortedArr = np.zeros( arrSize )
    for i in range( arrSize ):
        sortedArr[ i ] = i
    return sortedArr
        
def semiSorted( arrSize ):
    #This function will create an array where every 10th number
    #will contain a randomized number.
    semiArr = np.zeros( arrSize )
    for i in range( arrSize ):
        if ( i + 1 ) % 10 == 0:
            semiArr[ i ] = random.randint( 0, arrSize )
        else:
            semiArr[ i ] = i
    return semiArr            

'''
    We'll have this section used to do the actual experimentation.
    
    we'll have an array of 3 sizes for each of the function types:
       1000, 10000, and 100000
    
    Three things will be implemented:
    
    1: Random Function: This function will fully randomize a list
    from 0 to n-1
    
    2: sorted list: This won't be a function but will just create
    a list from 0 to n-1
    
    3: Semi Sorted: This function will create a list with a random
    number for every 10 numbers
    
'''

#randomly array
random1000       = randomList( 1000 )
random10000      = randomList( 10000 )
random100000     = randomList( 100000 ) 

#sorted array
sorted1000       = sortedList( 1000 )
sorted10000      = sortedList( 10000 )
sorted100000     = sortedList( 100000 )

#semi sorted array
semiSorted1000   = semiSorted( 1000 )
semiSorted10000  = semiSorted( 10000 )
semiSorted100000 = semiSorted( 100000 )


#we'll need to make an testing output for all this experiments

#random numbers are sorted
startTime = time.time()
bubbleSort( random1000 )
endTime = time.time() - startTime
print( "bubblesort( random1000 ) timing: ", endTime )

startTime = time.time()
bubbleSort( random10000 )
endTime = time.time() - startTime
print( "bubblesort( random10000 ) timing: ", endTime )

startTime = time.time()
bubbleSort( random100000 )
endTime = time.time() - startTime
print( "bubblesort( random100000 ) timing: ", endTime )

#sorted numbers are sorted
startTime = time.time()
bubbleSort( sorted1000 )
endTime = time.time() - startTime
print( "bubblesort( sorted1000 ) timing: ", endTime )

startTime = time.time()
bubbleSort( sorted10000 )
endTime = time.time() - startTime
print( "bubblesort( sorted10000 ) timing: ", endTime )

startTime = time.time()
bubbleSort( sorted100000 )
endTime = time.time() - startTime
print( "bubblesort( sorted100000 ) timing: ", endTime )

#semi sorted numbers are sorted
startTime = time.time()
bubbleSort( semiSorted1000 )
endTime = time.time() - startTime
print( "bubblesort( semiSorted1000 ) timing: ", endTime )

startTime = time.time()
bubbleSort( semiSorted10000 )
endTime = time.time() - startTime
print( "bubblesort( semiSorted10000 ) timing: ", endTime )

startTime = time.time()
bubbleSort( semiSorted100000 )
endTime = time.time() - startTime
print( "bubblesort( semiSorted100000 ) timing: ", endTime )
