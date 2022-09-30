import sys


def create():
    arguments = sys.argv

    # Creating the config
    the = {"eg": False, "dump": False, "file": "./data/sample.csv",
           "help": False, "nums": 512, "seed": 10019, "separator": ","}

    for i, arg in enumerate(arguments):
        if arg == "-e" or arg == "--eg":
            the["eg"] = True
        if arg == "-d" or arg == "--dump":
            the["dump"] = True
        if arg == "-f" or arg == "--file":
            the["file"] = arguments[i+1]
        if arg == "-h" or arg == "--help":
            the["help"] = True
        if arg == "-n" or arg == "--nums":
            the["nums"] = int(arguments[i+1])
        if arg == "-s" or arg == "--seed":
            the["seed"] = int(arguments[i+1])
        if arg == "-S" or arg == "--separator":
            the["separator"] = arguments[i+1]

    return the
