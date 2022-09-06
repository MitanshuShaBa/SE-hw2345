import config
import num
import Sym
import main

def big_num():
    obj = num.num()
    main.the["nums"] = 32
    for i in range(1, 1001):
        obj.add(i)
    assert len(obj._has) == 32

if __name__ == "__main__":
    big_num()
    print("All test cases passed")