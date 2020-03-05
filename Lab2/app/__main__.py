# Author: Arvydas Apulskis IFF-7/13
# Module: P176B101 Intelektikos pagrindai
# Task: LAB2.


def main():
    f = open("./data/sunspot.txt", "r")
    contents = f.read()
    print(contents)

if __name__ == "__main__":
    main()
