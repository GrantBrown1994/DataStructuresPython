from AbstractTree import Tree

class AbstractBinaryTree(Tree):
    def left(self,p):
        """returns position of left child"""
        raise NotImplementedError("must be implemented")

    def right(self,p):
        """returns position of right child"""

    def sibling(self,p):
        """returns position of sibling if there is a sibling"""
        parent = self.parent(p)
        if parent is None:
            return None # either empty or its the root
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """generates an iteration of the positions of p's children"""
        if self.num_children(p) != 0:
            if self.left(p) is not None:
                yield self.left(p)
            if self.right(p) is not None:
                yield self.right(p)
