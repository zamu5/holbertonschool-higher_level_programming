#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} {}:".format(len(sys.argv) - 1, "arguments"
                          if len(sys.argv) != 2 else "argument"))
    for x in range(1, len(sys.argv)):
        print("{}: {}".format(x, sys.argv[x]))
