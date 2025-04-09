# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    N = len(A)
    if N == 0:
        return 0
    
    count = 0
    end = -1

    for i in range(N):
        if A[i] > end:
            count += 1
            end = B[i]
    
    return count