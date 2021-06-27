def solve(n, x, nums):
    # result = []
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == x:
    #             result = [i+1, j+1]
    # if result:
    #     return result
    # return "IMPOSSIBLE"
    new_nums = sorted(nums)
    i, j = 0, len(nums) - 1
    while i < j:
        if new_nums[i] + new_nums[j] == x:
            break
        if new_nums[i] + new_nums[j] < x:
            i += 1
        if new_nums[i] + new_nums[j] > x:
            j -= 1
    if i == j:
        return "IMPOSSIBLE"
    return len(nums) - nums[::-1].index(new_nums[j]), nums.index(new_nums[i])+1

if __name__ == "__main__":
    with open(0) as f:
        n, x = map(int, f.readline().strip().split())
        nums = list(map(int, f.readline().strip().split()))
    if solve(n, x, nums) == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        print(*solve(n, x, nums))