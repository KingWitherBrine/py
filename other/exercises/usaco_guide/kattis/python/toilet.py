def solve(starting, preferences):
    counts = [0, 0, 0]
    # always leave up
    state = "U"
    for i in preferences:
        if i != state:
            counts[0] += 2
    # always leave down 
    state = "D"
    for i in range(len(preferences)):
        if i != state:
            counts[1] += 2
    # always leave personal preference
    state = starting
    for i in preferences:
        if i != state:
            counts[2] += 1
            state = i
    return counts
if __name__ == "__main__":
    with open(0) as f:
        preferences = f.readline().strip()
        starting = preferences[0]
        preferences = preferences[1:]
    for i in solve(starting, preferences):
        print(i)