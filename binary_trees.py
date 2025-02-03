class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def create_node(self, data):
        return TreeNode(data)

    def create_left(self, data):
        self.left = self.create_node(data)
        return self.left
    
    def create_right(self, data):
        self.right = self.create_node(data)
        return self.right

    def display_tree(self, level = 0):
        print(" " * (level + 1) + str(self.data))
        if self.right:
            self.right.display_tree(level + 4)
        if self.left:
            self.left.display_tree(level + 4)

tree = TreeNode("Root")
child1 = tree.create_left("Left child")
child2 = tree.create_right("Right data")

child1.create_right("Hello")
child1. create_left("There")

child2.create_right("Nice to ")
child2.create_left("meet you.")

tree.display_tree()