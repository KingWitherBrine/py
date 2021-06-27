def solve(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i

if __name__ == "__main__":
    print(solve([2,2,1]))