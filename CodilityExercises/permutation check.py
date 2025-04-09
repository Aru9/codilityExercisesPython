import math
def solution(A):
    # Implement your solution here
    #alen = len(A)
    unique_elements = set(A)

    alen = len(A)
    if (alen != len(unique_elements)):
        return 0

    nSum = ( alen*(alen+1) ) // 2
    #print(" Len and Sum " + str(len(A)) + " and " + str(nSum) )
    if (nSum != sum(A)):
        return 0
    else:
        return 1
    
    def bestSolution(N,M):
        # Implement your solution here
        return N//math.gcd(N,M)

if __name__ == '__main__':
    print("Split")
    A = [3,1,2,4,3]

    for time, position in enumerate(A):
        print(" Time = " + str(time) + " position  = " + str(position))
    B = [ x for x in range (1, 15)]
    print(B)
    print(len(B))
    print(solution(A))
    