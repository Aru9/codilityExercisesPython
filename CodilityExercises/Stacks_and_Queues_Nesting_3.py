def solution(S):
    # Initialize an empty stack
    stack = []
    
    # Iterate over each character in the string S
    for char in S:
        if char == '(':
            # Push opening parentheses onto the stack
            stack.append(char)
        elif char == ')':
            # Check if the stack is not empty and the top is an opening parenthesis
            if not stack:
                # If the stack is empty, it means there's no matching opening parenthesis
                return 0
            # Pop the top of the stack (i.e., a matching opening parenthesis)
            stack.pop()
    
    # If the stack is empty after processing all characters, the string is properly nested
    return 1 if not stack else 0



if __name__ == '__main__':
    print("Stacks and Queues")
    print(solution("(()(())())"))