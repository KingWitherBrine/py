# O(N^2) AC
def solve(n, nums):
  for i in range(1, nums[0] + 1):
    possible_list = [i]
    check_duplicates = {i}
    for num in nums:
      next_number = num - possible_list[-1]
      possible_list.append(next_number)
      if next_number in check_duplicates or next_number not in range(1, n + 1):
        break
      check_duplicates.add(next_number)
    if len(possible_list) == n:
      return possible_list

if __name__ == '__main__':
  with open(0) as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
  result = solve(n, nums)
  print(*result)