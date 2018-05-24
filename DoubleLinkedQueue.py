from DoublyLinkedList import _DoublyLinkedBase


class DoubleLinkedQueue(_DoublyLinkedBase):

    def __init__(self):
        super().__init__()

    def last(self):
        if self._size == 0:
            raise Exception()
        return self._trailer._prev._element

    def first(self):
        if self._size == 0:
            raise Exception()
        return self._header._next._element

    def inset_first(self, e):
        self._insertBetween(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insertBetween(e, self._trailer._prev, self._trailer)

    def delete_first(self):

        if self._size == 0:
            raise Exception()
        return self._deleteNode(self._header._next)

    def delete_last(self):
        if self._size == 0:
            raise Exception()
        return self._deleteNode(self._trailer._prev)