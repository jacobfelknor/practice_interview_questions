from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            left_child = root.left
            right_child = root.right
            root.left = right_child
            root.right = left_child
            if root.left is not None:
                self.invertTree(root.left)
            if root.right is not None:
                self.invertTree(root.right)
        
        return root