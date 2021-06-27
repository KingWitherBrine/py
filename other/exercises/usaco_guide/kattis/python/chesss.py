def solve(nums):
    correct = [1, 1, 2, 2, 2, 8]
    result = [0, 0, 0, 0, 0, 0]
    for i in range(len(nums)):
        result[i] = correct[i] - nums[i]
    return result

if __name__ == "__main__":
    with open(0) as f:
        nums = list(map(int, f.readline().strip().split()))
    print(*solve(nums))