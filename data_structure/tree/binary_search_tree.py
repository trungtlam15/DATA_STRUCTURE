
class BinarySearchTree:
    def __init__(self):
        self.node = None

    def insert(self, data):
        node = Node(data)
        parent_node = self.find_parent_node(data)
        if parent_node == None:
            self.node = node
        elif parent_node.data > data :
            parent_node.left = node
        else:
            parent_node.right = node



    def find_parent_node(self, data):
        node = self.node
        while node != None:
            if node.data > data:
                if node.left == None:
                    return node
                node = node.left
            else:
                if node.right == None:
                    return node
                node = node.right
        return node

    def set_up(self):
        number_node = input("number of node")
        for i in range(int(number_node) - 1):
            data = input("enter value at " + str(i) + ": ")
            self.insert(data)


    def delete(self,data):
        pass


    def find_parent_node_V2(self, data):
        parent_note = self.node;
        if self.node.data == data:
            parent_note = None

        while parent_note != None and (parent_note.left != None or parent_note.right != None):
            if self.node.left.data == data or self.node.right.data == data:
                break;
            if data < parent_note.data and parent_note.left != None:
                parent_note = parent_note.left
            elif data > parent_note.data and parent_note.right != None:
                parent_note = parent_note.right

        return parent_note




    def search(self, data):
        current_node = self.node
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.data == data:
                return current_node
            else:
                if current_node.left != None:
                    queue.append(current_node.left)
                if current_node.right != None:
                    queue.append(current_node.right)




class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



if __name__ == '__main__':
    tree = BinarySearchTree()
    # tree.set_up()

    tree.insert(27)
    tree.insert(14)
    tree.insert(35)
    tree.insert(19)
    tree.insert(10)
    tree.insert(43)
    tree.insert(31)

    # print(tree)

    # tree.search(19)
    parent = tree.find_parent_node_V2(19)
    print(parent)