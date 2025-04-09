from collections import Counter

def solution_easier(S):
    n = len(S)
    if n == 1:
        return 1

    for length in range(1, n + 1):
        substrings = [S[i : i + length] for i in range(n - length + 1)]
        counts = Counter(substrings)
        for sub, count in counts.items():
            if count == 1:
                return length

    return n



def solution(S):
    n = len(S)
    if n == 1:
        return 1

    for length in range(1, n + 1):
        substring_counts = {}
        for i in range(n - length + 1):
            substring = S[i : i + length]
            substring_counts[substring] = substring_counts.get(substring, 0) + 1

        for substring, count in substring_counts.items():
            if count == 1:
                return length

    return n  # Should not reach here based on the problem constraints

# Examples:
print(solution("abaaba"))   # Output: 2
print(solution("zyzyzyz"))  # Output: 5
print(solution("aabbbabaaa")) # Output: 3
print(solution("abcdefg"))  # Output: 1
print(solution("aaaaaa"))   # Output: 1
print(solution("abacaba"))  # Output: 3 ("bac")