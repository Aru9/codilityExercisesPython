import math

def primeFactors(num, primearray):
    divisor = set()
    for primeNum in primearray:
        if primeNum * primeNum > num:
            break
        while (num%primeNum == 0):
            #print()
            divisor.add(primeNum)
            num//=primeNum
    if num > 1:
        divisor.add(num)
    return divisor

def solution(A, B):
    # Implement your solution here
    
    limit = max(A+B)
    n = int(math.sqrt(limit))
    #n = len(A)
    # Find prime to the limit , that is to the lagest number , starting with 2
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= n):
        if (sieve[i]):
            k = i * i
            while (k <= n):
                sieve[k] = False
                k += i
        i += 1
    
    primeList = [ index for index,x in enumerate(sieve) if x== True]
    #print(primeList)
    count = 0
    for i in range(len(A)):
        primeFactor_A = primeFactors(A[i],primeList)
        primeFactor_B = primeFactors(B[i],primeList)
        #print(" A "+ str(primeFactor_A) + " ,B " + str(primeFactor_B) )
        if ( primeFactor_A == primeFactor_B ):
            count+=1
    
    return count

def bestsolution(a_pts, b_pts):
    """Solution method implementation."""
    cnt = 0
    for i, _ in enumerate(a_pts):
        # pick pair of numbers to analyze
        a_elem, b_elem = a_pts[i], b_pts[i]
 
        # calculate their gcd       
        gcd = math.gcd(a_elem, b_elem)
        # initialize the pair of gcds
        gcd_a, gcd_b = 0, 0
        # systematically reduce the two numbers to (1, 1)
        # by successively dividing them by the initial gcd
        while (gcd_a, gcd_b) != (1, 1):
            gcd_a = math.gcd(a_elem, gcd)
            gcd_b = math.gcd(b_elem, gcd)
            a_elem //= gcd_a
            b_elem //= gcd_b
        # our pair of numbers has common prime divisors
        cnt += 1 if (a_elem, b_elem) == (1, 1) else 0
    return cnt

    

print(solution([15, 10, 9], [75, 30, 5]))
