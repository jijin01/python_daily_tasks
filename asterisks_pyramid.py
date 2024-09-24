def valid_input(num):
    while True:
        try:
            row = int(input(num))
            if isinstance(row, int):
                return row
        except ValueError:
            print("The input should be an integer")


def asterisks_pyramid():
    row = valid_input("How many rows you want: ")
    k = 0
    for i in range(1, row + 1):
        for space in range(1, (row - i) + 1):
            print(end="  ")

        while k != (2 * i - 1):
            print("* ", end="")
            k += 1

        k = 0
        print()


asterisks_pyramid()
