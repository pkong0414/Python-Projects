'''
    BubbleSort(With Swap Count).py
    
    This file will contain BubbleSort with swap count

'''

import numpy as np
import random
import time

def bubbleSortv2( arr ):
    i = 1
    swaps = 0
    for i in range( len( arr ) ):
        for j in range( 0, len( arr ) - i - 1  ):
            if arr[ j ] < arr[ j-1 ]:
                #we do the exchange
                
                #storing in a temp var
                temp = arr[ j ]
                
                #the actual exchange
                arr[ j ] = arr[ j-1 ]
                arr[ j-1 ] = temp
                
                #incrementing swaps
                swaps = swaps + 1
                
        if swaps is 0:
            #creating the terminal condition
            swaps = -1
        else:
            #resetting the counter
            swaps = 0
            i = i + 1
        if swaps is -1:
            return 0
           
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
    We are creating the experimental conditions here in this section

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
bubbleSortv2( random1000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( random1000 ) timing: ", endTime )

startTime = time.time()
bubbleSortv2( random10000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( random10000 ) timing: ", endTime )

startTime = time.time()
bubbleSortv2( random100000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( random100000 ) timing: ", endTime )

#sorted numbers are sorted
startTime = time.time()
bubbleSortv2( sorted1000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( sorted1000 ) timing: ", endTime )

startTime = time.time()
bubbleSortv2( sorted10000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( sorted10000 ) timing: ", endTime )

startTime = time.time()
bubbleSortv2( sorted100000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( sorted100000 ) timing: ", endTime )

#semi sorted numbers are sorted
startTime = time.time()
bubbleSortv2( semiSorted1000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( semiSorted1000 ) timing: ", endTime )

startTime = time.time()
bubbleSortv2( semiSorted10000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( semiSorted10000 ) timing: ", endTime )

startTime = time.time()
bubbleSortv2( semiSorted100000 )
endTime = time.time() - startTime
print( "bubblesort_with_swapCount( semiSorted100000 ) timing: ", endTime )
