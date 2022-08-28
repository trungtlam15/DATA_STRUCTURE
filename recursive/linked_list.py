class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def find(self,str):
        while (self.headval != None):
            if str == self.headval.dataval:
                return True
            self.headval = self.headval.nextval;
        return False

    def find_recursive(self,str):
        if self.headval == None:
            return False
        if str == self.headval.dataval:
            return True
        self.headval = self.headval.nextval;
        return self.find_recursive(str)


if __name__ == '__main__':
    list1 = SLinkedList()
    list1.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    list1.headval.nextval = e2
    e2.nextval = e3

    # result = list1.find("Fri")
    # print(result)

    result = list1.find_recursive("Fri")
    print(result)
