

def solution(S, P, Q):
    # Length of the DNA sequence
    N = len(S)
    
    # Initialize prefix arrays for A, C, G, T
    prefix_A = [0] * (N + 1)
    prefix_C = [0] * (N + 1)
    prefix_G = [0] * (N + 1)
    prefix_T = [0] * (N + 1)
    
    # Fill the prefix arrays
    for i in range(N):
        prefix_A[i + 1] = prefix_A[i] + (1 if S[i] == 'A' else 0)
        prefix_C[i + 1] = prefix_C[i] + (1 if S[i] == 'C' else 0)
        prefix_G[i + 1] = prefix_G[i] + (1 if S[i] == 'G' else 0)
        prefix_T[i + 1] = prefix_T[i] + (1 if S[i] == 'T' else 0)
    
    # Process the queries
    result = []
    for k in range(len(P)):
        start = P[k]
        end = Q[k] + 1  # end is exclusive in the prefix array
        
        # Check if there are any 'A', 'C', 'G', 'T' in the range [start, end-1]
        if prefix_A[end] - prefix_A[start] > 0:
            result.append(1)
        elif prefix_C[end] - prefix_C[start] > 0:
            result.append(2)
        elif prefix_G[end] - prefix_G[start] > 0:
            result.append(3)
        else:
            result.append(4)
    
    return result

    


if __name__ == '__main__':
    print("Array Counter")
    #A = 

    print(solution("CAGCCTA" ,[2,5,0] ,[4,5,6]))


