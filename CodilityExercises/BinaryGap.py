def solution(N):
    """
    Finds the length of the longest binary gap in the binary representation of a given integer.

    A binary gap within a positive integer N is any maximal sequence of consecutive zeros
    that is surrounded by ones at both ends in the binary representation of N.

    Parameters:
    N (int): A positive integer.

    Returns:
    int: The length of the longest binary gap. If there is no binary gap, returns 0.
    """
    # Implement your solution here
    binary_representation = str(format(N,'b'))
    #print(binary_representation)
    tmp_gap=0
    maxGap = 0
    sc =False
    for i in range(len(binary_representation)):
        if (binary_representation[i] == '1' and sc == False):
            sc = True
            tmp_gap=0
        elif (binary_representation[i] == '1' and sc == True):
            sc = True
            maxGap = max(tmp_gap,maxGap)
            tmp_gap=0
            #print("New Maxgap after compare " + str(maxGap))
        elif (binary_representation[i] == '0' and sc == True):
            tmp_gap += 1
            #print("Current Number " + binary_representation[i] + " - Current Gap " + str(tmp_gap) + " - Max Gap " + str(maxGap))
    
    return maxGap


# The following is code to output the results. You do not need to modify it
if __name__ == '__main__':
    N = [1041, 15, 32, 529, 20, 9, 529, 1041, 133137]
    for number in N:
        print("Current Numbers solution " + str(number) + " " + str(solution(number)))
   