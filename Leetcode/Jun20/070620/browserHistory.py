#!/usr/bin/python3

import logging
import sys
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format="%(levelname)s - %(msg)s")
# logging.disable(logging.DEBUG)

class BrowserHistory:

    def __init__(self, homepage):
        self.bHist = list()
        self.fHist = list() # This is a stack
        self.bLen = 0
        self.fLen = 0
        self.currentPage = homepage
        

    def visit(self, url):
        logging.debug("Visit call".center(30,'-'))
        self.debugPrint()

        self.addBHist(self.currentPage)
        self.currentPage = url
        self.fHist.clear()
        self.fLen = 0

        logging.debug("End visit call".center(30,'-'))
        self.debugPrint()

    def back(self, steps):
        logging.debug("Back call".center(30,'-'))
        self.debugPrint()

        if not self.bHist: return self.currentPage
        
        self.fHist.append(self.currentPage)
        self.fLen += 1
        
        if steps > self.bLen:

            logging.debug("Steps were greater")
            
            self.fHist += self.bHist[1:]
            self.fLen += self.bLen - 1
            retVal = self.bHist[0]
            self.bHist.clear()
            self.bLen = 0
            
        elif steps > 1:

            logging.debug("Steps normal case")
            
            self.fHist += self.bHist[-(steps - 1):]
            self.fLen += steps - 1
            self.bHist = self.bHist[:-(steps - 1)]
            retVal = self.bHist.pop()
            self.bLen -= steps
            
        else:
            logging.debug("Equal to 1 case")
            
            retVal = self.bHist.pop()
            self.bLen -= 1
            
        self.currentPage = retVal

        logging.debug("End back call".center(30,'-'))
        self.debugPrint()
        logging.debug(f"retVal is {retVal}")
        
        return retVal  

    def forward(self, steps):
        logging.debug("Forward call".center(30,'-'))
        self.debugPrint()

        if not self.fHist: return self.currentPage
        
        self.bHist.append(self.currentPage)
        self.bLen += 1
        
        if steps > self.fLen:
            
            logging.debug("Steps were greater")

            self.bHist += self.fHist[1:]
            self.bLen += self.fLen - 1
            retVal = self.fHist[0]
            self.fHist.clear()
            self.fLen = 0
            
        elif steps > 1:
            
            logging.debug("Steps normal case")

            self.bHist += self.fHist[-(steps - 1):]
            self.bLen += steps - 1
            self.fHist = self.fHist[:-(steps - 1)]
            retVal = self.fHist.pop()
            self.fLen -= steps
            
        else:
            
            logging.debug("Equal to 1 case")

            retVal = self.fHist.pop()
            self.fLen -= 1
            
        self.currentPage = retVal

        logging.debug("End of Forward call".center(30,'-'))
        self.debugPrint()
        logging.debug(f"retVal is {retVal}")
        
        return retVal 
        
        
        
    def addBHist(self, url):
        self.bHist.append(url)
        self.bLen += 1
    
    def addFHist(self, url):
        self.fHist.append(url)
        self.fLen += 1

    def debugPrint(self):
        logging.debug(f"currentPage is {self.currentPage}")
        logging.debug(f"bLen is {self.bLen}, bHist is {self.bHist}")
        logging.debug(f"fLen is {self.fLen}, fHist is {self.fHist}")


        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



cList = ["BrowserHistory","back","back","visit","forward","visit","visit","visit","back","visit","visit","visit","back","visit","visit","visit","visit","back","visit","visit","visit","visit","visit","visit","visit","back","forward","back","forward","visit","back","visit","visit"]

aList = [["icpbj.com"],[1],[10],["xbepk.com"],[8],["kls.com"],["dlkwxpf.com"],["pnep.com"],[9],["rmis.com"],["bxf.com"],["dz.com"],[2],["acuqsax.com"],["dcvo.com"],["ijbg.com"],["nlott.com"],[7],["dd.com"],["vssnq.com"],["teur.com"],["pn.com"],["szi.com"],["brhldg.com"],["yulyoqv.com"],[4],[10],[8],[5],["av.com"],[3],["okr.com"],["meli.com"]]

c = globals()['BrowserHistory'](aList[0][0])

for i in range(1, len(aList)):
    logging.debug('')
    logging.debug("".rjust(30, '*'))
    logging.debug(f"Calling function {cList[i]} with arg {aList[i][0]}")
    func = getattr(c, cList[i])
    func(aList[i][0])

    logging.debug("".rjust(30, '*'))
