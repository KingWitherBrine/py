def solve(n, nums):
    count = 0
    for i in range(n-1):
        if nums[i+1] < nums[i]:
            count += nums[i]-nums[i+1]
            nums[i+1] += (nums[i]-nums[i+1])
    return count

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
    print(solve(n, nums))