from HashTableAbstract import HashTableAbstract
from UnsortedTableMap import UnsortedTableMap


class SeperateChainHashMap(HashTableAbstract):

    def _bucket_getitem(self, hf, key):
        """access list with hash function, and then"""
        bucket = self._hashtable[hf]
        if bucket is not None:  # if bucket is not empty then we will grab item, if it is return hf key error
            return bucket[key]
        else:
            raise KeyError("HashFunction key: {0} is not in current map".format(hf))

    def _bucket_setitem(self, hf, key, value):
        # self._table[hf] allows us to access list or table value with the hash function index
        # that is calculated from the compression function that maps it to a range from 0 to N-1
        # and the [key] part allows us to access the __getItem__ method of the UnsortedTableMap
        # since we did not inherit it it does not try to use HashTableAbstract's __getitem__ method
        if self._hashtable[hf] is None:     # uses map __getitem__ to find item
            self._hashtable[hf] = UnsortedTableMap()
        oldsize = len(self._hashtable[hf])
        self._hashtable[hf][key] = value
        if len(self._hashtable[hf]) > oldsize:      # if we did not override previous key value
            self._n += 1

    def iteratorKey(self):
        """gives us keys for table"""
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item._key

    def iteratorValue(self):
        """gives us values of the buckets"""
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item._value

    def __iter__(self):
        """returns item objects of the map with its key and value"""
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item


if __name__ == "__main__":
    ChainMap = SeperateChainHashMap(11, 3)
#     a = ChainMap.hashcodes("sadfadsfasfdasdfasdfasdfasdfasdfasdfasfasfasfasfasdfasdfasdfdsf")
    ChainMap["hello"] = "test"
