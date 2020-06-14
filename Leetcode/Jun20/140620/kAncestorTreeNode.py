#!/usr/bin/python3

"""
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.

Note:
    Difficult = Hard due to volume of input, number of queries

    Strategy was to intialise DP hash when class was created, still timed out though

"""

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.known = dict()
        self.parent = parent
        
        # Populate DP hash as you initialise
        # Using DFS
        
        for i in range(n-1, 0, -1):
            self.known[i] = dict()
            self.DFSPopulate(i, parent[i], 1)
            
            
    def DFSPopulate(self, orig, curr, level):
        if curr == -1:
            self.known[orig]['length'] = level - 1
            return
        
        self.known[orig][level] = curr
        
        self.DFSPopulate(orig, self.parent[curr], level+1)

    def getKthAncestor(self, node: int, k: int) -> int:
        # Handle k > ancestor no case
        # Case for 0
        if node == 0: return -1
        
        if k > self.known[node]['length']: return -1
        
        return self.known[node][k]
        
