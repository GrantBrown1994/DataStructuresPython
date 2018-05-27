class CircularArrayQueue:

    def __init__(self, capacity):
        self._data = [] * capacity
        self._capacity = capacity
        self._front = 0 # start of queue
        self._integer = 0   # number of items
        self._back = 0  # where new item is inserted

    def __len__(self):
        return self._integer

    def getQueue(self):
        return self._data

    def enqueue(self, e):
        if self._integer != self._capacity:
            self._front = self._front % self._capacity
            self._integer += 1
            self._back = (self._front + self._integer) % self._capacity
            self._data.insert(self._back, e)
        else:
            raise Exception()

    def dequeue(self):
        if self._integer != 0:
            self._front = self._front % self._capacity
            self._data[self._front] = None        # if we popped then the list would have to shift all the items
            self._integer += -1                              # to the left in O(n) time
            self._front = (self._front + self._integer) % self._capacity
            self._back = (self._front + self._integer) % self._capacity
        else:
            raise Exception()

    def is_empty(self):
        if self._integer == 0:
            return True
        else:
            return False

    def first(self):
        if self._integer == 0:
            raise Exception()
        else:
            return self._data[self._front]

