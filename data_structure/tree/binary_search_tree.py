class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, node):
        self.root = node

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def deleteNode(self, data):

        # Base Case
        parent_node = None;
        current_node = self.root;
        if data == self.root.data:
            pass
        else:
            while current_node is not None and data != current_node.data:
                parent_node = current_node
                if data < parent_node.data:
                    current_node = current_node.left
                elif data > parent_node.data:
                    current_node = current_node.right
                else:
                    break

        # at this time we have current_node, which is the node need to be deleted

        # case 1 current node is leaf
        if current_node.left is None and current_node.right is None:
            if parent_node.left is not None and parent_node.left.data == current_node.data:
                parent_node.left = None
            else:
                parent_node.right = None
            return
        # case 2: current node have 1 child
        elif current_node.left is None or current_node.right is None:
            if parent_node.left is not None and parent_node.left.data == current_node.data:
                if current_node.left is not None:
                    parent_node.left = current_node.left
                else:
                    parent_node.left = current_node.right
            else:
                if current_node.left is not None:
                    parent_node.right = current_node.left
                else:
                    parent_node.right = current_node.right
            return

        # case 3: node have 2 child
        temp = self.minValueNode(current_node.right)
        # temp = self.maxValueNode(current_node.left)
        current_node.data = temp.data;

        new_data = temp.data
        parent_node = current_node
        current_node = current_node.right
        while current_node.data != new_data:
            parent_node = current_node
            current_node = current_node.left

        parent_node.left = current_node.right

        return



        # if root is None:
        #     return root
        #
        # # If the key to be deleted
        # # is smaller than the root's
        # # key then it lies in  left subtree
        # if key < root.key:
        #     root.left = deleteNode(root.left, key)
        #
        # # If the kye to be delete
        # # is greater than the root's key
        # # then it lies in right subtree
        # elif (key > root.key):
        #     root.right = deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        # else:
        #
        #     # Node with only one child or no child
        #     if root.left is None:
        #         temp = root.right
        #         root = None
        #         return temp
        #
        #     elif root.right is None:
        #         temp = root.left
        #         root = None
        #         return temp
        #
        #     # Node with two children:
        #     # Get the inorder successor
        #     # (smallest in the right subtree)
        #     temp = minValueNode(root.right)
        #
        #     # Copy the inorder successor's
        #     # content to this node
        #     root.key = temp.key
        #
        #     # Delete the inorder successor
        #     root.right = deleteNode(root.right, temp.key)
        #
        # return root

if __name__ == '__main__':

    node44 = Node(44)
    node17 = Node(17)
    node88 = Node(88)

    node32 = Node(32)
    node28 = Node(28)
    node29 = Node(29)

    node44.left = node17
    node44.right = node88

    node17.right = node32
    node32.left = node28
    node28.right = node29

    node65 = Node(65)
    node97 = Node(97)

    node88.left = node65
    node88.right = node97

    node54 = Node(54)
    node82 = Node(82)
    node65.left = node54
    node65.right = node82

    node76 = Node(76)
    node80 = Node(80)
    node78 = Node(78)

    node82.left = node76
    node76.right = node80
    node80.left = node78


    binarySearchTree = BinarySearchTree(node44)
    binarySearchTree.deleteNode(32)
    binarySearchTree.deleteNode(65)

    print(node44)

