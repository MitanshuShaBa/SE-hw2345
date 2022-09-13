import re
import num
import Sym

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass =  None
        self.x = {}
        self.y = {}
        for k, value in enumerate(self.names):
            if re.search("^[A-Z]*", value):
                self.all[k] = value
                num(k,value)
            else:
                Sym(k,value)
            if not re.search(":$", value):
                if re.search("[!+-]", value):
                    self.y[k] = value 
                else:
                    self.x[k] = value 
                if re.search("!$", value):
                    self.klass[k]=value



