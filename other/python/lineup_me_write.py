from itertools import permutations as perms
cows = sorted("Beatrice Sue Belinda Bessie Betsy Blue Bella Buttercup".split())

def solve(clues):
  for perm in perms(cows):
    if all(abs(perm.index(cow1) - perm.index(cow2)) == 1 for cow1, cow2 in clues):
      return perm
  return None

if __name__ == '__main__':
  with open('lineup.in') as f:
    n = int(f.readline())
    constraints = []
    for line in f:
      words = line.strip().split()
      constraints.append((words[0], words[-1]))

  with open('lineup.out', 'w') as f:
    print(*solve(constraints), sep='\n', file=f)