def list(num, num_1):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            num_1 = num_1 * j
        print("# %d ! = %d" % (i, num_1))


if __name__ == "__main__":
    num = eval(input())
    num_1 = 1
    list(num, num_1)
