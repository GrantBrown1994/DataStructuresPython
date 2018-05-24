#checking for element uniqueness recursive algorithm


# element unique recursion algorithm

def elementUnique(S):

    if len(S) == 1:
        return True
    first = S[0]
    remainder = S[1:]
    if elementUnique(remainder):
        if first in remainder:
            return False
        else:
            return True



if __name__ == "__main__":

    S = [0, 1, 2, 3, 4, 5, 6]

    b = elementUnique(S)
    if b == True:
        print("True")
    else:
        print("False")