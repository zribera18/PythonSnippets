class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None


    # 
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next

    # 
    def reverseList(self):
        curr = self.head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    # 
    def findData(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    
    def EthansReverseList(self):
        tmp = None
        curr = self.head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    
    def rotate(self, rotations):
        for i in range(0, rotations):
            curr = self.head
            while curr:
                if curr.next.next == None:
                    temp = curr.next
                    curr.next = None
                    temp.next = self.head
                    self.head = temp
                curr = curr.next

    def deleteLast(self, remove):
        curr = self.head
        prev = None
        prevRemoval = None
        nextRemoval = None
        while curr:
            if curr.data == remove:
                prevRemoval = prev
                nextRemoval = curr.next
            prev = curr
            curr = curr.next
        if prevRemoval:
            prevRemoval.next = nextRemoval

    # 
    def insert(self, data):
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp

    def append(self, data):
        curr = self.head
        if curr == None:
            self.head = Node(data)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def pop(self):
        tmp = self.head.data
        self.head = self.head.next
        return tmp


    # 
    # def push(self, data):
    #     print "Hi"


if __name__ == '__main__':
    list = LinkedList()
    # list.head = Node("hi")
    list.append("hi1")

    list.append("bye")
    list.append("bye again")
    list.append("bye")
    list.insert("first bitch")
    print "popped::" + str(list.pop())
    list.printList()
    print ""
    # list.reverseList()
    list.deleteLast("bye")
    list.printList()

    # print "true false::: " + str(list.findData("hi"))
    # temp = list.head
    # while temp:
    #     print temp.data
    #     temp = temp.next
