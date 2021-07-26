#!/usr/bin/env python3
""" Module - Define LIFO cache replacement algorithm """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache replacement system """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Inserts new data to cache """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.stack.append(key)
            else:
                if len(self.cache_data.keys()) < self.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.stack.append(key)
                elif len(self.cache_data.keys()) == self.MAX_ITEMS:
                    k = self.stack.pop(-1)
                    self.cache_data.pop(k)
                    print("DISCARD: {}".format(k))
                    self.cache_data[key] = item
                    self.stack.append(key)

    def get(self, key):
        """ Retrive data from cache """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
