def solve(logs):
    counts = [None] * len(logs)
    total = 0
    for log in logs:
        if counts[log[0]-1] != log[1] and counts[log[0]-1] != None:
            total += 1
        counts[log[0]-1] = log[1]
    return total
    
if __name__ == "__main__":
    with open(0) as f:
        num_logs = int(f.readline().strip())
        logs = [list(map(int, f.readline().strip().split())) for i in range(num_logs)]
    print(solve(logs))