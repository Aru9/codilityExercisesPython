def solution(A):
    N = len(A)
    
    # Step 1: Count frequencies of all numbers in A
    freq = [0] * (2 * N + 1)  # Frequency array, range is 1 to 2 * N
    for num in A:
        freq[num] += 1
    
    # Step 2: Precompute number of divisors for each number
    divisors_count = [0] * (2 * N + 1)
    
    # For each number i, increment the divisors count for all multiples of i
    for i in range(1, 2 * N + 1):
        for j in range(i, 2 * N + 1, i):
            divisors_count[j] += freq[i]

    # Step 3: For each number in A, calculate the non-divisors
    nonDivisors = []
    for num in A:
        nonDivisors.append(N - divisors_count[num])
    
    return nonDivisors

# Test the solution with the provided example
print(solution([3, 1, 2, 3, 6]))  # Expected output: [2, 4, 3, 2, 0]
