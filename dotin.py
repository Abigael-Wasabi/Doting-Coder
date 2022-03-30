def show_stars(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print("\n")


show_stars(9)
