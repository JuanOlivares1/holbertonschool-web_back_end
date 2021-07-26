#!/usr/bin/env python3
""" Module - Define LRU cache replacement algorithm """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache replacement system """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.ref = 0

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)[0]))

    def put(self, key, item):
        """ Inserts new data to cache """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = (item, self.ref)
                self.ref += 1
            else:
                if len(self.cache_data.keys()) < self.MAX_ITEMS:
                    self.cache_data[key] = (item, self.ref)
                    self.ref += 1
                elif len(self.cache_data.keys()) == self.MAX_ITEMS:
                    lr = -1
                    for k, v in self.cache_data.items():
                        if lr != -1:
                            if lr > v[1]:
                                lr = v[1]
                                lru = k
                        else:
                            lr = v[1]
                            lru = k
                    print("DISCARD: {}".format(lru))
                    self.cache_data.pop(lru)
                    self.cache_data[key] = (item, self.ref)
                    self.ref += 1

    def get(self, key):
        """ Retrive data from cache """
        if key and key in self.cache_data.keys():
            self.cache_data[key] = (self.cache_data[key][0], self.ref)
            self.ref += 1
            return self.cache_data[key][0]
        else:
            return None
