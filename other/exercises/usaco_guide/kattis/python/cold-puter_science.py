def solve(temps):
    count = 0
    for i in temps:
        if i < 0:
            count += 1
    return count

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        temps = list(map(int, f.readline().strip().split()))
        print(solve(temps))