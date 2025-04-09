def prefix_sums(A):
    n = len(A)
    print("Len = " + str(n) )
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
        print("k = " + str(k) + " current Sum = " + str(P[k]) )
    return P



if __name__ == '__main__':
    print("Array Counter")
    #A = 

    print(prefix_sums([3,4,4,6,1,4,4]))