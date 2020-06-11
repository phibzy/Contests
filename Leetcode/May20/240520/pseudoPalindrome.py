#!/usr/bin/python3

import logging
import pdb

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Space Complexity: O(D) - Where D is the maximum depth of the tree
# Time Complexity:  O(N + W) - Where N is number of nodes and W is max width of the tree
                              # You have to visit N nodes regardless, but W comparisons are made depending on how many root->leaf paths there are
                              # If perfectly imbalanced W then only one path, perfectly balanced then many paths  
class Solution:
    def pseudoPalindromicPaths (self, root):
        if not root: return 0
        
        digits = [ 0 for _ in range(11) ]

        # Use 0 in digits as return value
        self.rPalPath(root, 1, digits)
        
        return digits[0]
    
    def rPalPath(self, node, length, digits):
        if not node: return 0
      
        digits[node.val] += 1
        
        # If leaf node, do calculation
        if (not node.left) and (not node.right):
            if self.checkPath(digits): digits[0] += 1 
            digits[node.val] -= 1
            return
                
        self.rPalPath(node.left, length+1, digits)
        self.rPalPath(node.right, length+1, digits)

        digits[node.val] -= 1
    
    def checkPath(self, digits):
        oddCount = 0

        for i in range(1,10):
            if digits[i] % 2 == 1: oddCount += 1

          
        return oddCount <= 1   
