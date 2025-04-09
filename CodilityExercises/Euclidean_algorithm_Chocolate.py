def solution(N,M):
    choc = [True] * N

    count = 0
    index = 0

    while(choc[index]):
        choc[index] = False
        index +=M
        count +=1
        if(index>=N):
            index = abs(N-index)
    return count





print(solution(10,4))
