def solution(M, A):
    # Implement your solution here
    n =len(A)
    count = 0
    left = 0
    seen = {}
    limit = 1000000000

    for right in range(n):
        if ( A[right] in seen and seen[A[right]] >= left ):
            left = seen[A[right]] + 1
        seen[A[right]] = right
        count += right-left + 1
        if count > limit :
            return limit
    return count


print(solution(6, [3, 4, 5, 5, 2]))