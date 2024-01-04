#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined = dir(hidden_4)
    for i in defined:
        if i[0:2] == "__":
            continue
        else:
            print(f"{i:s}")
