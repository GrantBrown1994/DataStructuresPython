class CircularLinkedQueue:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None       # a node object will be the tail
        self._size = 0

    def enqueue(self, e):

        new = self._Node(e, None)           # will be tail node
        if self._size == 0:
            new._next = new     # make list circular even though there is just one element
        else:
            new._next = self._tail._next        # new node point to head
            self._tail_next = new           # make old tail point to new tail
        self._tail = new
        self._size += 1

    def dequeue(self):

        if self._size == 0:
            raise Exception()
        dequeued = self._tail._next
        if self._size == 1:
            self._tail = None   # list becomes empty
        self._tail._next = dequeued._next   # Node old head pointed to becomes new head
        self._size -= 1
        return dequeued._element

    def rotate(self):

        # makes front element last element
        if self._size == 0:
            raise Exception()
        else:
            self._tail = self._tail._next
