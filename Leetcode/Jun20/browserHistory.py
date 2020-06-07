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
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
