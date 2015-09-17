'''
File can be found here:  https://codility.com/demo/results/demo8AJJ26-ZHP/


A board consisting of ball switches arranged into N rows and M columns is given. A ball switch is a
device that can change the direction of a rolling ball. It has the following properties:

-  it is square-shaped;
-  it can be in one of three modes: −1, 0 or +1;
-  a ball can enter it through the top or the left edge;
-  a ball can leave it through the bottom or the right edge;
-  if the mode is −1, a ball entering the device will leave it through the bottom edge;
-  if the mode is +1, a ball entering the device will leave it through the right edge;
-  if the mode is 0, a ball entering the device will not change direction;
-  after a ball leaves the device, its mode is immediately negated.


K balls are rolled through the board one by one. Each ball enters the board through the top edge of
the top-left ball switch. Then it rolls through the board and possibly changes its direction
depending on the modes of the switches through which it passes. Eventually it leaves the
board either:

-  through the bottom edge of one of the switches in the bottom row; or
-  through the right edge of one of the switches in the rightmost column.



Write a function:

def solution(A, K)

that,given a matrix A consisting of N rows and M columns describing a board of
ball switches and a non-negative number K of balls inserted into this board,
returns the number of balls that will leave the board through the bottom edge
of the bottom-right switch.

'''

def solution(A, K):
    
    N = len(A[0])      
    M = len(A)   
    count = 0
    for i in range(K):
        rowPtr = 0
        colPtr = 0
        dir = 'd'       #initial direction is down
        while(True):
            if (A[rowPtr][colPtr] == -1):
                A[rowPtr][colPtr] = 1
                rowPtr += 1
                dir = 'd'
            elif(A[rowPtr][colPtr] == 1):
                A[rowPtr][colPtr] = -1
                colPtr += 1
                dir = 'r'
            else:
                if(dir == 'r'):
                    colPtr +=1
                elif(dir == 'd'):
                    rowPtr +=1
            if (rowPtr == M or colPtr == N):
                if(rowPtr == M and colPtr == N-1):
                    count +=1
                break
    return count
