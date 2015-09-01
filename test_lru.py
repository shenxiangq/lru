#!/usr/bin/env python
# encoding=utf-8

from lru import LRUCache

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.set(1, '1')
    lru.set(2, '2')
    lru.set(3, '3')
    print lru.get(1)
