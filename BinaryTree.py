from BinaryTreeAbstract import AbstractBinaryTree
from LinkedQueue import SingleLinkedQueue

#   creating a balanced left binary tree here, if any
#   node has more then 2 children then it is not balanced
#   left comes before right in precedence
#   notice the use of encapsulation
# for a general tree just use a list to contain references to the children positions
# and iterate through them if needed
class LinkedBinaryTree(AbstractBinaryTree):

    class _Node:

        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(AbstractBinaryTree.Position):

        def __init__(self, container, node):
            """decleares container and node of Tree's current position"""
            self._container = container
            self._node = node

        def element(self, p):
            node = self._validate(p)
            return node._element

        def __eq__(self, p):
            """Checks to see if 2 positions are the same node"""
            if type(p) == type(self) and (p._node == self._node):
                return True
            else:
                return False

        def __ne__(self, p):
            if self._node == p._node:
                return False
            else:
                return True

    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        """checks to see if Linked Binary Tree is right container
        that p is a position object and that it is not deprecated"""

        if not isinstance(p, self.Position):
            return TypeError("position is not a position object")
        if p._container is not self:
            return TypeError("Container isnt right container for position")
        if p._node._parent == p._node:
            return ValueError("p has been deleted")      # p has been deleted and points at itself
        return p._node

    def __len__(self):
        """"number of elements in tree"""
        return self._size

    def _makePosition(self, node):
        """returns position object for the node being pointed too"""
        if node is not None:    # if node is none list is empty
            return self.Position(self, node)
        else:
            print("Position could not be made since Node was empty")
            return None

    def root(self):
        """returns positon of root, if empty returns none"""
        return self._makePosition(self._root)

    def parent(self, p):
        """returns parent position of """
        node = self._validate(p)
        return self._makePosition(node._parent)

    def left(self, p):
        """returns left child position of current node p"""
        node = self._validate(p)
        return self._makePosition(node._left)   # returns left node

    def right(self, p):
        """returns right child position of current position p"""
        node = self._validate(p)
        return self._makePosition(node._right)

    def num_children(self, p):
        node = self._validate(p)
        numChildern = 0
        if node._left != None:
            numChildern += 1
        if node._right != None:
            numChildern += 1
        return numChildern

    def add_root(self, e):
        if self._root != None:
            raise ValueError("Already root for tree")
        else:
            self._size = 1
            self._root = self._Node(e)  # keep parent right, and left all still equal to none
            return self._makePosition(self._root)

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left != None:
            raise ValueError("Left Child already exists")
        else:
            new = self._Node(e, node)
            self._size += 1
            node._left = new
            return self._makePosition(new)

    def addRight(self, p, e):
        node = self._validate(p)
        if node._right != None:
            raise ValueError("Right Child already exists")
        else:
            new = self._Node(e, node)
            self._size += 1
            node._right = new
            return self._makePosition(new)

    def _replace(self, p , e):
        node = self._validate(p)
        oldElement = node._element
        node._element = e
        return oldElement

    def _delete(self, p):
        """Deletes current position and makes child point to ancestor
            and makes ancestor point to decendant"""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Cannot delete a node with 2 children")
        else:
            if node._left != None:
                child = node._left
            else:
                child = node._right
            if node == self._root:
                self._root = child
            child._parent = node._parent    # sets to none if node was root
            parent = child._parent
            if node == parent._left:
                parent._left = child
            else:
                parent._right = child
            self._size -= 1
            node._parent = node     # node just points at it self
            node._left = None
            node._right = None
            element = node._element
            return element

    def depth(self, p):
        """gives depth of position p"""
        node = self._validate(p)

        if node._parent == None:
            return 0
        else:
            return 1 + self.depth(self._makePosition(node._parent))

    def is_leaf(self, p):
        if self.num_children(p) == 0:
            return True
        else:
            return False

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))

    def breadthFirstTransversal(self):
        """go through each depth of the tree, starting at the root, then next the leftmost child
        of the root, and going left to right in each depth, not recursive"""
        #   use queue to implement this
        #   if we used Linkedstack it would return position in right to left format
        if not self.is_empty():
            que = SingleLinkedQueue()
            que.enqueue(self.root())
            while not que.is_empty():
                p = que.dequeue()
                yield p
                for c in self.children(p):
                    que.enqueue(c)

    def inorderTransversal(self):
        """meant strictly for binary trees, viewed as left to right, for every position p it visits all left
        nodes first then p then the rightmost nodes, used in search trees since it can make sure elements
        are increasing in a left to right manner"""
        for p in self._subtreeInorder(self.root()):
            yield p

    def _subtreeInorder(self, p):
        if self.left(p) is not None:
            for left in self._subtreeInorder(self.left(p)):
                yield left
        yield p
        if self.right(p) is not None:
            for right in self._subtreeInorder(self.right(p)):
                yield right

        # remember that if the the fuction that creates a generator ends without returning a yield a stop iteration
        # exception occurs which will stop the for loop
        # thats how these nested generators operate in the inorder transversal
        # the local variables are stored by the generators which makes it possible
