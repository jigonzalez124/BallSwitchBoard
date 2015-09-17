# you can use print for debugging purposes, e.g.
# print "this is a debug message"

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
