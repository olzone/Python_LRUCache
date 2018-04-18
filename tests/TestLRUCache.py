import unittest

from LRUCache import LRUCache


class TestStringMethods(unittest.TestCase):

    def test_promoteFromHead(self):
        lru = LRUCache(3)

        for d in ['A', 'B', 'C', 'A']:
            lru.get(d)

        self.assertEqual(lru.getCacheState(), ['A', 'C', 'B'])

    def test_promoteInide(self):
        lru = LRUCache(3)

        for d in ['A', 'B', 'C', 'B']:
            lru.get(d)

        self.assertEqual(lru.getCacheState(), ['B', 'C', 'A'])

    def test_promoteFromTail(self):
        lru = LRUCache(3)

        for d in ['A', 'B', 'C', 'C']:
            lru.get(d)

        self.assertEqual(lru.getCacheState(), ['C', 'B', 'A'])


    def test_capacity(self):
        lru = LRUCache(3)

        for d in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            lru.get(d)

        self.assertEqual(lru.getCacheState(), ['G', 'F', 'E'])

if __name__ == '__main__':
    unittest.main()