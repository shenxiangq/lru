#!/usr/bin/env python
# encoding=utf-8
from collections import OrderedDict

class LRUCache(object):
    '''
    This is based on the idea of LinkedHashMap.
    This class implements a doubly linked list.
    The list is ordered by the access order, ie the least recently used item is
    in the last node, the first node is the to_remove node.
    '''
    class LinkedNode(object):
        __slots__ = ['key', 'value', 'prev', 'next']

        def __init__(self, key, value, prev, next):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity=16):
        self.capacity = capacity
        self.node_map = {}
        self._head_node = self.LinkedNode(None, None, None, None)
        self._tail_node = self.LinkedNode(None, None, None, None)
        self._head_node.next = self._tail_node
        self._tail_node.prev = self._head_node

    def get(self, key):
        if key not in self.node_map:
            return None
        else:
            node = self.node_map[key]
            self._move_to_tail(node)
            return node.value

    def set(self, key, value):
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._move_to_tail(node)
        else:
            if len(self.node_map) >= self.capacity:
                # remove the first node
                to_remove = self._head_node.next
                self.node_map.pop(to_remove.key)
                self._head_node.next = to_remove.next
                to_remove.next.prev = self._head_node

            node = self.LinkedNode(key, value, self._tail_node.prev, self._tail_node)
            self._tail_node.prev.next = node
            self._tail_node.prev = node
            self.node_map[key] = node

    def _move_to_tail(self, node):
        # if this node is the last node, no need to move.
        if node is self._tail_node.prev:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self._tail_node.prev.next = node
        node.prev = self._tail_node.prev
        node.next = self._tail_node
        self._tail_node.prev = node

class LRUCacheOrdered(object):
    '''不能存储可变类型对象，不能并发访问set()'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self,key):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None

        return value

    def set(self,key,value):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last = False)    #pop出第一个item
            self.cache[key] = value

