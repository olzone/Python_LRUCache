class Node:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def getNext(self):
        return self.__next

    def getPrev(self):
        return self.__prev

    def getData(self):
        return self.__data

    def setNext(self, next):
        self.__next = next

    def setPrev(self, prev):
        self.__prev = prev

    def setData(self, data):
        self.__data = data

    # def __del__(self):
    #     print("deleting", self)