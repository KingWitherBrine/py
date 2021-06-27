def solve(i, s1, s2):
    if i == n:
        return abs(s2-s1)
    return min(solve(i+1, s1+nums[i], s2), solve(i+1, s1, s2+nums[i]))

# from itertools import permutations as perms
# def solve(nums):
    # min_count = float("inf")
    # for i in perms(nums, len(nums)//2):
    #     if abs(sum(i[0])-sum(i[1])) < min_count:
    #         min_count = abs(sum(i[0])-sum(i[1]))
    # return min_count

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
    print(solve(0, 0, 0))
