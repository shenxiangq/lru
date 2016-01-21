#!/usr/bin/env python
# encoding=utf-8
import heapq, itertools

class LFUCache(object):
    REMOVED = object()

    def __init__(self, capacity=16):
        self.capacity = capacity
        self.entry_map = {}
        self.pq = []
        self.counter = itertools.count()

    def set(self, key, value):
        if key in self.entry_map:
            entry = self.entry_map[key]
            entry[1] = self.REMOVED
            new_entry = [entry[0]+1, key, value]
            self.entry_map[key] = new_entry
            heapq.heappush(self.pq, new_entry)
        else:
            if len(self.entry_map) >= self.capacity:
                while(self.pq):
                    _, akey, value = heapq.heappop(self.pq)
                    if akey is not self.REMOVED:
                        del self.entry_map[akey]
                        removed_key = akey

            entry = [1, key, value]
            heapq.heappush(self.pq, entry)
            self.entry_map[key] = entry

    def get(self, key):
        if key in self.entry_map:
            entry = self.entry_map[key]
            entry[1] = self.REMOVED
            new_entry = [entry[0]+1, key, entry[-1]]
            self.entry_map[key] = new_entry
            heapq.heappush(self.pq, new_entry)
            value = entry[-1]
        else:
            value = None
        return value


