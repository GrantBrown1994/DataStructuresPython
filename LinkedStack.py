class SingleLinkedStack:

# -------------------------------------------------------------------------------------------------------
    class _Node:

        def __init__(self, element, next):
            self._element = element
            self._next = next  # points toward the next node

# -------------------------------------------------------------------------------------------------------

    # head will be start of stack since it is easy to locate close to the head

    def __init__(self):

        self._head = None  # no head at first
        self._size = 0

    def __len__(self):
        return self._size

    # starts at head and points to new elements downward the list
    def push(self, e):
        self._head = self._Node(e, self._head)       # push the first head back and point to it, first entry is the tail in the end
        self._size += 1

    def pop(self):

        if self._size == 0:
            raise Exception()
        else:
            popped = self._head._element
            self._head = self._head._next
            self._size += -1
            return popped

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
