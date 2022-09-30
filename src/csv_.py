import csv


# Read the file
def read(file, separator):
    """
    params:
    file - filename
    separator - delimiter

    returns (data, sym_columns, num_columns, max_columns, min_columns)"""
    data = []
    num_columns = []
    sym_columns = []
    max_columns = []
    min_columns = []
    skip_column_number = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=separator)
        line = 0
        for row in csv_reader:
            row_data = []

            # Column names
            if line == 0:
                for i, name in enumerate(row):
                    if name.endswith(":"):
                        skip_column_number.append(i)
                        continue
                    if name.endswith("+"):
                        max_columns.append(name)
                    elif name.endswith("-"):
                        min_columns.append(name)

                    if name[0].isupper():
                        num_columns.append(name)
                    else:
                        sym_columns.append(name)

                    row_data.append(name)

            if line > 0:
                for i, value in enumerate(row):
                    if i in skip_column_number:
                        continue
                    row_data.append(float(value))

            line += 1
            data.append(row_data)
    return (data, sym_columns, num_columns, max_columns, min_columns)
