def InsertionSort(data):

    for i in range(1, len(data)):
        current = data[i]
        k = i
        while k > 0 and (data[k-1] > current):
            data[k] = data[k-1]
            k += -1
        data[k] = current


if __name__ == "__main__":

    data = [3,2,1,0]
    InsertionSort(data)
    print(data)
