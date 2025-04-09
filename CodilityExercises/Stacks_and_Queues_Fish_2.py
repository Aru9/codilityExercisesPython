
UPSTREAM, DOWNSTREAM = 0, 1  # Constants to represent upstream (0) and downstream (1)

def solution(A: list, B: list):
    downstream_fish_stack = []  # Stack to track downstream fish
    surviving_upstream_fish = 0  # Counter for surviving upstream fish

    # Iterate through each fish based on its size and direction
    for fish_size, fish_direction in zip(A, B):
        
        # If the fish is moving downstream
        if fish_direction == DOWNSTREAM:
            downstream_fish_stack.append(fish_size)  # Add the fish to the stack
        else:
            # If the fish is moving upstream, check for collisions with downstream fish
            while downstream_fish_stack:
                # If the fish at the top of the stack is smaller, it gets eaten
                if downstream_fish_stack[-1] < fish_size:
                    downstream_fish_stack.pop()  # The current fish eats the smaller fish
                else:
                    # The upstream fish is smaller and gets eaten, so break the loop
                    break
            else:
                # If no downstream fish remains, the upstream fish survives
                surviving_upstream_fish += 1

    # The total number of survivors is the downstream fish left in the stack 
    # plus the surviving upstream fish
    return len(downstream_fish_stack) + surviving_upstream_fish



    



if __name__ == '__main__':
    print("Stacks and Queues")
    print(solution([4,3,2,1,5],[0,1,0,0,0]))