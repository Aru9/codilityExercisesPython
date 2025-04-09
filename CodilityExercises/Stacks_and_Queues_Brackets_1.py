def solution(S):

    stack =[]

    matching_brackets = {')':'(', ']':'[', '}':'{',  }

    for char in S:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack or stack[-1] != matching_brackets[char]:
                return 0
            stack.pop()
    
    return 1 if not stack else 0



if __name__ == '__main__':
    print("Stacks and Queues")
    print(solution("{[()()]}"))