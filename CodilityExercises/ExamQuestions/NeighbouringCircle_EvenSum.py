def solution(A):
    N = len(A)
    used = [False] * N  # To track which elements are already paired
    count = 0

    for i in range(N):
        if not used[i]:
            j = (i + 1) % N
            if not used[j] and (A[i] + A[j]) % 2 == 0:
                used[i] = True
                used[j] = True
                count += 1

    return count
