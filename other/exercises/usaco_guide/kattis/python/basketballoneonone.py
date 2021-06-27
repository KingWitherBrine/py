def solve(records):
    a = 0
    b = 0
    for i in range(0, len(records), 2):
        if records[i] == "A": a += int(records[i+1])
        if records[i] == "B": b += int(records[i+1])
    if a > b: return "A"
    else: return "B"

if __name__ == "__main__":
    with open(0) as f:
        records = f.readline().strip()
    print(solve(records))