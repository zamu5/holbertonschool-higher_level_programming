#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lis = dir(hidden_4)
    for x in lis:
        if x[:2] != "__":
            print(x)
