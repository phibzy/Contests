#!/usr/bin/python3

class Solution:
    def getStrongest(self, arr, k):
        if len(arr) == 1: return arr        
        arr.sort()
        
        median = arr[((len(arr) - 1) // 2)]
        rList = list()
        
        start = 0
        end = len(arr) - 1
        count = 0
        
        calc1 = abs(arr[start] - median)
        calc2 = abs(arr[end] - median)
        while end >= start and count < k:
            if calc1 > calc2:
                rList.append(arr[start])
                start += 1
            elif calc1 == calc2:
                if arr[start] > arr[end]:
                    rList.append(arr[start])
                    start += 1
                elif arr[start] == arr[end]:
                    rList.append(arr[start])
                    rList.append(arr[end])
                    start += 1
                    end -= 1
                else:
                    rList.append(arr[end])
                    end -= 1
            else:
                rList.append(arr[end])
                end -= 1
            
            count += 1
            calc1 = abs(arr[start] - median)
            calc2 = abs(arr[end] - median)
        
        return rList[:k]
            
