def solve(num):
    lst = [num]
    while True:
        if lst[-1] == 1: return lst
        if lst[-1] % 2 == 0: lst.append(int(lst[-1] / 2))
        else: lst.append(int(lst[-1] * 3 + 1))
        

if __name__ == "__main__":
    with open(0) as f:
        num = int(f.readline().strip())
    print(*solve(num))