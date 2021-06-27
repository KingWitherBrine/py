def solve(nums):
    return len(set(nums))

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
    print(solve(nums))