from cs50 import get_int


def get_input():
    while True:
        x = get_int("enter the desired height: ")
        if x > 0 and x <= 8:
            return x
        else:
            return get_input()


height = get_input()

for rows in range(height):
    for spaces in range(height - rows - 1):
        print(" ", end="")
    for blocks in range(rows + 1):
        print("#", end="")
    print()
