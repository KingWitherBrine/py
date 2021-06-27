def solve(n, k, nums):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if count + 1 == len(nums):
                return count
            if (nums[j] - nums[i]) <= k:
                count += 1
    return count

if __name__ == "__main__":
    with open(0) as f:
        n, k = map(int, f.readline().strip().split())
        nums = [int(f.readline().strip()) for i in range(n)]
    print(solve(n, k, nums))