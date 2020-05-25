#!/usr/bin/python3

import logging
import pdb

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root):
        if root is None: return 0
        
        valList = [0 for _ in range(0, 10)]
        length = 0
        
        result = 0
        
        # iterative DFS solution with stack
        s = list()
        s.append(root, valList)

        printStack(s)

        # Go all the way to bottom with loop, pushing on all nodes
        # The same way we did the other problem
        
        while s:
            # pdb.set_trace()
            node = s.pop()
            if node is None: continue

            logging.debug(f"node is {node.val}")

            length += 1
            
            valList[node.val] += 1

            if node.left is None and node.right is None:
                if self.checkPath(valList, length):
                    logging.debug("We have a palindrome")
                    result += 1
                
                # remove val, change diff digits if necessary
                # not removing vals from previous levels
                valList[node.val] -= 1
                length -= 1
            
            else:
                logging.debug("this is happening")  
                s.append(node.left)
                s.append(node.right)

            printStack(s)

        
        return result
    
    def checkPath(self, valList, length):
        odd = 0
        total = 0

        printList(valList)
        
        # must be at most 1 odd number of a particular digit
        for i in range(1, len(valList)):
            logging.debug(f"i is {i}, we have {valList[i]} of them")

            total += valList[i] 
            
            if valList[i] % 2 == 1:
                odd += 1
            
            if total == length: break

        logging.debug(f"We have {odd} odd values")
        
        return odd <= 1

def printList(s):
    print(f"Current list:")
    for i in s:
        print(f" --> {i}", end='')
    print("\n-------- list end ----------")

            
def printStack(s):
    logging.debug(f"Current stack:")
    for i in s:
        if i is None:
            logging.debug(" --> None")
            continue
        logging.debug(f" --> {i.val}")
    logging.debug("-------- stack end ----------")

a = Solution()
print(a.pseudoPalindromicPaths(TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))))
# print(a.pseudoPalindromicPaths(TreeNode(2, TreeNode(3), TreeNode(3))))
