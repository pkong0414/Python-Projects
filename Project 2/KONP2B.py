'''
    InsertionSort.py
    
    This file will contain insertionsort
'''

import numpy as np
import random
import time

def insertionSort( arr ):
    for j in range( 2, len( arr) ):
        i = j - 1
        key = arr[ j ]
        while i > 0 and arr[ i ] > key:
            #exchange condition
                
            #exchange operation
            arr[ i + 1 ] = arr[ i ]
                
            #decrementing i
            i = i - 1
        arr[ i + 1 ] = key
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
        if ( i + 1 ) % 10 is 0:
            semiArr[ i ] = random.randint( 0, arrSize )
        else:
            semiArr[ i ] = i
    return semiArr

'''
    This is the experimental section
'''

#random array
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


#random numbers are sorted
startTime = time.time()
insertionSort( random1000 )
endTime = time.time() - startTime
print( "insertionSort( random1000 ) timing: ", endTime )

startTime = time.time()
insertionSort( random10000 )
endTime = time.time() - startTime
print( "insertionSort( random10000 ) timing: ", endTime )

startTime = time.time()
insertionSort( random100000 )
endTime = time.time() - startTime
print( "insertionSort( random100000 ) timing: ", endTime )

#sorted numbers are sorted
startTime = time.time()
insertionSort( sorted1000 )
endTime = time.time() - startTime
print( "insertionSort( sorted1000 ) timing: ", endTime )

startTime = time.time()
insertionSort( sorted10000 )
endTime = time.time() - startTime
print( "insertionSort( sorted10000 ) timing: ", endTime )

startTime = time.time()
insertionSort( sorted100000 )
endTime = time.time() - startTime
print( "insertionSort( sorted100000 ) timing: ", endTime )

#semi sorted numbers are sorted
startTime = time.time()
insertionSort( semiSorted1000 )
endTime = time.time() - startTime
print( "insertionSort( semiSorted1000 ) timing: ", endTime )

startTime = time.time()
insertionSort( semiSorted10000 )
endTime = time.time() - startTime
print( "insertionSort( semiSorted10000 ) timing: ", endTime )

startTime = time.time()
insertionSort( semiSorted100000 )
endTime = time.time() - startTime
print( "insertionSort( semiSorted100000 ) timing: ", endTime )
