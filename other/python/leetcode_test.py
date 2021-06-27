def solve(nums, target):
    s = set()
    nums = sorted(nums)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            start, end = j+1, len(nums) - 1
            while start < end:
                if nums[i] + nums[j] + nums[start] + nums[end] == target:
                    s.add((nums[i], nums[j], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
    return s

print(solve([1,0,-1,0,-2,2], 0))