def solution(A):
    seen = set()

    seen = { num for num in A if num > 0}

    smallestInteger = 1
    while smallestInteger in seen:
        smallestInteger += 1

    return smallestInteger

if __name__ == '__main__':
    print("Array Counter")
    #A = 

    print(str(solution([-3,-1,-2, 1,2,3,3,2,1])))