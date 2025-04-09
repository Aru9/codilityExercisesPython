def solution(K, M, A):
    # Implement your solution here

    def check(max_sum):
        """
        Checks if it's possible to divide array A into at most K blocks
        such that the sum of each block is no greater than max_sum.
        """
        blocks = 1
        current_sum = 0
        for a in A:
            if (a > max_sum):
                return False
            if (current_sum + a ) > max_sum:
                blocks+=1
                current_sum=a
            else:
                current_sum+=a
        return blocks<=K

    

    n=len(A)
    low = M
    high = sum(A)
    result = high
    
    while(low <= high):
        mid = (low+high)//2
        if (check(mid)):
            result = mid
            high = mid -1
        else:
            low = mid +1
    return result


    

print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))