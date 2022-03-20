# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        data = set()
        breadthSearch(root, data)
        
        return len(data) <= 1  
        
def breadthSearch(node, data):
    # Add our current node value to our set.
    data.add(node.val)

    #If the set has more than 1 element, return false.
    if len(data) > 1:
        return False

    if node.left:
        breadthSearch(node.left, data)
    if node.right:
        breadthSearch(node.right, data)     
