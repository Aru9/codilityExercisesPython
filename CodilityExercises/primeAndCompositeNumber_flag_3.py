
def solution(A):
    n = len(A)
    peak = []
    for i in range(1,n-1):
        if(A[i-1] < A[i] > A[i+1]):
            peak.append(i)
    #print(peak)

    # If no peaks exist, no flags can be placed
    if not peak:
        return 0
    
    

    # Binary Search to for finding peaks and placiing of the flags
    left, right = 1, len(peak)

    while left<=right:
        mid =(left+right)//2
        flags_placed = 1  # Place the first flag at the first peak
        last_flag_position = peak[0]  # The position of the last placed flag

        for i in range(1, len(peak)):
            if(peak[i]- last_flag_position >= mid ):
                flags_placed+=1
                last_flag_position = peak[i]
            if(last_flag_position == mid):
                break
        
        # If we successfully placed `mid` flags, try for more flags
        if flags_placed >= mid:
            max_flags = mid  # Update the result
            left = mid + 1  # Try to increase the number of flags
        else:
            right = mid - 1  # Try fewer flags
    return max_flags


if __name__ == '__main__':
    print("Hello")
    print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))