def solution(A, B, C):
    """
    Finds the minimum number of nails needed to nail all planks (more performant).

    Args:
        A: An array of start points of planks.
        B: An array of end points of planks.
        C: An array of nail positions.

    Returns:
        The minimum number of nails needed, or -1 if not all planks can be nailed.
    """
    n = len(A)
    m = len(C)

    planks = sorted(zip(A, B), key=lambda x: x[1])  # Sort planks by end position

    def check(num_nails):
        """
        Checks if using the first num_nails nails is sufficient to nail all planks.
        """
        nailed = [False] * n
        used_nails = sorted(C[:num_nails])
        nailed_count = 0

        nail_idx = 0
        for i in range(n):
            if nailed[i]:
                continue

            start, end = planks[i]
            while nail_idx < len(used_nails) and used_nails[nail_idx] <= end:
                nail = used_nails[nail_idx]
                if start <= nail <= end:
                    nailed[i] = True
                    nailed_count += 1
                    break
                nail_idx += 1
            if not nailed[i] and nail_idx == len(used_nails) and any(not n for n in nailed):
                return False  # Remaining planks cannot be nailed with these nails

        return nailed_count == n

    low = 1
    high = m
    min_nails = -1

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            min_nails = mid
            high = mid - 1
        else:
            low = mid + 1

    return min_nails