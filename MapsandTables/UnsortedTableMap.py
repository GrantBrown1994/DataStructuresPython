from MapBase import MapBase

# this class will include mutating methods of the MutableMappings class

# since each of these methods are implemented using for loops they can possibly run O(n)
# if you want to be more exact its O(k +1) with k being the index of the item we want to find


class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []    # creates an empty list that will store objects with key and values

    def __getitem__(self, item):
        for i in self._table:   # returns iterator object
            if item == i._key:
                return i._value
        raise KeyError("Key {0} is not in map".format(i._key))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))    # adds object to list that stores a key and a value
                                                # makes this list a map now

    def __delitem__(self, k):
        for i in range(len(self._table)):
            if k == self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError("Key {0} is not in Map".format(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

    # when function ends it raises StopIteration error which is caught by for loop and ends the for loop
