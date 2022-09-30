import math
import csv
import Cols
import Sym
import num
import csv_
import main


class Data:
    def __init__(self, src):
        the = main.the

        self.cols = None
        self.rows = []
        if(type(src) == str):
            csv_data = csv_.read(the['file'], the['separator'])

            data, sym_columns, num_columns, max_columns, min_columns, skip_column_name, skip_column_number = csv_data

            self.add(data[0], sym_columns, num_columns, max_columns,
                     min_columns, skip_column_name, skip_column_number)
            for row in data[1:]:
                self.add(row)

    def stats(self, places, showCols=None, fun="mid"):
        if showCols is None:
            showCols = self.cols.y
        t = []
        for col in showCols:
            if col in self.cols.sym_columns:
                obj = Sym.Sym()
                i = self.cols.names.index(col)

                for value in self.rows:
                    obj.add(value[i])

            if col in self.cols.num_columns:
                obj = num.num()
                i = self.cols.names.index(col)

                for value in self.rows:
                    obj.add(value[i])

            output_fun = obj.mid() if fun == "mid" else obj.div()
            output_fun = round(output_fun, places)
            t.append((col, output_fun))

        return t

    def add(self, row, sym_columns=None, num_columns=None, max_columns=None,
            min_columns=None, skip_column_name=None, skip_column_number=None):

        if self.cols is None and num_columns is not None:
            self.cols = Cols.Cols(row, sym_columns, num_columns, max_columns,
                                  min_columns, skip_column_name, skip_column_number)
        else:
            row = self.rows.append(row)


def rnd(x, places):
    mul = 10**(places or 2)
    return math.floor(x*mul+0.5)/mul
