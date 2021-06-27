def solve(cows):
    p = {}
    count = 0
    for i in range(len(cows)):
        if cows[i] in p.keys():
            p[cows[i]].append(i)
        else:
            p[cows[i]] = [i]
    for i in cows:
        for j in cows[p[i][0]+1:p[i][1]]:
            if not p[j][0] in range(p[i][0], p[i][1]) and p[j][1] in range(p[i][0], p[i][1]):
                count += 1
    return count // 2
if __name__ == "__main__":
    with open("circlecross.in", "r") as f:
        cows = f.readline().strip()
    with open("circlecross.out", "w") as f:
        print(str(solve(cows)), file=f)