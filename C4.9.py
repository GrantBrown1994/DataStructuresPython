
def findMaxMin(S, lower, upper):

    mid = (upper + lower) // 2

    if lower == mid:
        return max(S[mid], S[upper]), min(S[mid], S[upper])
    else:
        fmax, fmin = findMaxMin(S, lower, mid)
        smax, smin = findMaxMin(S, mid, upper)
        return max(fmax, smax), min(fmin, smin)


# Do not use the code below, it is a linear recursion vs  binary as above but it is O(n) and requires O(n) disk space
# wheras the code above is binary recursion and the disk usage is O(log n) since the length is being cut in half

#def findMaxMin(S, n):
 #       print()
  #      if n == 0:
   #         a = S[n]
    #        b = S[n]
     #       return a, b
      #  max, min = findMaxMin(S, n - 1)
       # a = S[n]  # min
        #b = S[n]  # max
        #if a <= min:
         #   min = a
        #elif b <= min:
         #   min = b
        #elif a >= max:
         #   max = a
        #elif b >= max:
         #   max = b
        #return max, min

if __name__ == "__main__":

    S = [1, 9, 6, 2, 8, 7]

    max, min = findMaxMin(S, 0, len(S) - 1)

    print(str("Max is " + str(max) + "  Min is "+ str(min)))
