class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def printTree(self, level = 0):
        print(" " * (level + 4) + str(self.data))
        for child in self.children:
            child.printTree(level + 3)


# example use.
rootNode = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
child1_1 = Node("Child 1.1")
child1_2 = Node("Child 1.2")
child2_1 = Node("Child 2.1")
child2_2 = Node("Child 2.2")

rootNode.addChild(child1)
rootNode.addChild(child2)
child1.addChild(child1_1)
child1.addChild(child1_2)
child2.addChild(child2_1)
child2.addChild(child2_2)

rootNode.printTree()
