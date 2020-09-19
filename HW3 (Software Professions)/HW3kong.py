import math
import random
import turtle
import numpy as np

"""
CS 4500, HW3, Fall 2019

Paint Blob Paintings

This is an INDIVIDUAL assignment. Do NOT work on this with anyone else.

Consider the following (wildly improbable) situation:

You have an N X N grid lying on the floor, where N is an integer between 2 and 15 inclusive.
You are capable of dropping blobs of paint on to the grid in such a way that
The blob lands randomly on the grid on to only one cell (each time)
The blob does not splatter into any of the other cells
The blob always falls somewhere on the grid
If subsequent blobs of paint fall on that same cell, that’s OK, and again there is no splatter

In order to “complete” your painting (and our apologies to Jackson Pollock), you continue dropping paint blobs, one at
a time, until each cell has at least one paint blob dropped on to it.
When the painting is complete, every cell contains paint, and some cells may have LOTS of paint.

For homework 3, you are to write a Python program that does the following:

On the screen, ask the interactive user to enter an integer between 2 and 15 inclusive. This will determine the size of
your square grid. I will call this number N. If the user enters something illegal, give an error message and keep asking
until you get something appropriate.

Next, ask the interactive user to enter an integer between 1 and 10 inclusive. This will tell your program how many
“paintings” it will make. I will call this number K. If the user enters something illegal, give an error message and
keep asking until you get something appropriate.
Make an N X N random paint blob painting K times. As each of the K paintings is being made, display graphics on the
screen to show the interactive user how the painting is proceeding. You have great latitude as to how you will display
the painting as it fills up with paint. At the very least, the interactive user should be able to tell which cells have
 NO paint so far, which cells have SOME paint so far, and which cell is being painted right at the moment.

 This minimum would require three distinct colors. However, you might be able to think of a clever way to visually
 communicate more information about the painting than no paint, some paint, and currently being painted. Be thoughtful
 and creative about this, please. Give some thought as to how quickly you want to paint drops to appear in your simulation.
After a painting “finishes,” alert the interactive user, and inform them that they must push ENTER (or RETURN) to continue.
After all K paintings have been finished (including the final ENTER push by the user), display the following statistics
 from all the paintings: The minimum, maximum, and average number of paint blobs it took to paint a picture; and the
 minimum, maximum, and average number that describes the most paint blobs that fell into any one cell in a painting.

After you have this program working, I challenge you to use your program to explore how the statistics change when you
use larger and smaller grids (N).  This challenge does NOT change the specification of the program you will submit for
this assignment.

"""

turt = turtle.Turtle()

# N will dictate the NxN grid
N = 0
K = 0
while( N < 2 or N > 15 ):
   N = int( input( "Please enter the number for N [2- 15]: " ) )
# K will dictate the number of paint circle this program will draw
while( K < 1 or K > 10 ):
    K = int( input( "Please enter the number of canvas to paint: " ) )

"""
we have a list for both X and Y. When both X and Y lists are filled, the loop will end.
"""
# seeding RNG
random.seed( )

# drawing the grid
# grid will be of dimension 600 / N.
# This I believe is an appropriate size which will divide a portion up to N times.

for i in range( K ):
    turt.clear()
    # initializing the visit list
    # this visit list will give us the means to finish a canvas
    Finished = False

    # start of the perimeter drawing
    gridLength = 40
    # turt.pu()
    # turt.setx( LENGTH / 2 )
    # turt.sety ( LENGTH / 2 )
    # turt.pd()
    # turt.left( 180 )
    # turt.forward( LENGTH )
    # turt.left( 90 )
    # turt.forward( LENGTH )
    # turt.left( 90 )
    # turt.forward( LENGTH )
    # turt.left( 90 )
    # turt.forward( LENGTH )
    length = 700
    boxLen = 700 / N
    center = boxLen / 2

    # initializing visit list for x and y
    VisitList = np.zeros( N * N )

    # hiding turtle before drawing
    turt.hideturtle()

    # start of the grid drawing
    for i in range( N + 1 ):
        # this will give us the vertical lines for our grids
        turt.pu()
        x = -350 + ( boxLen * i )
        turt.setposition( x, 350 )
        turt.pd()
        turt.setheading( 270 )
        turt.forward( 700 )

    for j in range( N + 1 ):
        # this will give us the horizontal lines for our grids
        turt.pu()
        y = 350 - ( j * boxLen )
        turt.setposition( -350, y )
        turt.pd()
        turt.setheading( 0 )
        turt.forward( 700 )
    # end of the grid drawing

    while( Finished == False ):
        # randomly deciding x and y coordinates
        x = random.randint( 0, N - 1 )
        y = random.randint( 0, N - 1 )

        # randomly deciding the colors
        color1 = float( random.random() )
        color2 = float( random.random() )
        color3 = float( random.random() )

        # debugging output
        print( "color 1: ", color1 )
        print( "color 2: ", color2 )
        print( "color 3: ", color3 )

        turt.color( ( color1, color2, color3 ) )
        # incrementing the visit list of coordinates visited
        VisitList[ (y * N) + x ] = VisitList[ (y * N ) + x ] + 1

        # debugging output
        print( "Visit: ", VisitList )

        # the circle or dot function from turtle will draw the paint drops we need.
        # we use ( -350, -350 ) as a origin point to operate this canvas
        turt.pu()
        turt.setx( (-350 + center) + ( x * boxLen ) )
        turt.sety( -350 + ( y * boxLen ) )

        turt.pd()
        #we use center because the center length is the actual radius as well!
        turt.begin_fill()
        turt.circle( center, 360 )
        turt.end_fill()

        # this will consider for every coordinates X and Y that have been visited
        if all( v > 0 for v in VisitList ):
            Finished = True
            print("This canvas is finished!")
