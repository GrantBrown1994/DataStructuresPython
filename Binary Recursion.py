def binarysum(S, start, stop):

    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binarysum(S, start, mid) + binarysum(S, mid, stop)



a = binarysum([0,1,2,3,4,5,6,7,8], 0, 9)
print(a)
