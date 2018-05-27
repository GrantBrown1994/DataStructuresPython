class Tree:

    class Position:

        def element(self):
            """gives element at this position"""
            raise NotImplementedError("must be implemented")

        def __eq__(self):
            """True if two positions are equal to each other"""
            raise NotImplementedError("must be implemented")

        def __ne__(self):
            """True if new position"""
            raise NotImplementedError("must be implemented")

    def root(self):
        """Return position of root"""
        raise NotImplementedError("must be implemented")

    def num_children(self, p):
        """returns number of children"""
        raise NotImplementedError("must be implemented")

    def parent(self,p):
        """Returns parent of position p"""
        raise NotImplementedError("must be implemented")

    def __len__(self):
        """Total number of elements in tree"""
        raise NotImplementedError("must be implemented")

    def is_root(self, p):

        if self.root() == p:
            return True
        else:
            return False

    def is_leaf(self,p):
        """returns true if no children"""
        return self.num_children(p) == 0

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

