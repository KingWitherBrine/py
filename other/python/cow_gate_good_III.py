def cow_gate(num_cows, cows):
    cows = sorted(cows)
    time = 0
    for a, b in cows:
        if time < a:
            time = a
        time += b
    return time

if __name__ == "__main__":
    with open(0) as f:
        num_cows = int(f.readline().strip())
        cows = [list(map(int, f.readline().strip().split())) for i in range(num_cows)]
    print(cow_gate(num_cows, cows))