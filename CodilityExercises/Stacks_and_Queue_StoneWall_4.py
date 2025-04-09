def solution(H):
    stack = []  # Initialize an empty stack to store block heights
    block_count = 0  # Counter for the number of blocks used
    
    for height in H:
        # Remove blocks from the stack that are taller than the current height
        while stack and stack[-1] > height:
            stack.pop()
        
        # If the stack is empty or the current height is not the same as the top of the stack, push it
        if not stack or stack[-1] != height:
            stack.append(height)
            block_count += 1  # We used a new block
    
    return block_count




if __name__ == '__main__':
    print("Stacks and Queues")
    print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))