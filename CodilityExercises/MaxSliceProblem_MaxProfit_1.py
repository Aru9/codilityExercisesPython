def solution(A):
    # Implement your solution here
    if len(A)<2:
        return 0
    
    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

        if price < min_price:
            min_price=price

    return max_profit






if __name__ == '__main__':
    print("Hello, Max Slice Problems")
    print(solution([23171, 21011, 21123, 21366, 21013, 21367]))