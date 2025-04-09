
def solution(N):
    i=1
    minimum_value = 1_000_000_000

    while(i*i < N):
        if( N % i == 0):
            minimum_value = min(minimum_value, (i + (N//i) ) )
        i+=1
    if(i*i == N):
        minimum_value = min(minimum_value, ( i*2 ) )

    return 2*minimum_value


if __name__ == '__main__':
    print("Hello")
    print(solution(30))