def solve(nums):
    new_nums = sorted(nums)
    for i in range(len(nums)):
        if max(nums[:i+1]) - min(nums[:i+1]) > 1:
            return nums[:i+1]
if __name__ == "__main__":
    print(solve([1,3,2,2,5,2,3,7])) 