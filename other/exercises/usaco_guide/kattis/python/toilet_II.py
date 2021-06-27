def solve(starting, preferences):
    up, down, self_pref = 0, 0, 0
    if starting == "U":
        up += (preferences.count("D")*2)
        # down += 
        for i in range(len(preferences)-1):
            if preferences[0] != starting:
                self_pref += 1
            if preferences[i] != preferences[i+1]:
                self_pref += 1
    if starting == "D":
        up += 

if __name__ == "__main__":
    with open(0) as f:
        preferences = f.readline().strip()
        starting = preferences[0]
        preferences = preferences[1:]
    for i in solve(starting, preferences):
        print(i)