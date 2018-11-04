# -*- coding:utf-8 -*-
__date__ = '2018/11/4 13:21'

class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext


    def __repr__(self):
        return str(self.data)

class Chain(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def append(self, dataOrNode):
        item = None

        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next

            node._next = item
            self.length += 1

    def __repr__(self):
        _str = ""
        node = self.head
        while node != None:
            value = node.data
            _str += "{},".format(value)
            node = node._next
        return _str.rstrip(",")





if __name__ == "__main__":
    n1 = Node(0)
    chain = Chain()
    chain.append(n1)
    print(chain)

    n1 = Node(1)
    chain.append(n1)
    print(chain)