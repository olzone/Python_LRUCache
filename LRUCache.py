from  DoublyLinkedList import DoublyLinkedList


class LRUCache:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__doublyLinkedList = DoublyLinkedList()
        self.__nodeMap = dict()

    def get(self, key):
        node = None

        if key in self.__nodeMap:
            node = self.__nodeMap.get(key)
            self.__doublyLinkedList.moveNodeToHead(node)
        else:
            if(self.__doublyLinkedList.getSize() >= self.__capacity):
                del self.__nodeMap[self.__doublyLinkedList.getTail().getData()]
                self.__doublyLinkedList.removeTail()
            node = self.__doublyLinkedList.addDataToList(key)
            self.__nodeMap[key] = node

        return node

    def getCacheState(self):
        return self.__doublyLinkedList.toList()