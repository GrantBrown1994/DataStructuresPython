from collections.abc import MutableMapping

# so the mapping class is all non mutating methods of dict class
# and the mutable mapping includes the mutating methods also
# the reason you cannot directly import dict is that it is
# implemented using C and you cannot override methods since they are independent of
# each other and implemented using different programming languages


class MapBase(MutableMapping):

    class _Item:

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, k):
            """checks to see if two keys are the same"""
            return self._key == k._key

        def __ne__(self, k):
            if self._key != k._key:
                return True
            else:
                return False

        def __lt__(self, k):
            """checks to see if key is higher order then current objects key"""
            return self._key < k._key

