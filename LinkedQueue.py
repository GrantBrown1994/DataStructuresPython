class SingleLinkedQueue:

    # -------------------------------------------------------------------------------------------------------
    class _Node:

        def __init__(self, element, next):
            self._element = element
            self._next = next  # points toward the next node

    # -------------------------------------------------------------------------------------------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, e):
        new = self._Node(e, None)

        if self._size == 0:
            self._head = new
        else:
            self._tail._next = new      # not overriding current tail, just making new entry to tail and pointing to it
        self._tail = new                # then setting the new tail to this new entry
        self._size += 1

    def dequeue(self):

        if self._size == 0:
            raise Exception()
        else:
            ans = self._head._element
            self._head = self._head._next
            self._size += -1
            if self._size == 0:
                self._tail = None
            return ans

    def __len__(self):
        return self._size

    def first(self):
        if self._size == 0:
            raise Exception()
        return self._head._element