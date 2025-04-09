def solution(A):
    absLst = [ abs(a) if a< 0 else a for a in A  ]
    #print(absLst)
    absDistinct = set(absLst)
    #print(absDistinct)
    #print(len(absDistinct))
    return len(absDistinct)





print(solution([-5, -3, -1, 0, 3, 6]))