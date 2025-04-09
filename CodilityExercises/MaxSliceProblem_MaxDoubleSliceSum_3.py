def solution(A):
    N = len(A)
    
    # Edge case, we need at least 3 elements to form a double slice
    if N < 3:
        return 0
    
    # Arrays to store the maximum possible slice sums for left and right parts
    max_left = [0] * N  # max_left[i] is the maximum sum of slice ending before i
    max_right = [0] * N  # max_right[i] is the maximum sum of slice starting after i
    
    # Fill max_left
    for i in range(1, N - 1):
        max_left[i] = max(0, max_left[i - 1] + A[i])
    
    # Fill max_right
    for i in range(N - 2, 0, -1):
        max_right[i] = max(0, max_right[i + 1] + A[i])
    
    # Now we compute the maximum sum of the double slice for any valid middle point Y
    max_sum = 0
    for Y in range(1, N - 1):
        # Double slice is made of max_left[Y-1] + max_right[Y+1]
        max_sum = max(max_sum, max_left[Y - 1] + max_right[Y + 1])
    
    return max_sum







if __name__ == '__main__':
    print("Hello, Max Slice Problems")
    print(solution([3, 2, 6, -1, 4, 5, -1, 2]))


#     max_ending = max_slice = 0
# 3 for a in A:
# 4 max_ending = max(0, max_ending + a)
# 5 max_slice = max(max_slice, max_ending)
# 6 return max_slice