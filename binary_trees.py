class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __repr__(self):
        """Return detailed information to developers for debugging."""
        left = f"Left({self.left_child.data})" if self.left_child else "Left(None)"
        right = f"Right({self.right_child.data})" if self.right_child else "Right(None)"
        return f"TreeNode(data={self.data}, {left}, {right})"


    def create_left_child(self, data):
        """createt the left child of the node."""
        self.left_child = TreeNode(data)
        return self.left_child
    
    def create_right_child(self, data):
        """Creates a the right child of the node"""
        self.right_child = TreeNode(data)
        return self.right_child
    
    def display_tree(self, level=0, prefix="Root: "):
        """Outputs a representation of the tree in hierarchical formate"""
        print(" " * level * 4 + prefix + str(self.data))
        if self.left_child:
            self.left_child.display_tree(level + 1, "L--> ")
        if self.right_child:
            self.right_child.display_tree(level + 1, "R--> ")   
    
    # Tree traversal
    # inorder tree traversal
    def inorder_traversal(self):
        """Visits the Left ----> Root ----> Right trees in the given order.
        
        Step1: Recursively traverse the left subtree.
        Step2: Visit root node.
        Step3: Recursively travese right subtree."""
        if self.left_child:
            self.left_child.inorder_traversal()
        print(self.data, end="->")
        if self.right_child:
            self.right_child.inorder_traversal()
            

tree  = TreeNode("Root")
# level 1
child1 = tree.create_left_child(20)
child2 = tree.create_right_child(30)

# level 2
child1_1 = child1.create_left_child(50)
child1_2 = child1.create_right_child(60)

child2_1 = child2.create_left_child(100)
child2_2 = child2.create_right_child(200)

tree.inorder_traversal()