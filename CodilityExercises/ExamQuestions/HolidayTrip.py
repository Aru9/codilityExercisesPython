def solution(P, S):
    total_pass = sum(P)
    res = 0
    S.sort(reverse=True)
    for i in S:
        if total_pass - i > 0:
            total_pass = total_pass - i
            res += 1
        else:
            res += 1
    return res

def solution(P, S):
    total_pass = sum(P)
    res = 0
    S.sort(reverse=True)

    for seats in S:
        total_pass -= seats
        res += 1
        if total_pass <= 0:
            break

    return res



def solution(P, S):
    total_people = sum(P)
    car_seats = sorted(S, reverse=True)  # Sort cars by capacity descending

    cars_used = 0
    seats_accumulated = 0

    for seats in car_seats:
        seats_accumulated += seats
        cars_used += 1
        if seats_accumulated >= total_people:
            break

    return cars_used
