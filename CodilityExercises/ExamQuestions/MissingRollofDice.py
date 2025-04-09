def solution(A, F, M):
    n = len(A)
    total_rolls = n + F
    sum_known = sum(A)
    required_sum = M * total_rolls
    sum_missing = required_sum - sum_known

    if sum_missing < F or sum_missing > 6 * F:
        return [0]

    missing_rolls = [0] * F
    base_value = sum_missing // F
    remainder = sum_missing % F

    for i in range(F):
        missing_rolls[i] = base_value + (1 if i < remainder else 0)

    return missing_rolls