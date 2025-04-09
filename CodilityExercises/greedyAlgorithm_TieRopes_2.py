def solution(K, A):
    count = 0
    current_length = 0

    for rope in A:
        current_length += rope
        if current_length >= K:
            count += 1
            current_length = 0

    return count
