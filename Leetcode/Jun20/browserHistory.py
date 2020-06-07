#!/usr/bin/python3

class BrowserHistory:

    def __init__(self, homepage):
        self.bHist = list()
        self.fHist = list() # This is a stack
        self.bLen = 0
        self.fLen = 0
        self.currentPage = homepage
        

    def visit(self, url):
        self.addBHist(self.currentPage)
        self.currentPage = url
        self.fHist.clear()
        self.fLen = 0

    def back(self, steps):
        if not self.bHist: return self.currentPage
        
        self.fHist.append(self.currentPage)
        
        if steps > self.bLen:
            
            self.fHist += self.bHist[1:]
            self.fLen += self.bLen
            retVal = self.bHist[0]
            self.bHist.clear()
            
        elif steps > 1:
            
            self.fHist += self.bHist[-(steps - 1):]
            self.fLen += steps
            self.bHist = self.bHist[:-(steps - 1)]
            retVal = self.bHist.pop()
            self.bLen -= steps
            
        else:
            
            retVal = self.bHist.pop()
            self.bLen -= 1
            
        self.currentPage = retVal
        
        return retVal  

    def forward(self, steps):
        if not self.fHist: return self.currentPage
        
        self.bHist.append(self.currentPage)
        
        if steps > self.fLen:
            
            self.bHist += self.fHist[1:]
            self.bLen += self.fLen
            retVal = self.fHist[0]
            self.fHist.clear()
            
        elif steps > 1:
            
            self.bHist += self.fHist[-(steps - 1):]
            self.bLen += steps
            self.fHist = self.fHist[:-(steps - 1)]
            retVal = self.fHist.pop()
            self.fLen -= steps
            
        else:
            
            retVal = self.fHist.pop()
            self.fLen -= 1
            
        self.currentPage = retVal
        
        return retVal 
        
        
        
    def addBHist(self, url):
        self.bHist.append(url)
        self.bLen += 1
    
    def addFHist(self, url):
        self.fHist.append(url)
        self.fLen += 1

        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
