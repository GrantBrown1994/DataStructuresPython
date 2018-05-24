from Queue import CircularArrayQueue

if __name__ == "__main__":

    data = CircularArrayQueue(10)
    data.enqueue(1)
    data.enqueue(2)
    print(data.getQueue())
    data.dequeue()
    print(data.getQueue())

