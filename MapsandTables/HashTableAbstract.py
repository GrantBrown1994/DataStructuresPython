from MapBase import MapBase
import random as r

class HashTableAbstract(MapBase):

    # will be using the MAD method for the compression function and using pythons built
    # in hash code function, will use just immutable data types of specific key objects

    def __init__(self, p, capacity):
        # p should be a prime number larger than capacity of bucket array
        self._hashtable = [None] * capacity
        self._p = p
        self._n = 0     # number of items in hash table
        # will be using MAD = [(a*hash*(k) + b) mod p] mod capacity
        self._a = r.randrange(p-1) + 1
        self._b = r.randrange(p-1)

    def  _hashfunction(self, k):

        h = (((hash(k)*self._a) + self._b) % self._p) % len(self._hashtable)
        return h

    def _bucket_getitem(self, hf, key):
        raise NotImplementedError("Need to implement Collision Handling Scheme")

    def _bucket_setitem(self, hf, key, value):
        raise NotImplementedError("Need to implement Collision Handling Scheme")

    def _bucket_delitem(self, hf, key):
        raise NotImplementedError("Need to implement Collision Handling Scheme")

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        """can be done using seperate chaining in which we have to make an
            auxilary data structure, a map(which is just a list with non numeric index's), to
            chain collisions, or we can use open addressing techniques,
             linear probing, or double hashing (not gonna do quadratic)"""

        hashkey = self._hashfunction(key)
        return self._bucket_getitem(hashkey, key)

    def __setitem__(self, key, value):
        hashkey = self._hashfunction(key)
        self._bucket_setitem(hashkey, key, value)
        # want to keep load factor below 0.6
        # load factor is n/N where n is number of items in map
        # and N is the length of the table
        if self._n > len(self._hashtable) // 2:
            # by subtracting by one we are keeping the number prime which
            # helps in keeping the hash function uniform
            self._resize(2 * (len(self._hashtable) - 1))

    def __delitem__(self, key):
        hashkey = self._hashfunction(key)
        self._bucket_deleteitem(hashkey, key)
        self._n -= 1

    def _resize(self, newcapacity):
        oldlist = list(self.items())    # since it inherets the mapping class we can use this method
        self._hashtable = newcapacity * [None]
        self._n = 0
        for (key, value) in oldlist:
            self[key] = value

    def hashcodes(self, s):
        mask = (1 << 32) - 1
        h = 0
        for c in s:
            h = (h << 5 & mask) | (h >> 27)
            h += ord(c)
        return h


