
class TreeNode:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

def travel_inorder(root):
    if root != None:
        travel_inorder(root.left)
        print(root.info)
        travel_inorder(root.right)

def travel_preorder(root):
    if root != None:
        print(root.info)
        travel_preorder(root.left)
        travel_preorder(root.right)

def travel_postorder(root):
    if root != None:
        travel_postorder(root.left)
        travel_postorder(root.right)
        print(root.info)

def setup_tree():
    tree_node_a = TreeNode("A")
    tree_node_b = TreeNode("B")
    tree_node_c = TreeNode("C")
    tree_node_d = TreeNode("D")
    tree_node_e = TreeNode("E")
    tree_node_f = TreeNode("F")
    tree_node_g = TreeNode("G")
    tree_node_h = TreeNode("H")
    tree_node_i = TreeNode("I")
    tree_node_j = TreeNode("J")

    tree_node_a.left = tree_node_b
    tree_node_a.right = tree_node_c

    tree_node_b.left = tree_node_d
    tree_node_b.right = tree_node_e

    tree_node_d.left = tree_node_h
    tree_node_d.right = tree_node_i

    tree_node_e.left = tree_node_j

    tree_node_c.left = tree_node_f
    tree_node_c.right = tree_node_g

    return tree_node_a

if __name__ == '__main__':
    tree_node_a = setup_tree()
    # PRINT OUT INORDER TRAVEL
    # travel_inorder(tree_node_a)

    # PRINT OUT PREORDER TRAVEL
    # travel_preorder(tree_node_a)

    # PRINT OUT POSTORDER TRAVEL
    travel_postorder(tree_node_a)



