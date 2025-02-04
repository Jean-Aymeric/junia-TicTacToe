from Node import Node

root = Node()
root.generateChildren("X", "O")
print(root.Grid)
for child in root.Children:
    print(child.Grid)
