#binary tree post order trasversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

print("Binary Tree Postorder Traversal")

root_val = int(input("Enter root value: "))
root = Node(root_val)

left_val = input("Enter left child of root (or -1 for no child): ")
if left_val != "-1":
    root.left = Node(int(left_val))

right_val = input("Enter right child of root (or -1 for no child): ")
if right_val != "-1":
    root.right = Node(int(right_val))


print("Postorder Traversal:", end=" ")
postorder(root)
