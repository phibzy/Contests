#!/usr/bin/python3

class Solution:
    def minReorder(self, n, connections):
        # Step 1 - Create graph with adj list
        graph = [list() for _ in range(n)]
        connected = [False for _ in range(n)] # keeps track of who's already connected to 0
        visited = [False for _ in range(n)] # keeps track of who's already connected to 0
        q = list()

        connected[0] = True
        result = 0

        for i, j in connections:
            graph[i].append((j, True))
            if j == 0: connected[i] = True
            graph[j].append((i, False))

        q.append(0)
        
        while q:
            node = q.pop(0)
            if visited[node]: continue
            for neighbour, flag in graph[node]:
                if (not connected[neighbour]) and flag == True:
                    result += 1
                    connected[neighbour] = True
                
                q.append(neighbour)

            visited[node] = True

        return result


a = Solution()
print(a.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))


        
