def solution(A):
    if len(A) == 0:
        return 0

    # 1. Work with absolute values: The sign choice is independent for each element.
    abs_A = [abs(A[i]) for i in range(len(A))]  # O(N)

    # 2. Find the maximum absolute value and count occurrences:
    max_value = max(abs_A)
    count = [0] * (max_value + 1)
    for a in abs_A:
        count[a] += 1
    # `count[x]` now stores how many times the absolute value `x` appears in A.

    # 3. Calculate the total sum of absolute values:
    total_sum = sum(abs_A)  # O(N)

    # 4. Dynamic Programming to find reachable partial sums:
    # dp[i] >= 0 means a partial sum of 'i' can be achieved using a subset of abs_A.
    # The value of dp[i] stores the remaining count of the last used absolute value
    # to ensure we don't use it more times than it appears in abs_A.
    dp = [-1] * (total_sum + 1)
    dp[0] = 0  # A sum of 0 is always achievable (by using no elements).

    # Iterate through each possible absolute value (from 1 to max_value):
    for a in range(1, max_value + 1):
        if count[a] <= 0:
            continue  # If this absolute value is not in A, skip it.

        # Iterate through all possible partial sums (from 0 to total_sum):
        for partial_sum in range(total_sum):
            # If 'partial_sum' is already reachable (dp[partial_sum] >= 0),
            # it means we haven't used the current absolute value 'a' to reach it yet
            # in this inner loop iteration. We can now potentially use 'a'.
            if dp[partial_sum] >= 0:
                dp[partial_sum] = count[a]  # Mark that we can use 'a' up to its count.

            # If 'partial_sum' is not yet reachable (dp[partial_sum] == -1),
            # but 'partial_sum' is greater than or equal to the current absolute value 'a',
            # AND if 'partial_sum - a' was reachable (dp[partial_sum - a] > 0),
            # it means we can reach 'partial_sum' by including one instance of 'a'.
            elif partial_sum >= a and dp[partial_sum - a] > 0:
                dp[partial_sum] = dp[partial_sum - a] - 1 # Decrement the remaining count of 'a' used to reach 'partial_sum'.

    # 5. Find the partial sum closest to total_sum / 2:
    # Iterate downwards from total_sum // 2. The first reachable partial sum we find
    # will give us the minimum absolute difference.
    for partial_sum in range(total_sum // 2, -1, -1):
        if dp[partial_sum] >= 0:
            # If 'partial_sum' is reachable, it represents the sum of one subset.
            # The sum of the other subset would be 'total_sum - partial_sum'.
            # The minimum absolute difference is the absolute difference between these two sums.
            return total_sum - 2 * partial_sum

    # This should ideally not be reached if total_sum is non-negative.
    return 0