import num
import Sym
import main
import Data as data
import sys

sys.path.append("../code/")

import unittest

class TestCSVReader(unittest.TestCase):

    def test_big_num(self):
        obj = num.num()
        main.the["nums"] = 32
        for i in range(1, 1001):
            obj.add(i)
        assert len(obj._has) == 32

    def test_Sym(self):
        obj = Sym.Sym()
        for value in ["a", "a", "a", "a", "b", "b", "c"]:
            obj.add(value)
        mode, entropy = obj.mid(), obj.div()
        entropy = (entropy*1000)//1/1000
        assert(mode == "a" and 1.37 <= entropy and entropy <= 1.38)

    def test_num(self):
        obj = num.num()
        main.the["nums"] = 512
        for i in range(1, 101):
            obj.add(i)
        mid, div = obj.mid(), obj.div()
        assert mid <= 52 and mid >= 50 and div < 32 and div > 30.5
    
    def test_data(self):
        d = data.Data("../data/sample.csv")
        for _, col in d.cols.y.items():
            if not isinstance(col, num.Num):
                continue
            print(
                "{ "
                + f":at {col.at} :hi {col.high} :isSorted {col.isSorted} :lo {col.lo} :n {col.n} :name {col.name} :w {col.w}"
                + " }"
            )
        return True, "PASS"

    def test_csv():
        print("{", end=" ")
        d = data.Data("../data/sample.csv")
        for i, col in d.cols.all.items():
            print(col.name, end=" ")
        print("}")
        for i, row in d.rows.items():
            if i > 10:
                break
            print("{", end=" ")
            for j, cell in row.cells.items():
                print(cell, end=" ")
            print("}")

        return True, "PASS"

    def test_stats():
    
        d = data.Data("../data/sample.csv")
        print()
        print("xmid", d.stats(fun="mid", places=2, showCols=d.cols.x))
        print("xdiv", d.stats(fun="div", places=3, showCols=d.cols.x))
        print("ymid", d.stats(fun="mid", places=2, showCols=d.cols.y))
        print("ydiv", d.stats(fun="div", places=3, showCols=d.cols.y))
        return True, "PASS"

if __name__ == "__main__":
    unittest.main()
