# python implementation of a BST
from typing import Union


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f"Node({self.val})"

class BST:
    def __init__(self, root: Node=None) -> None:
        self.root = self.normalize_input(root)

    def normalize_input(self, node: Union[Node, int, float]) -> Node:
        # convert to a node, if needed
        # this supports inserting/initializing BST with a .insert(3) OR .insert(Node(3))
        if node is None: return None
        TYPES = [float, int]
        if type(node) is not Node:
            assert type(node) in TYPES # only support numeric types
            return Node(node)
        elif type(node) is Node:
            assert type(node.val) in TYPES # only support numeric types
            return node
        raise TypeError("Unsupported type. Nodes must contain a numeric type (float or int)")

    def print_inorder(self) -> None:
        if self.root is not None:
            if self.root.left is not None:
                BST(self.root.left).print_inorder()
            print(self.root.val)
            if self.root.right is not None:
                BST(self.root.right).print_inorder()

    def print_postorder(self) -> None:
        if self.root is not None:
            if self.root.left is not None:
                BST(self.root.left).print_inorder()
            if self.root.right is not None:
                BST(self.root.right).print_inorder()
            print(self.root.val)

    def get_min(self) -> Node:
        while(self.root.left) is not None:
            return BST(self.root.left).get_min()
        
        return self.root


    def insert(self, node: Union[Node, int, float]) -> 'BST':
        node = self.normalize_input(node)

        if self.root is None:
            self.root = node
        else:
            if node.val <= self.root.val:
                # node should insert to the left of root
                if self.root.left is None:
                    # root doesn't have a left yet, insert here
                    self.root.left = node
                else:
                    # root has a left. Recurse on root.left
                    BST(self.root.left).insert(node)
            else:
                # node should insert to the right of root
                if self.root.right is None:
                    # root doesn't have a right yet, insert here
                    self.root.right = node
                else:
                    # root has a right. Recurse on root.right
                    BST(self.root.right).insert(node)
        
        return self

    def delete(self, node: Union[Node, int, float]) -> 'BST':
        node = self.normalize_input(node)
        # root case
        if self.root.val == node.val:
            if self.root.left is None and self.root.right is None:
                self.root = None
                return self
            if self.root.left and not self.root.right:
                # left child becomes root
                self.root = self.root.left
                return self
            if self.root.right and not self.root.left:
                # right child becomes root
                self.root = self.root.right
                return self
            # root has two subtrees
            # replace root with min value of right subtree
            min_val = BST(self.root.right).get_min()
            self.root.val = min_val.val
            self.root.right = BST(self.root.right).delete(min_val).root

        # non-root case
        return self._delete(node)
    
    def _delete(self, node: Node) -> 'BST':
        # base case, if we call on a leaf.right/left
        if self.root is None: return BST()
        
        if node.val < self.root.val:
            # val to delete lives in the left subtree
            new_left = BST(self.root.left)._delete(node)
            self.root.left = new_left.root if new_left else None
        elif node.val > self.root.val:
            # val to delete lives in the right subtree
            new_right = BST(self.root.right)._delete(node)
            self.root.right = new_right.root if new_right else None
        else:
            # this is the value to delete
            # first case: no children..
            if not self.root.left and not self.root.right:
                return None
            # second case: only has a right child
            if self.root.right and not self.root.left:
                # right child becomes root
                return BST(self.root.right)
            elif self.root.left and not self.root.right:
                # left child becomes root
                return BST(self.root.left)
            
            # second case: only 
        
        return self

if __name__ == "__main__":
    import random
    l = random.sample(range(-10000, 10000), 20)
    bst = BST(l[len(l) // 2])
    for x in l:
        bst.insert(x)

    bst.print_postorder()


# tests
# bst = BST(50)

# bst.insert(13)
# bst.insert(30)
# bst.insert(29)
# bst.insert(100)
# bst.insert(51)
# bst.insert(-3)
# print(f"root: {bst.root}")
# bst.print_inorder()

# # try delete
# bst.delete(50)
# print("deleted 50")
# print(f"new root: {bst.root}")
# bst.print_inorder()


# bst.delete(100)
# print("deleted 100")
# print(f"new root: {bst.root}")
# bst.print_inorder()


# bst.delete(29)
# print("deleted 29")
# print(f"new root: {bst.root}")
# bst.print_inorder()

# bst.delete(51)
# print("deleted 51")
# print(f"new root: {bst.root}")
# bst.print_inorder()


# bst.delete(13)
# print("deleted 13")
# print(f"new root: {bst.root}")
# bst.print_inorder()

# bst.delete(30)
# print("deleted 30")
# print(f"new root: {bst.root}")
# bst.print_inorder()

# bst.delete(-3)
# print("deleted -3")
# print(f"new root: {bst.root}")
# bst.print_inorder()