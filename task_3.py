"""
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
 Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def find_max_value(root):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right
    return current.val

def find_min_value(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.val

def sum_tree_values(root):
    if root is None:
        return 0
    return root.val + sum_tree_values(root.left) + sum_tree_values(root.right)


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 1)
root = insert(root, 8)


total_sum = sum_tree_values(root)
print(f"Сума всіх значень у дереві: {total_sum}")
