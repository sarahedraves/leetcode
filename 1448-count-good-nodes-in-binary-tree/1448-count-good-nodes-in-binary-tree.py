# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.recursive(root, root.val)
    
    def recursive(self, node, pathmax):
        if node is None:
            return 0
        isgood=int(node.val>=pathmax)
        if node.left is None and node.right is None:
            return isgood
        elif node.left is None:
            return self.recursive(node.right,max(pathmax,node.val))+isgood
        elif node.right is None:
            return self.recursive(node.left,max(pathmax,node.val))+isgood
        else:
            return self.recursive(node.right,max(pathmax,node.val))+self.recursive(node.left,max(pathmax,node.val))+isgood