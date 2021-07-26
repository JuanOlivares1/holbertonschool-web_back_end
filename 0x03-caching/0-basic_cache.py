#!/usr/bin/env python3
""" Module - Define basic cache class"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Define basic cache - inherits from BaseCaching """

    def put(self, key, item):
        """ Inserts new data to cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrive data from cache """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
