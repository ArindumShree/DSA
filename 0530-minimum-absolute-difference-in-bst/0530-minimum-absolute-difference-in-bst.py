# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_(self, node):
        if node is None:
            return
        self.in_(node.left)
        if self.prev is not None:
            self.ans = min(self.ans, node.val - self.prev)
        self.prev = node.val
        self.in_(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')
        self.in_(root)

        return self.ans