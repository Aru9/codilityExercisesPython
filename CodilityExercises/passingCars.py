

def solution(A):
    # Implement your solution here
    east_count = 0
    passing_pair = 0
    for i in A:
        if i == 0:
            east_count+=1
        elif i == 1:
            passing_pair+=east_count
            if passing_pair > 1_000_000_000:
                return -1
    return passing_pair



if __name__ == '__main__':
    print("Array Counter")
    #A = 

    print(solution([0,1,0,1,1]))
    print(solution([1,1,0,1,1]))
    print(solution([0,1,0,1,0,1]))
    print(solution([0,1,1,0,1,0,1,0,1,1]))

