def solution(A):

    N = len(A)

    events = []

    #Lets find the start and end for the each of the discs, we will add tuples to the list
    for i in range(N):
        start = i - A[i]
        end = i + A[i]
        events.append((start, 'start', i))
        events.append((end, 'end', i))

    # Now sort them first based on the position on the x-axis , so from the tuple x , x[0] , and if two x-axis positions are same , then sort based on start and end , with start coming first and end next
    # We are doing this sort , so we can count the active disc based on start and removing an active disc based on end

    events.sort(key=lambda x: (x[0],x[1]=='end') )

    # Now when we encounter start we start counting by incrementing the active disc , which is nothing but disc which would intersect
    # And we decrease the active disc when we encounter end , signifying the disc should not be counted against active disc

    active_disc = 0
    intersection_cnt = 0

    for event in events:
        position, event_type, index = event

        if event_type == 'start':
            intersection_cnt+=active_disc
            if intersection_cnt > 10_000_000:
                return -1
            active_disc+=1
        elif event_type == 'end':
            active_disc-=1
    
    return intersection_cnt


    



if __name__ == '__main__':
    print("Array Counter")
    print(solution([1,5,2,1,4,0]))