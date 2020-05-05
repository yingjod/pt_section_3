i = 1

while i <= 9:
    j = 1
    while j <= 9:
        print("%d * %d = %2d" % (j, i, i * j), end=" ")
        j += 1
    print()
i += 1
