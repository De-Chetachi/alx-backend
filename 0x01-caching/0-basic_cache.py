#!/usr/bin/env python3
'''base caching'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''a basic cache class that inherits from BaseCaching
    BaseCaching implements a cache class
    with a max-itmes and cache_data field
    methods like print cache, get to retrieve a cacheitem based on key
    a put method to add data to the cache_data'''
