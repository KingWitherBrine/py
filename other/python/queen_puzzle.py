from itertools import permutations as perms

def is_legal(nums):
  length = len(nums)
  for i in range(length):
    for j in range(i+1, length):
      if abs(j - i) == abs(nums[j] - nums[i]):
        return False
  return True

def is_restricted(perm, lines):
  for i in range(len(perm)):
    if lines[i][perm[i]] == "*":
      return True
  return False
  
# print(is_restricted([2, 0, 3, 1], ["..*.", ".*..", "....", "...."]))

def solve(num, lines):
  count = 0
  for perm in perms(range(8), 8): # perms: (0, 1, 2, ...., 7)
    if is_legal(perm):
      if not is_restricted(perm, lines):
        count += 1
  return count

# print(solve(8, ['........', '........', '..*.....', '........', '........', '.....**.', '...*....', '........']))

if __name__ == "__main__":
  with open(0) as f:
    num = 8
    lines = [f.readline().strip() for _ in range(num)]
  # print(solve(8, lines))
  print(num, lines)