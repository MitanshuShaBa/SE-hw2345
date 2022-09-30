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

    def add(self, v):
        pos = 0
        if v is not None:
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if len(self._has) < main.the["nums"]:
                pos = 1 + len(self._has)
            elif random.randint(0, len(self._has)) < main.the["nums"]/self.n:
                pos = random.randint(0, len(self._has))

            if pos != 0:
                self.isSorted = False
                self._has[pos] = int(v)

    def per(self, t, p):
        p = math.floor(p*len(t)+0.5)
        return (t[max(1, min(len(t), p))])

    def div(self):
        a = self.nums()
        return (self.per(a, 0.9) - self.per(a, 0.1))/2.58

    def mid(self):
        return(self.per(self.nums(), 0.5))
