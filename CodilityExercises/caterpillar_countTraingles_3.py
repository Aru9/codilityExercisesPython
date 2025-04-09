def solution(A):
    A.sort()
    N = len(A)
    count = 0

    for i in range(N - 2):
        k = i + 2
        for j in range(i + 1, N - 1):
            while k < N and A[i] + A[j] > A[k]:
                k += 1
            count += k - j - 1

    return count
