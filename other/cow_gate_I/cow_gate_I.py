def solve(logs):
    starting_state = {}
    count = 0
    for i in range(1, 11):
        for log in logs:
            if i == log[0] and i not in starting_state:
                starting_state[i] = log[1]
    # print(starting_state)
    for log in logs:
        if starting_state[log[0]] != log[1]:
            starting_state[log[0]] = log[1]
            # print(log, starting_state[log[0]])
            count += 1
    return count
if __name__ == "__main__":
    with open(0) as f:
        num_logs = int(f.readline().strip())
        logs = [list(map(int, f.readline().strip().split())) for i in range(num_logs)]
    print(solve(logs))