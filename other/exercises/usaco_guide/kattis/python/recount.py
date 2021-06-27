def solve(cases):
    d = {}
    for i in cases:
        d[i] = d.get(i, 0) + 1
    max_vote = []
    max_num = float("-inf")
    new_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    if list(new_d.items())[0][1] == list(new_d.items())[1][1]:
        return "Runoff!"
    return list(new_d.items())[0][0]

if __name__ == "__main__":
    with open(0) as f:
        cases = []
        for i in f:
            if cases == "***":
                break
            cases.append(i.strip())
    cases = cases[:-1]
    print(solve(cases))