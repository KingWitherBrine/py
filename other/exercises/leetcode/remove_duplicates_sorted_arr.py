def solve(nums):
    nums = list(set(nums))
    return len(nums)

if __name__ == "__main__":
    print(solve([1,1,2]))