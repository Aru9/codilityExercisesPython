def solution(A):
    distinctA =  set(A)
    return len(distinctA)
    



if __name__ == '__main__':
    print("Array Counter")
    print(solution([2,1,1,2,3,1]))