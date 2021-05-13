#!/usr/bin/env python
# 1. given a tree with a root node, count the # of nodes in the tree. Define my own data structure.

class Node:
    def __init__(self):
        self.children = [] # these are Node objs
    
    @property
    def count(self):
        count = 1
        for child in self.children:
            count += child.count
        return count
    
    def add_child(self, child_node):
        self.children.append(child_node)
    

# create a parent, with no children. count returns 1
parent = Node()
assert parent.count == 1
print(parent.count) # expect 1


# create 1 child with no children.
child = Node()
parent.add_child(child)
assert parent.count == 2
print(parent.count) 

# create a 2nd child node with grandchild
child_two = Node()
grandchild = Node()
child_two.add_child(grandchild)
parent.add_child(child_two)
assert parent.count == 4
print(parent.count)


