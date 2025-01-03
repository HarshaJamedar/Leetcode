# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        if root is None:
            return result
        def traversal(node):
            if node is None:
                return
            result.append(node.val)
            traversal(node.left)
            traversal(node.right)
            return result
        return traversal(root)

        
        