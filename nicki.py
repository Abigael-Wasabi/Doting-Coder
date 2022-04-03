def numbers(limit):
    for i in range(1, limit):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")


numbers(21)


def even_or_odd():
    n = int(input("enter a no: "))
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


even_or_odd()
