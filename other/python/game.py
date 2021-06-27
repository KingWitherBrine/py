from itertools import permutations as perms

def is_legal(perm):
  for i in range(len(perm)):
    for j in range(i+1, len(perm)):
      if abs(j-i) == abs(perm[j]-perm[i]):
        return False
  return True

def is_restricted(perm, lines):
  for i in range(len(perm)):
    if lines[i][perm[i]] == "*":
      return True
  return False

def solve(perm, lines):
  count = 0
  for perm in perms(range(8), 8):
    if is_legal(perm) and not is_restricted(perm, lines):
      count += 1
  return count

if __name__ == "__main__":
  with open(0) as f:
    num_lines = 8
    lines = [f.readline().strip() for _ in range(8)]
  print(solve(num_lines, lines))