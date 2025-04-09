def solve_improved(arr):
    n = len(arr)
    if n <= 2:
        return n

    max_len = 2
    current_len = 2

    for i in range(2, n):
        if arr[i] == arr[i - 2]:
            current_len += 1
        else:
            current_len = 2
        max_len = max(max_len, current_len)

    return max_len


print(solve_improved( [3, 7, 3, 7, 2, 1, 2]))
print(solve_improved([1, 5, 6, 0, 1, 0]))