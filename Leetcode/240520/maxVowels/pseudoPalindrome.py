#!/usr/bin/python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root):
        if root is None: return 0
        
        valList = [0 for _ in range(0, 10)]
        diffVals = 0
        length = 0
        
        result = 0
        
        # iterative DFS solution with stack
        s = list()
        s.append(root)
        
        while s:
            node = s.pop()
            if node is None: continue
            length += 1
        
            if valList[node.val] == 0:
                diffVals += 1
            
            valList[node.val] += 1

            if root.left is None and root.right is None:
                if self.checkPath(valList, diffVals, length): result += 1
                
                # remove val, change diff digits if necessary
                valList[node.val] -= 1
                if valList[node.val] == 0: diffVals -= 1
                length -= 1
            
            else:
                
                s.append(root.left)
                s.append(root.right)
        
        
        return result
    
    def checkPath(self, valList, diffVals, length):
        # floor div of len + 1
        if length == 2:
            return diffVals == 1
        
        if diffVals == 1: return True   
        
        calc = (length + 1) // 2
        
        if not diffVals <= calc:
            return False
        
        # odd lengths have odd diffVals except for 2 case
        if length % 2 == 1 and (diffVals % 2 == 0 and diffVals != 2):
            return False
        
        # even check - all present digits must be in even quantities
        if length % 2 == 0:
            if diffVals == 2:
                pass
                # check equal amounts
            
            else:
                halfLength = length / 2
                for i in range(1, 10):     
                    pass
        
    
               
