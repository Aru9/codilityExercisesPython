def solution(A):
    # Implement your solution here
    maxSum = curSum = A[0]
    for i in range(1, len(A)):
        curSum = max(A[i], curSum + A[i])
        maxSum = max(maxSum,curSum)
    
    return maxSum






if __name__ == '__main__':
    print("Hello, Max Slice Problems")
    print(solution([3, 2, -6, 4, 0]))


#     max_ending = max_slice = 0
# 3 for a in A:
# 4 max_ending = max(0, max_ending + a)
# 5 max_slice = max(max_slice, max_ending)
# 6 return max_slice