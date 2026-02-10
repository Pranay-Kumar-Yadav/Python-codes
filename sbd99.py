#binary tree pre order trasversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


print("Binary Tree Preorder Traversal")

# ---- input in the middle ----
root_val = int(input("Enter root value: "))
root = Node(root_val)

left_val = input("Enter left child of root (or -1 for no child): ")
if left_val != "-1":
    root.left = Node(int(left_val))

right_val = input("Enter right child of root (or -1 for no child): ")
if right_val != "-1":
    root.right = Node(int(right_val))

# ---- traversal ----
print("Preorder Traversal:", end=" ")
preorder(root)
