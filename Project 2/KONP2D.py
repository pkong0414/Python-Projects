'''
    QuickSort.py
    
    This file will contain quicksort.
'''

import numpy as np
import random
import time
''' 
    quicksort will perform recursively
        
    Parameters:
    arr = array itself
    p = starting element of the array
    r = ending element of the array
        
    idea of quicksort is to take the array
    and use the end number as the pivot
        
    The list will then sort itself until up
    to the element before the pivot, which
    the number will do an exchange with then
    current index count.
        
    This will create 2 arrays which of different
    size, depending on where the pivot ends up.
        
    code taken from:
        quicksort geek for geeks: 
        https://www.geeksforgeeks.org/python-program-for-quicksort/
    '''

def partition( arr, p, r ):
    i = (p - 1)  # index of smaller element
    pivot = arr[ r ]  # pivot

    for j in range( p, r ):

        # If current element is smaller than or
        # equal to pivot
        if arr[ j ] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[ i ], arr[ j ] = arr[ j ], arr[ i ]

    arr[i + 1], arr[ r ] = arr[ r ], arr[ i + 1 ]
    return (i + 1)

        # The main function that implements QuickSort

    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort
def quickSort(arr, p, r):
    if p < r:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, p, r)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, p, pi - 1)
        quickSort(arr, pi + 1, r)

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
    This section will contain the experiment section
    
    
'''

#random arrays
random1000       = randomList( 1000 )
random10000      = randomList( 10000 )
random100000     = randomList( 100000 ) 

#sorted arrays
sorted1000       = sortedList( 1000 )
sorted10000      = sortedList( 10000 )
sorted100000     = sortedList( 100000 )

#semi sorted arrays
semiSorted1000   = semiSorted( 1000 )
semiSorted10000  = semiSorted( 10000 )
semiSorted100000 = semiSorted( 100000 )


#random numbers are sorted
startTime = time.time()
quickSort( random1000, 0, len( random1000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( random1000 ) timing: ", endTime )

startTime = time.time()
quickSort( random10000, 0, len( random10000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( random10000 ) timing: ", endTime )

startTime = time.time()
quickSort( random100000, 0, len( random100000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( random100000 ) timing: ", endTime )


#semi sorted numbers are sorted
startTime = time.time()
quickSort( semiSorted1000, 0, len( semiSorted1000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( semiSorted1000 ) timing: ", endTime )

startTime = time.time()
quickSort( semiSorted10000, 0, len( semiSorted10000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( semiSorted10000 ) timing: ", endTime )

startTime = time.time()
quickSort( semiSorted100000, 0, len( semiSorted100000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( semiSorted100000 ) timing: ", endTime )

#sorted numbers are sorted
startTime = time.time()
quickSort( sorted1000, 0, len( sorted1000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( sorted1000 ) timing: ", endTime )

startTime = time.time()
quickSort( sorted10000, 0, len( sorted10000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( sorted10000 ) timing: ", endTime )

startTime = time.time()
quickSort( sorted100000, 0, len( sorted100000 ) - 1 )
endTime = time.time() - startTime
print( "quickSort( sorted100000 ) timing: ", endTime )
