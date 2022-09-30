import math
import csv
import Cols


class Data:
    def __init__(self, src):

        self.cols = 0
        self.rows = {}
        if(type(src) == str):
            csv(src, self.add(row))
        else:
            for _, row in src.items():
                self.add(row)

    def stats(self, places, showCols, fun):
        showCols, fun = showCols or self.cols["y"], fun or "mid"
        t = {}
        for _, col in showCols.items():
            v = fun(col)
            v = rnd(v, places) or v
            t[col["name"]] = v
        return t

    def add(self, xs, row):

        if self.cols is None:
            self.cols = Cols(xs)
        else:
            row = self.rows.push(xs.cells, xs)
            for _, todo in zip(self.cols.x, self.cols.y):
                for _, col in todo.items():
                    col.add(row.cells[col.at])


def rnd(x, places):
    mul = 10**(places or 2)
    return math.floor(x*mul+0.5)/mul
