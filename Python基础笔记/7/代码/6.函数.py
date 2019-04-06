# for in
def table(row):
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print("{}*{}={:2}   ".format(i, j, i * j), end="")
        print()
table(7)




