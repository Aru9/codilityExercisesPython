

def solution(A):
    # Implement your solution here
    N = len(A)

    if N < 2:
        return -1
    
    min_avg = float('inf')
    min_index = -1 

    for i in range(N-1):
        avg_2 = (A[i] + A[i+1])/2
        if avg_2 < min_avg:
            min_avg =avg_2
            min_index = i

        if i+2 < N:
            avg_3 = (A[i] + A[i+1] + A[i+2])/3
            if avg_3 < min_avg:
                min_avg =avg_3
                min_index = i
    return min_index


if __name__ == '__main__':
    print("Array Counter")
    print(solution([4, 2, 2, 5, 1, 5, 8]))

