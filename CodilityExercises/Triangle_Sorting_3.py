def solution(A):
    A.sort()
    #print(A)
    
    n = len(A)

    for i in range(n-2):
        if ( (A[i] + A[i+1]) > A[i+2] ):
            return 1
    return 0
    



if __name__ == '__main__':
    print("Array Counter")
    print(solution([10,2,5,1,8,20]))