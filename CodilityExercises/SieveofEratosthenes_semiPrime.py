import math

def Mysolution(N, P , Q):
    out = list()
    n = len(P)
    
    #First lets get the prime number between starting from 2 till n
    sieve = [True] * (N+1) 
    #print(sieve)
    for i in range(2,N+1):
        if sieve[i]:
            out.append(i)
            for j in range(i,N+1,i):
                sieve[j]=False
    
 
    semiPrime = sorted({ x * y for x in out for y in out})
    smCnt = [0] * (n)
    for i in range(n):
        count = 0
        for num in semiPrime:
            if (P[i]<= num <= Q[i] and num <= N):
                smCnt[i]+=1
        
    return smCnt

import math

def solution(N, P, Q):
    # write your code in Python 3.6
    
    # 1
    # find primes: use 'Sieve of Eratosthenes'
    prime_list_boolean = [True] * (N+1) # note: plus one for "0"
    prime_list_boolean[0] = False   
    prime_list_boolean[1] = False
    for i in range( 2, math.floor(math.sqrt(N))+1 ):
        if prime_list_boolean[i] == True:
            j = i + i
            for not_prime in range( j, N+1, i ):
                prime_list_boolean[not_prime] = False
    
    # 2
    # append 'prime' to list
    prime_list = []
    for index in range( N+1 ):
        if prime_list_boolean[index] == True:
            prime_list.append(index)
    print(prime_list)
    
    # 3
    # find semi-primes
    semiprime_list_boolean = [False] * (N+1) # note: plus one for "0"
    for i in range( len(prime_list) ):
        for j in range(i, len(prime_list), 1):
            semiprime_temp = prime_list[i] * prime_list[j] 
            if semiprime_temp > N:
                break
            else:
                semiprime_list_boolean[semiprime_temp] = True
    print(semiprime_list_boolean)
    # 4
    # count the number of semi-primes
    count_semiprime_list = [0] * (N+1)
    num_semiprime_so_far = 0
    for i in range(N+1):
        if semiprime_list_boolean[i]==True:
            num_semiprime_so_far += 1
        count_semiprime_list[i] = num_semiprime_so_far
    #print(count_semiprime_list)
    print(count_semiprime_list)
    
    # 5
    # return answers to all the queries
    answer_list = [0] * len(P)
    for i in range( len(P) ):
        begin_value = P[i]
        end_value = Q[i]
        #print(count_semiprime_list[end_value])
        #print(count_semiprime_list[begin_value])
        # be very careful about the 'begin_value' (not included)
        answer_list[i] = count_semiprime_list[end_value] - count_semiprime_list[ (begin_value-1) ]
    #print(answer_list)
    
    return answer_list

# Test the solution with the provided example
#N = 26
#P = [1, 4, 16]
#Q = [26, 10, 20]
#print(solution(N, P, Q))  # Expected output: [10, 4, 0]

        

    

    

# Test the solution with the provided example
print(solution(26, [1, 4, 16], [26, 10, 20]))  # Expected output:  [10, 4, 0]
