import re
import num
import Sym


class Cols:
    def __init__(self, names, sym_columns, num_columns, max_columns, min_columns, skip_column_name, skip_column_number):
        self.names = names
        self.all = []
        self.klass = None
        self.x = [
            col_name for col_name in names if col_name not in max_columns and col_name not in min_columns]  # independent cols
        # dependant cols
        self.y = [
            col_name for col_name in names if col_name in max_columns or col_name in min_columns]
        self.sym_columns = sym_columns
        self.num_columns = num_columns
        self.max_columns = max_columns
        self.min_columns = min_columns
        self.skip_column_name = skip_column_name
        self.skip_column_number = skip_column_number
