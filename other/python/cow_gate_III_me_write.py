def cow_gate3(cows):
    time = 0
    for start, question_time in cows:
        time = max(time, start) + question_time
    return time

if __name__ == "__main__":
    with open("cowqueue.in") as f:
        n = int(f.readline())
        cows = sorted([tuple(map(int, line.split())) for line in f])
    with open("cowqueue.out", "w") as f:
        print(cow_gate3(cows), file=f)