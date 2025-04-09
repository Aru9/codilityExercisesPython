# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def hunderedPercentsolution(A):
    # write your code in Python 3.6
    A.append(1)
    target = len(A)
    fib = fibonacci(target)
    dp = {-1: 0}
    for i in range(target):
        if A[i] == 0: continue
        temp_result = []
        for jump in fib:
            if jump > i + 1: break
            if i - jump in dp:
                print(" Before i : " + str(i) + " jump : " + str(jump) +  " i-jump : " + str(i-jump)  + " dp : "   + str(dp) + " temp_result : " + str(temp_result))
                temp_result.append(dp[i - jump] + 1)
                print(" After i : " + str(i) + " jump : " + str(jump) +  " i-jump : " + str(i-jump)  + " dp : "   + str(dp)+ " temp_result : " + str(temp_result))
        if temp_result:
            dp[i] = min(temp_result)
            print("Under if condition temp_results i : " + str(i) + " jump : " + str(jump) +  " i-jump : " + str(i-jump)  + " dp : "   + str(dp)+ " temp_result : " + str(temp_result))
    return dp.get(target - 1, -1)

def fibonacci(n):
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib


from collections import deque

def solution(A):
    N = len(A)
    
    # Handle edge case where N is 0, the frog is already on the other bank
    if N == 0:
        print("Edge case: No positions in the river.")
        return 0
    
    # Precompute all Fibonacci numbers up to N
    fib = [1, 1]
    while fib[-1] <= N:
        fib.append(fib[-1] + fib[-2])
    
    #print(f"Fibonacci numbers up to N: {fib}")  # Debug print

    # BFS setup
    queue = deque([(-1, 0)])  # (position, jumps)
    visited = [False] * (N + 1)
    visited[0] = True  # Start from the bank, position -1 corresponds to position 0

    #print(f"Starting BFS from position -1 (index 0), initial queue: {queue}")  # Debug print
    
    # Perform BFS
    while queue:
        current, jumps = queue.popleft()
        
        #print(f"\nVisiting position {current} (jumps so far: {jumps}), queue: {queue}")  # Debug print
        
        # Try all possible jumps from current position
        for f in fib:
            next_position = current + f
            #print(f"  Trying jump of size {f}, which leads to position {next_position}")
            
            if next_position == N:  # If we reach the other side, return jumps + 1
                #print(f"  Reached the other side at position {next_position}, returning {jumps + 1}")
                return jumps + 1
            
            if 0 <= next_position < N and A[next_position] == 1 and not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, jumps + 1))
                #print(f"  Added position {next_position} to the queue, new queue: {queue}")  # Debug print
    
    # If we can't reach position N, return -1
    #print("Couldn't reach the other side, returning -1")
    return -1

# Test the function with the given example
A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
result = solution(A)
print(f"Result: {result}")
