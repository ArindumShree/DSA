# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_(self,node,order):
        if node==None:
            return 
        self.in_(node.left,order)
        order.append(node.val)
        self.in_(node.right,order)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        order=[]
        ans=float('inf')
        self.in_(root,order)
        
        for i in range(1,len(order)):
            ans=min(ans,(abs(order[i]-order[i-1])))
        return ans