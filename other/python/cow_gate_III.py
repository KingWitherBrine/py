def cow_gate(num_cows, cows):
    cows = sorted(cows)
    time = 0
    for i in range(len(cows) - 1):
        if sum(cows[i]) > cows[i+1][0]:
            cows[i+1] = cows[i][0] + cows[i+1][0]
            time += sum(cows[i]) + cows[i+1][1]
    return time
        
# print(cow_gate(3, [[2, 1], [8, 3], [5, 7]]))

if __name__ == "__main__":
    with open(0) as f:
        num_cows = int(f.readline().strip())
        cows = [list(map(int, f.readline().strip().split())) for i in range(num_cows)]
    print(cow_gate(num_cows, cows))