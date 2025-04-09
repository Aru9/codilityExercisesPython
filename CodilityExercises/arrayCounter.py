def solution(N, A):
    counter = [0] * N

    for i in A:
        if i <= N:
            #print("Updating i " + str(i))  
            counter[i-1] += 1
            #print(counter)
        else:
            counter = [max(counter)] * N
            #print(counter) 

    return counter

def solution1(N, A):
    # Initialize counters to 0, and variables for tracking the max value and last update
    counters = [0] * N
    current_max = 0
    last_update = 0

    for operation in A:
        if 1 <= operation <= N:
            # Before increasing, we must ensure the counter is updated correctly considering the last "max counter"
            if counters[operation - 1] < last_update:
                counters[operation - 1] = last_update
            # Perform the increase operation
            counters[operation - 1] += 1
            # Update the current max if needed
            if counters[operation - 1] > current_max:
                current_max = counters[operation - 1]
        else:
            # Perform the max counter operation
            last_update = current_max

    # Ensure that all counters are updated to at least the last "max counter" value
    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters



if __name__ == '__main__':
    print("Array Counter")
    #A = 

    print(solution(5,[3,4,4,6,1,4,4]))