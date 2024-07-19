# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #iterative method
        res = [] #result array
        stack = [] #list while traversing 
        curr = root # current pointer

        #while pointer or stack are non empty
        while curr or stack:
            while curr:
                stack.append(curr) #appending all the nodes that are left to pointer
                curr = curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res
        #Recursive solution
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return res




        