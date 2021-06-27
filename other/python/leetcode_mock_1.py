def solve(s):
    new_s = []
    d = {}
    output = []
    for i in range(len(s)):
        d[s[i]] = i
        all_true = True
        for j in d:
            if j not in s[i:]:
                all_true = False
                break
            if not all_true:
                output.append(i)
    return output

if __name__ == "__main__":
    with open(0) as f:
        s = f.readline().strip()
    print(solve(s))