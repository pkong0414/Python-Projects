'''
    SelectionSort.py
    
    This file will contain selectionsort
'''

import numpy as np
import random
import time

def selectionSort( arr ):
    
    for i in range( len( arr ) - 1 ):
        min = i
        for j in range( i+1, len( arr ) ):
            if arr[ j ] < arr[ min ]:
                min = j
        
        #storing in a temp var before the exchange
        temp = arr[ i ]
        
        #the exchange happening
        arr[ i ] = arr[ min ]
        arr[ min ] = temp
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

random1000       = randomList( 1000 )
random10000      = randomList( 10000 )
random100000     = randomList( 100000 ) 

sorted1000       = sortedList( 1000 )
sorted10000      = sortedList( 10000 )
sorted100000     = sortedList( 100000 )

semiSorted1000   = semiSorted( 1000 )
semiSorted10000  = semiSorted( 10000 )
semiSorted100000 = semiSorted( 100000 )


#random numbers are sorted
startTime = time.time()
selectionSort( random1000 )
endTime = time.time() - startTime
print( "selectionSort( random1000 ) timing: ", endTime )

startTime = time.time()
selectionSort( random10000 )
endTime = time.time() - startTime
print( "selectionSort( random10000 ) timing: ", endTime )

startTime = time.time()
selectionSort( random100000 )
endTime = time.time() - startTime
print( "selectionSort( random100000 ) timing: ", endTime )

#sorted numbers are sorted
startTime = time.time()
selectionSort( sorted1000 )
endTime = time.time() - startTime
print( "selectionSort( sorted1000 ) timing: ", endTime )

startTime = time.time()
selectionSort( sorted10000 )
endTime = time.time() - startTime
print( "selectionSort( sorted10000 ) timing: ", endTime )

startTime = time.time()
selectionSort( sorted100000 )
endTime = time.time() - startTime
print( "selectionSort( sorted100000 ) timing: ", endTime )

#semi sorted numbers are sorted
startTime = time.time()
selectionSort( semiSorted1000 )
endTime = time.time() - startTime
print( "selectionSort( semiSorted1000 ) timing: ", endTime )

startTime = time.time()
selectionSort( semiSorted10000 )
endTime = time.time() - startTime
print( "selectionSort( semiSorted10000 ) timing: ", endTime )

startTime = time.time()
selectionSort( semiSorted100000 )
endTime = time.time() - startTime
print( "selectionSort( semiSorted100000 ) timing: ", endTime )
