from Node import Node

root = Node()
root.generateChildren("X", "O", True)
# print(root)
print(root.getMaxGrid())
