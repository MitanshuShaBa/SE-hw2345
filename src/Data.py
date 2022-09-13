import re
import main

def csv(fname, fun):
    sep="([^" + main.the["separator"] + "]+)"
    f = open(fname, 'r')
    while True:
        s = f.readline()
        if not s:
            return f.close()
        else:
            t={}
            for s1 in re.findall(sep, s):
                t[1+len(t)]=coerce(s1)
            fun(t)

def coerce(s):
    def fun(s1):
        if s1==True: return True
        if s1==False: return False
        return s1
    return int(s) or fun(re.search("^%s*(.−)%s*$", s))
