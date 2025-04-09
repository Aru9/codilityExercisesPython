# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    
    # Step 1: Find the candidate for the leader using Boyer-Moore Voting Algorithm
    candidate = None
    count = 0
    
    for num in A:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Step 2: Verify if the candidate is the actual leader
    leader_count = A.count(candidate)
    
    # If the candidate does not appear more than half the array length, there is no leader
    if leader_count <= n // 2:
        return 0
    
    # Step 3: Count the number of equi leaders
    equi_leaders = 0
    leader_occurrences_left = 0
    leader_occurrences_right = leader_count

    for i in range(n - 1):  # Loop till the second-to-last index
        if A[i] == candidate:
            leader_occurrences_left += 1
            leader_occurrences_right -= 1
        
        # Check if both subarrays have the leader more than half their sizes
        if leader_occurrences_left > (i + 1) // 2 and leader_occurrences_right > (n - i - 1) // 2:
            equi_leaders += 1
    
    return equi_leaders

# Example usage:
#A = [4, 3, 4, 4, 4, 2]
#print(solution(A))  # Output: 2





if __name__ == '__main__':
    print("Hello, Leader!")
    arr = [4, 3, 4, 4, 4, 2]
    print(solution(arr))  # Output: 2