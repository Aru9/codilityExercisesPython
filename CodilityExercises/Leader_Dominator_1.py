def solution(A):
    n =len(A)
    candidate = None
    count = 0

    # Step 1: Find the candidate using the Boyer-Moore Voting Algorithm
    for i in A:
        if count == 0:
            candidate = i
            count = 1
        elif i == candidate:
            count+=1
        else:
            count-=1

    # Step 2: Validate the candidate
    count = 0
    for num in A:
        if num == candidate:
            count+=1
    
    if count > (n//2):
        return A.index(candidate)
    else:
        return -1



if __name__ == '__main__':
    print("Hello, Leader!")
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(solution(arr))  # Output: 2