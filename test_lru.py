#!/usr/bin/env python
# encoding=utf-8

from lru import LRUCache, LRUCacheOrdered
from lfu import LFUCache
import time

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.set(1, '1')
    lru.set(2, '2')
    lru.set(3, '3')
    print lru.get(1)

    n = 10**5
    lru = LRUCache(n/2)
    start = time.time()
    for i in xrange(n):
        lru.set(i, None)
    end = time.time()
    print 'total time:%.3f' % (end - start)
    print '%.3f / second' % (n/(end-start))

    start = time.time()
    for i in xrange(n):
        lru.get(i)
    end = time.time()
    print 'total time:%.3f' % (end - start)
    print '%.3f / second' % (n/(end-start))
    a = raw_input()
