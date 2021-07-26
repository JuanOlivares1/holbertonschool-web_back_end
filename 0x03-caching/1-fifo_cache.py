#!/usr/bin/env python3
""" Module - Define FIFO cache replacement algorithm """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache replacement system """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Inserts new data to cache """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            else:
                if len(self.cache_data.keys()) < self.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.queue.append(key)
                elif len(self.cache_data.keys()) == self.MAX_ITEMS:
                    k = self.queue.pop(0)
                    self.cache_data.pop(k)
                    print("DISCARD: {}".format(k))
                    self.cache_data[key] = item
                    self.queue.append(key)
    
    def get(self, key):
        """ Retrive data from cache """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
