

def solution(A):
    # Implement your solution here
    A.sort()
    for i in range(0,len(A),2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]


if __name__ == '__main__':
    print("Unpaired")
    A = [9,6,5,1,2,3,4,7]
    # print(str(len(A)//2))
    # print(type(A))
    # print(type(A[0]))
    # print(A)
    # A.sort()
    # print(A)
    # print( str(A.pop(0)) + " " + str(A.pop(1)) )
    # print(A)
    # R= [x for x in range(0,len(A),2)]
    # print(R)


    N = len(A)
    
    # XOR all numbers from 1 to N+1
    total_xor = 0
    for i in range(1, N + 2):  # from 1 to N+1
        total_xor ^= i
        print("Curren XOR : " + str(total_xor) + " for i = " + str(i) )
    
    # XOR all elements in the array A
    array_xor = 0
    for num in A:
        array_xor ^= num
        print("Curren array_xor : " + str(array_xor) + " for num = " + str(num))
    
    # The missing number is the XOR of the above two results
    print( total_xor ^ array_xor )