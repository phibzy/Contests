#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 30, 2020 14:05:56 AEST
  @file        : q3

"""

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # bfs - find 1, run bfs. Then loop through - if any other ones found then disconnected
        
        i, j = 0, 0
        islandExists = False
        visited = dict()
        leastAdjacent = 4
        
        while i < len(grid):
            while j < len(grid[i]):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # new land - return 0 if already disconnected from already found land
                    if islandExists == True: return 0
                    
                    islandExists = True
                    # run bfs
                    
                    s = list()
                    s.append((i,j))

                    
                    while s:
                        n = 0
                        x, y = s.pop()
                        print(f"current coords are {x}, {y}")
                        visited[(x,y)] = True
                        
                        if self.checkLand(grid,  x-1, y): n+=1
                        if self.checkLand(grid,  x+1, y): n+=1
                        if self.checkLand(grid,  x, y-1): n+=1
                        if self.checkLand(grid,  x, y+1): n+=1
                            
                        leastAdjacent = min(leastAdjacent, n)
                        
                        if self.checkValid(grid, visited, x-1, y): s.append((x-1, y))
                        if self.checkValid(grid, visited, x+1, y): s.append((x+1, y))     
                        if self.checkValid(grid, visited, x, y-1): s.append((x, y-1))
                        if self.checkValid(grid, visited, x, y+1): s.append((x, y+1))
                            
                        # Did not handle the "bridge" case - i.e. element of n == 2 that when removed disconnects everything
                        # TL;DR If not in the corner and n==2 then answer is 1
                        
                    
                    
                    
                j += 1
            i += 1
            
        if len(grid[0]) == 2: return 2
            
        return leastAdjacent
                    
                # if land and not visited, run bfs
                # else do nothing
        
    
    # returns True if valid land
    def checkValid(self, grid, visited, x, y):
        if x < 0 or x >= len(grid): return False
        if y < 0 or y >= len(grid[0]): return False
        if (x,y) in visited: return False
        return grid[x][y] == 1 
    
    def checkLand(self, grid, x, y):
        print(f"current checkLand(x,y) are {x}, {y}")
        if x < 0 or x >= len(grid): return False
        if y < 0 or y >= len(grid[0]): return False
        return grid[x][y] == 1
