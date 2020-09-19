'''
    MergeSort.py
    
    This file will contain the function for mergesort.
'''

import numpy as np
import math
import random
import time


'''
    mergesort will perform recursively
        
    Parameters:
    arr: array itself
    p: the starting element of the array
    q: the middle element of the array
    r: the end element of the array
      
    idea is to create two arrays of separate bounds:
    L ( lower bound ) and R ( upper bound ).
       
    This allows us to sort through each of the array
    in a divide and conquer manner.
    
    code taken from geek for geeks:
        mergesort geek for geeks:
        https://www.geeksforgeeks.org/python-program-for-merge-sort/
'''


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

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

#semisorted arrays
semiSorted1000   = semiSorted( 1000 )
semiSorted10000  = semiSorted( 10000 )
semiSorted100000 = semiSorted( 100000 )

random10 = randomList( 10 )
print( "before: ", random10 )
mergeSort( random10, 0, len( random10 ) - 1 )
print( "after: ", random10 )

#random numbers are sorted
startTime = time.time()
mergeSort( random1000, 0, len( random1000 ) - 1 )
endTime = time.time() - startTime
print( "mergeSort( random1000 ) timing: ", endTime )

startTime = time.time()
mergeSort( random10000, 0, len( random10000 ) - 1 )
endTime = time.time() - startTime
print( "mergeSort( random10000 ) timing: ", endTime )

startTime = time.time()
mergeSort( random100000, 0, len( random100000 ) - 1 )
endTime = time.time() - startTime
print( "mergeSort( random100000 ) timing: ", endTime )

#sorted numbers are sorted
startTime = time.time()
mergeSort( sorted1000, 0, len( sorted1000 ) - 1 )
endTime = time.time() - startTime
print( "mergeSort( sorted1000 ) timing: ", endTime )

startTime = time.time()
mergeSort( sorted10000, 0, len( sorted10000 ) - 1  )
endTime = time.time() - startTime
print( "mergeSort( sorted10000 ) timing: ", endTime )

startTime = time.time()
mergeSort( sorted100000, 0, len( sorted100000 ) - 1  )
endTime = time.time() - startTime
print( "mergeSort( sorted100000 ) timing: ", endTime )

#semi sorted numbers are sorted
startTime = time.time()
mergeSort( semiSorted1000, 0, len( semiSorted1000 ) - 1  )
endTime = time.time() - startTime
print( "mergeSort( semiSorted1000 ) timing: ", endTime )

startTime = time.time()
mergeSort( semiSorted10000, 0, len( semiSorted10000 ) - 1  )
endTime = time.time() - startTime
print( "mergeSort( semiSorted10000 ) timing: ", endTime )

startTime = time.time()
mergeSort( semiSorted100000, 0, len( semiSorted100000 ) - 1  )
endTime = time.time() - startTime
print( "mergeSort( semiSorted100000 ) timing: ", endTime )
