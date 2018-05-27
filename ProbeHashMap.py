from HashTableAbstract import HashTableAbstract

class ProbeHashMap(HashTableAbstract):

    _available = object()       # marker for the cells that were removed and made empty so linear probing still works


    def _isavail(self, hf):
        return  self._hashtable[hf] is None or type(self._hashtable[hf]) == type(ProbeHashMap._available)

    def _findslot(self, hf, key):
        """Looks for slot with hf key and if it finds empty that means linear probing
            was not found and the hf key is not in container"""
        while True:
            if self._hashtable[hf] is None or type(self._hashtable[hf]) == type(ProbeHashMap._available):
                avail = self._hashtable[hf]
                if avail is None:
                    return(False, avail)    # slot searched was empty
            elif key == self._hashtable[hf]._key:
                return(True, hf)
            hf = (hf+1) % len(self._hashtable)


    def _bucket_getitem(self, hf, key):
        found, slot = self._findslot(hf, key)
        if found == True:
            return self._hashtable[slot]._value
        else:
            raise KeyError("Key {0} not in container".format(key))

    def _bucket_setitem(self, hf, key, value):
        found, slot = self._findslot(hf, key)
        if found == True:
            self._hashtable[hf] = value
        else:
            self._hashtable[hf] = self._Item(key, value)
            self._n += 1

    def _bucket_delitem(self, hf, key):
        found, slot = self._findslot(hf, key)
        if found == True:
            self._hashtable[hf] == self._available
            self._n -= 1
        elif found == False:
            raise KeyError("Key {0} not in container".format(key))

    def __iter__(self):
        for hf in range(len(self._hashtable)):
            if self._isavail(hf) == True:
                yield self._hashtable[hf]._key



