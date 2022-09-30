import num
import Sym
import main
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


if __name__ == "__main__":
    unittest.main()
