# calculate sum of numbers

def sum(S, n):

    if n == 0:
        return 0

    return sum(S, n-1) + S[n-1]


if __name__ == "__main__":

    S = [2,3,4,5 ,7, 8, 1, 2, 9,2 ,3]

    print(str(sum(S, len(S))))