def solution(A):
    # write your code in Python 3.6
    
    peak_list = []
    
    # find peaks
    for index in range( 1, len(A)-1 ):
        if A[index] > A[index-1] and A[index] > A[index+1]:
            peak_list.append( index )
    
    # print(peak_list)

    for num_block in range( len(A), 0 , -1 ):

        # check 'blocks containing the same number of elements'
        if ( len(A) % num_block == 0):
            
            block_size = int( len(A)/num_block ) 
            ith_block = 0
            num_block_has_peak = 0
            
            for peak_index in peak_list:
                
                # check if any peak is within the ith block
                if int( peak_index/block_size) == ith_block: 
                    num_block_has_peak += 1
                    ith_block += 1
        
            # chek if all blocks have at least one peak
            if num_block_has_peak == num_block:
                return num_block
    
    return 0



# Test the solution with the provided example
print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))  # Expected output: 3
