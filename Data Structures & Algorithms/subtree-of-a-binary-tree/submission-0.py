# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameSubtree(root, subroot):
            q = deque([root])
            sq = deque([subroot])

            while q:
                node = q.popleft()
                snode = sq.popleft()

                if not node and not snode:
                    continue
                if not node or not snode:
                    return False
                if node.val != snode.val:
                    return False

                q.append(node.left)
                q.append(node.right)
                sq.append(snode.left)
                sq.append(snode.right)

            return True

        q = deque([root])

        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                if isSameSubtree(node, subRoot):
                    return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False