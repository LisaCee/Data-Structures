from doubly_linked_list import DoublyLinkedList, ListNode
import sys
sys.path.append('../doubly_linked_list')


class KeyValNode(ListNode):
    def __init__(self, value, key):
        self.value = value
        self.prev = None
        self.next = None
        self.key = key


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.head = None
        self.tail = None
        self.limit = limit
        self.size = 0
        self.storage = {}
        # fast lookup
        self.cache = DoublyLinkedList()
        # fast removal

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # def maxCapacity(self):
    #     savedPrev = self.prev
    #     savedNext = self.next

    #     savedPrev.next = savedNext
    #     savedNext.prev = savedPrev

    # def recentlyAccessed(self, value):
    #     self.prev = self.head
    #     self.next = self.head.next

    #     self.head.next.prev = value
    #     self.head.next = value

    def get(self, key):
        if key in self.storage:
            # keep in cache
            # move to front of ll
            pass
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # get to see if key exists in cache
            # update value
            # move to head of ll

        # if doesn't exist, add to cache
        # add to head of ll
        # check limit
            # remove tail if needed

        # new_node = KeyValNode(key, value)
        # if self.head is None and self.tail is None:
        #     self.head = new_node
        #     self.tail = new_node
        pass
