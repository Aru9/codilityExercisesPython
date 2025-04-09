
def solution(A, K):
    """
    Rotates an array to the right K times.

    Parameters:
    A (list): A list of integers.
    K (int): The number of rotations to perform.

    Returns:
    list: The rotated array.
    """
    # Implement your solution here
    if len(A) == 0:
        return A
    for i in range(K):
        A.insert(0,A.pop())
    return A


if __name__ == '__main__':
    print("Array Rotation")
    print("==============")
    A = [3, 8, 9, 7, 6]
    K = 3
    print("Original Array: " + str(A))
    print("Rotated Array: " + str(solution(A, K)))

    