def solution(S):
    deletions = 0
    count_b = 0

    for ch in S:
        if ch == 'A':
            deletions = min(deletions + 1, count_b)
        else:
            count_b += 1

    return deletions


def solution(S):
    N = len(S)
    prefix_B = [0] * (N + 1)
    suffix_A = [0] * (N + 1)

    for i in range(1, N + 1):
        prefix_B[i] = prefix_B[i - 1] + (1 if S[i - 1] == 'B' else 0)

    for i in range(N - 1, -1, -1):
        suffix_A[i] = suffix_A[i + 1] + (1 if S[i] == 'A' else 0)

    min_deletions = float('inf')
    for i in range(N + 1):
        min_deletions = min(min_deletions, prefix_B[i] + suffix_A[i])

    return min_deletions
