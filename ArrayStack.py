class ArrayStack:

    def __init__(self, capacity):
        self._data = [] * capacity
        self._integer = 0    # number of items in stack currently
        self._top = 0  # index of top of stack

    def getLength(self):
        return len(self._data)

    def push(self, e):

        if self._integer == (len(self._data) - 1):
            raise Exception()

        self._data.insert(self._integer, e)

        if self._integer == 0:
            self._integer += 1
        else:
            self._integer += 1
            self._top += 1

    def pop(self):
        if self._integer != 0:
            self._data.pop()
            self._integer += -1
            self._top += -1
        else:
            raise Exception()

    def returnStack(self):
        return self._data

    def top(self):
        if self._integer != 0:
            return self._data[self._top]
        else:
            raise Exception()

    def is_empty(self):
        if self._integer == 0:
            return True
        else:
            return False
