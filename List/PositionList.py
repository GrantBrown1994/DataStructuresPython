from DoublyLinkedList import _DoublyLinkedBase


class PositionList(_DoublyLinkedBase):

    class Position:
         def __init__(self, container, node):
            self._container = container # positionlist object, give some name becomes container or variable to recognize list position
            self._node = node           # this positionlist object holds all the position objects

    def __init__(self):
        super().__init__()

    def element(self):
        return self._node.element

    def __eq__(self, other):
        return type(other) is type(self) and other.node is self._node

    def __ne__(self, other):
        return not (self == other)  # opposite of eq

    def _validate(self, p):
        if not isinstance(p, self.Position):    # checks to see if p is a position object
            raise TypeError("p must be proper Position type ")
        if p._container is not self:    # makes sure container is a positionlist object
            raise ValueError("p does not belong to this container" )
        if p._node._next is None:  # convention for deprecated nodes
            raise ValueError( "p is no longer valid ")
        return p._node

    def _make_position(self, node):
        if node._element == None:
            return None
        else:
            return self.Position(self, node)

    def _insertBetween(self, e, predecessor, successor):

        node = super()._insertBetween(e, predecessor, successor)
        return self._make_position(node)

    def getContainer(self):
        return self.Position._container

    def addFirst(self, e):
        return self._insertBetween(e, self._header, self._header._next)

    def addLast(self, e):
        return self._insertBetween(e, self._trailer._prev, self._trailer)

    def addBefore(self, p, e):
        current = self._validate(p)
        return self._insertBetween(e, current._prev, current)

    def addAfter(self, p, e):
        current = self._validate(p)
        return self._insertBetween(e, current, current._next)

    def delete(self, p):
        current = self._validate(p)
        return current._deleteNode


if __name__ == "__main__":

    positionNode = PositionList()
    e = "true"
    a = positionNode._insertBetween(e, positionNode._header, positionNode._trailer)