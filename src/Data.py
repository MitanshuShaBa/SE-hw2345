import math


class Data:
    def stats(self, places, showCols, fun):
        showCols, fun= showCols or self.cols["y"], fun or "mid"
        t={}
        for _, col in showCols.items():
            v=fun(col)
            v=rnd(v, places) or v
            t[col["name"]]=v
        return t

def rnd(x, places):
    mul=10**(places or 2)
    return math.floor(x*mul+0.5)/mul