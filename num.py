import math
import random
import main

class num():

    def __init__(self, c=0, s=""):
        self.n = 0
        self._has = {}
        self.at = c
        self.name = s
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True
        self.w = -1 if s.find("-$") else 1 

    def nums(self):
        if self.isSorted == False: 
            sorted(self._has)
            self.isSorted = True      
        return self._has