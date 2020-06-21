#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jun 21, 2020 12:44:32 AEST
  @file        : folderNames

"""

class Solution:
    def getFolderNames(self, names):
        
        used = dict()
        
        for i in range(len(names)):
            n = names[i]
            
            if n in used:
                k = used[n]
                
                while n+f"({k})" in used:
                    k += 1
                
                names[i] = n + f"({k})"
                
                used[n] = k
                
                    
            used[names[i]] = 1
        
        return names
                

a = Solution()
