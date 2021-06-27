def solve(a):
    lst = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] != "0" and a[i] != "0" and "1" not in a[i+1:j]:
                lst.append(abs(j-i))
    return lst

if __name__ == "__main__":
    with open(0) as f:
        a = f.readline().strip()
    print(solve(a))