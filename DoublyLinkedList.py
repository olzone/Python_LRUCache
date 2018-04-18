from Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getHead(self):
        return self.__head

    def getTail(self):
        return self.__tail

    def getSize(self):
        return self.__size

    def addDataToList(self, data):
        node = Node(data)

        if not self.__head:
            self.__head = node
            self.__tail = node
        else:
            node.setNext(self.__head)
            self.__head.setPrev(node)
            self.__head = node

        self.__size += 1

        return node

    def removeTail(self):
        if not self.__tail:
            raise RuntimeError("List is empty.")

        if self.__tail.getPrev():
            antecedentTail = self.__tail.getPrev()
            antecedentTail.setNext(None)
            del self.__tail
            self.__tail = antecedentTail
        else:
            del self.__tail
            self.__head = None
            self.__tail = None

        self.__size -= 1

    def moveNodeToHead(self, node):
        if node == self.__head:
            return

        if node == self.__tail:
            self.__tail = self.__tail.getPrev()

        prev = node.getPrev()
        next = node.getNext()

        prev.setNext(next)
        if next:
            next.setPrev(prev)

        node.setPrev(None)
        node.setNext(self.__head)
        self.__head.setPrev(node)
        self.__head = node


    def toList(self):
        dataList = []

        current = self.__head
        while(current != None):
            dataList.append(current.getData())
            current = current.getNext()

        return dataList
