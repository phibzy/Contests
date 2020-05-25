#!/usr/bin/python3

class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        wordList = sentence.split()
        swLen = len(searchWord)
        
        result = -1
        
        for i in range(len(wordList)):
            if wordList[i][:swLen] == searchWord:
                result = i + 1
                break
                
        return result
    
