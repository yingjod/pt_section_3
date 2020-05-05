def list_(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print("%4d" % j, end="")
        print()


if __name__ == "__main__":
    num = eval(input("enter a number: "))
    list_(num)
