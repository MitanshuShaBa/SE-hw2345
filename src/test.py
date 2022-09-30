import unittest
import num
import Sym
import main
import Data as data
import sys
import csv_

sys.path.append("../code/")


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

    def test_the(self):
        assert main.the["eg"] == False   

    def test_csv(self):
        d, _, _, _, _, _, _ = csv_.read("./data/sample.csv", ",")
        n = len(d)
        print()
        print("Length of data:", n)
        for i, row in enumerate(d):
            if i > 10:
                break
            print(*row, sep=", ")
        print()

        assert n == 399

    def test_data(self):
        d = data.Data("../data/sample.csv")
        print()
        for col in d.cols.y:
            if col in d.cols.sym_columns:
                i = d.cols.names.index(col)
                obj = Sym.Sym(c=i+1, s=col)

                for value in d.rows:
                    obj.add(value[i])

                print(obj)
            if col in d.cols.num_columns:
                i = d.cols.names.index(col)
                obj = num.num(c=i+1, s=col)

                for value in d.rows:
                    obj.add(value[i])

                print(obj)

        print()

        assert obj.n == 398
        assert obj.name == "Mpg+"
        assert obj.hi == 50

    def test_stats(self):

        d = data.Data("../data/sample.csv")
        print()
        print("xmid", d.stats(2, fun="mid", showCols=d.cols.x))
        print("xdiv", d.stats(3, fun="div", showCols=d.cols.x))
        print("ymid", d.stats(2, fun="mid", showCols=d.cols.y))
        print("ydiv", d.stats(3, fun="div", showCols=d.cols.y))

        xmid = d.stats(2, fun="mid", showCols=d.cols.x)
        assert xmid[0][1] == 4  # Clndrs


if __name__ == "__main__":
    unittest.main()
