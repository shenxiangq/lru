# lru
A LRU cache based on the idea of LinkedHashMap.
This class implements a doubly linked list.
The list is ordered by the access order, ie the least recently used item is 
in the last node, the first node is the to_remove node.
