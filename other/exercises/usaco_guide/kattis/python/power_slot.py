if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        cases = [list(map(int, f.readline().strip().split()))[1:] for i in range(n)]
        for i in cases:
            print(sum(i) - len(i) + 1)