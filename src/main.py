import config
import csv_

the = config.create()


data, _, _, _, _, _, _ = csv_.read(the['file'], the['separator'])
# print(len(data))
