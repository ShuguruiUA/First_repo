import sys


def parse_args():
    result = ""
    for arg in sys.argv[1:]:
        print(arg)
        result = " ".join(arg)

    return result
