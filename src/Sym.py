import math


class Sym:
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}

    def __repr__(self):
        return f"{{:at {self.at} :n {self.n} :name {self.name}}}"

    def add(self, v):
        if v is not None:
            self.n += 1
            if v in self._has:
                self._has[v] += 1
            else:
                self._has[v] = 1

    def mid(self):
        most = -1
        for key, value in self._has.items():
            if value > most:
                mode = key
                most = value
        return mode

    def div(self):
        def p_log_p(p):
            return p * math.log(p, 2)

        e = 0
        for _, n in self._has.items():
            if n > 0:
                e = e-p_log_p(n/self.n)
        return e
