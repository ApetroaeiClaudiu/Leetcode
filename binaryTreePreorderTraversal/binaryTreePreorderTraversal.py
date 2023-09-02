# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if root is None:
            return

        nodeStack = []
        nodeStack.append(root)

        while len(nodeStack) > 0:
            node = nodeStack.pop()
            result.append(node.val)
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)
        
        return result
