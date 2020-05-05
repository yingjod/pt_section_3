def run(i):
    for i in range(i, 0, -1):
        for j in range(1, i + 1):
            print("%4d" % j, end=" ")
        print()


if __name__ == "__main__":
    i = eval(input(" Enter a number : "))
    run(i)
