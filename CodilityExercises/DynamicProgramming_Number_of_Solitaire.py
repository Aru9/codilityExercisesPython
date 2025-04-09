def solution_dp_readable(A):
    """
    Calculates the maximal result achievable in the dice game using dynamic programming.

    Args:
        A: A list of integers representing the numbers on the squares.  A is board Valuies

    Returns:
        The maximal sum of numbers on marked squares to reach the end.
    """
    num_squares = len(A)
    if num_squares == 1:
        return A[0]

    # dp[i] stores the maximum result to reach square i
    max_results = [-float('inf')] * num_squares
    max_results[0] = A[0]  # Starting square is marked

    for current_square in range(1, num_squares):
        # Consider all possible previous squares from which we could reach the current square
        for previous_square in range(max(0, current_square - 6), current_square):
            # A valid move exists from previous_square to current_square
            if max_results[previous_square] != -float('inf'):
                # Update the maximum result to reach the current square
                # by considering the best result to reach the previous square
                # plus the value of the current square (which will be marked)
                max_results[current_square] = max(
                    max_results[current_square],
                    max_results[previous_square] + A[current_square]
                )

    # The maximal result to reach the last square
    final_result = max_results[num_squares - 1]

    # If the last square is unreachable (which shouldn't happen based on the problem), return 0
    return final_result if final_result != -float('inf') else 0


print(solution_dp_readable([1, -2, 0, 9, -1, -2]))


def solution(A):
    """
    Calculates the maximal result achievable in the dice game using dynamic programming.

    Args:
        A: A list of integers representing the numbers on the squares.

    Returns:
        The maximal sum of numbers on marked squares to reach the end.
    """
    num_squares = len(A)
    if num_squares == 1:
        return A[0]

    # dp[i] stores the maximum result to reach square i
    max_results = [-float('inf')] * num_squares
    max_results[0] = A[0]  # Starting square is marked

    for current_square in range(1, num_squares):
        # Consider all possible previous squares from which we could reach the current square
        for previous_square in range(max(0, current_square - 6), current_square):
            # A valid move exists from previous_square to current_square
            if max_results[previous_square] != -float('inf'):
                # Update the maximum result to reach the current square
                # by considering the best result to reach the previous square
                # plus the value of the current square (which will be marked)
                max_results[current_square] = max(
                    max_results[current_square],
                    max_results[previous_square] + A[current_square]
                )

    # The maximal result to reach the last square
    final_result = max_results[num_squares - 1]

    # If the last square is unreachable (which shouldn't happen based on the problem), return 0
    return final_result if final_result != -float('inf') else 0