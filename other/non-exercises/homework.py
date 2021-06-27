n = int(input("请给我一个数字: "))
for i in range(0, n):
    for j in range(i):
        print((j + 1), "*", (j + j + 1), "=", (j + 1) * (j + j + 1), end =" ")
        print((i + 1), "*", (i + 1), "=", (i + 1) * (i + 1), end =" ")