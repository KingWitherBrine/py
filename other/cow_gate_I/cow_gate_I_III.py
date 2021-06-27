def solve(logs):
    counts = {} # key: cow_num value: side
    total = 0
    for cow_num, side in logs:
        if cow_num in counts:
            if counts[cow_num] != side:
                total += 1
        counts[cow_num] = side 
    return total

if __name__ == "__main__":
    with open(0) as f:
        num_logs = int(f.readline().strip())
        logs = [list(map(int, f.readline().strip().split())) for i in range(num_logs)]
    print(solve(logs))