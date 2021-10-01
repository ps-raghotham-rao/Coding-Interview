
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self):
        a=TreeNode(2,None,None)
        b=TreeNode(3,None,None)
        root=TreeNode(3,a,b)

        print(root.left.val)
        print(root.right.val)

    

print(Solution().diameterOfBinaryTree())