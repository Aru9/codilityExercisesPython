def solution(A):
    print(A)
    A.sort()
    if A[1] < 0:
        return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])
    else:
        return (A[-1]*A[-2]*A[-3])
    



if __name__ == '__main__':
    print("Array Counter")
    print(solution([-3,1,2,-2,5,6]))