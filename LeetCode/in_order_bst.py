from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.in_order = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(self, node):
            if node:
                traverse(self, node.left)
                self.in_order.append(node.val)
                traverse(self, node.right)
        traverse(self, root)
        return self.in_order