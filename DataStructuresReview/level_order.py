from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


def levelOrder(root: Optional[TreeNode]) -> List[int]:
    q = []
    level_order = []
    q.append(root)
    while len(q) > 0:
        current = q.pop(0)
        level_order.append(current)
        if current.right is not None:
            q.append(current.right)
        if current.left is not None:
            q.append(current.left)

    return level_order


def levelOrderList(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []
    current_level = []
    next_level = []
    this_level_values = []
    ans = []
    current_level.append(root)
    while len(next_level) > 0 or len(current_level) > 0:
        if len(current_level) > 0:
            current = current_level.pop(0)
            this_level_values.append(current.val)
            if current.right is not None:
                next_level.append(current.right)
            if current.left is not None:
                next_level.append(current.left)
        else:
            current_level = next_level
            next_level = []
            ans.append(this_level_values)
            this_level_values = []

    # add final level
    if this_level_values:
        ans.append(this_level_values)

    return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(levelOrderList(root))
