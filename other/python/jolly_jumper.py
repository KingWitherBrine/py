def solve(nums):
  len_num, other = nums[0], nums[1:]
  lst = [abs(other[i] - other[(i+1)]) for i in  range(len_num - 1)]
  return "Jolly" if list(range(1, len_num)) == sorted(lst) else "Not jolly"

if __name__ == "__main__":
  with open(0) as f:
    nums = [list(map(int, line.strip().split())) for line in f]
  for i in nums:
    print(solve(i))