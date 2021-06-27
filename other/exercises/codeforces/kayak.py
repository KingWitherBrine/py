def solve(nums):
    if len(nums) == 2:
        return 0
    nums = sorted(nums)
    total_min_instability = float("inf")
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            temp_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
            min_instability = total_min_instability
            for k in range(0, len(temp_nums), 2):
                if temp_nums[k+1] - temp_nums[k] < min_instability:
                    min_instability =  temp_nums[k+1] - temp_nums[k]
            if min_instability < total_min_instability:
                total_min_instability = min_instability
    return total_min_instability


if __name__ == "__main__":
    with open(0) as f:
        n = f.readline().strip().split()
        nums = list(map(int, f.readline().strip().split()))
    print(solve(nums))