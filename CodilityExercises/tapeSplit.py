

def solution(A):
    # Implement your solution here
    
    total_sum = sum(A)
    
    # Initialize left sum for the first part
    left_sum = 0
    
    # Initialize the minimal difference with a large number
    min_diff = float('inf')
    
    # Iterate over possible split points P
    for P in range(1, len(A)):  # P ranges from 1 to N-1 (since both parts must be non-empty)
        left_sum += A[P - 1]  # Update the left sum (add the current element to the first part)
        right_sum = total_sum - left_sum  # Calculate the sum of the second part
        
        # Calculate the absolute difference between the two sums
        diff = abs(left_sum - right_sum)
        
        # Update the minimum difference
        min_diff = min(min_diff, diff)
    
    return min_diff

if __name__ == '__main__':
    print("Split")
    A = [3,1,2,4,3]

    for time, position in enumerate(A):
        print(" Time = " + str(time) + " position  = " + str(position))
    B = [ x for x in range (1, 15)]
    print(B)
    print(len(B))
    print(solution(A))
    