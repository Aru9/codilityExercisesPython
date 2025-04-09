class Solution:
    def solution(self, A):
        A.sort()
        num_guests = len(A)
        rooms = 0
        guest_index = 0

        while guest_index < num_guests:
            rooms += 1
            capacity = A[guest_index]
            guests_in_room = 0

            while guest_index < num_guests and guests_in_room < capacity:
                guests_in_room += 1
                guest_index += 1

        return rooms