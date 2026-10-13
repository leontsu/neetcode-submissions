# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        stack = [[root, root.val]]

        while stack:
            node, prevMax = stack.pop()
            if node:
                if node.val >= prevMax:
                    res += 1

                stack.append([node.right, max(node.val,prevMax)])
                stack.append([node.left, max(node.val,prevMax)])
        return res

