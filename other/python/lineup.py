from itertools import permutations as perms
cows = sorted("Beatrice Sue Belinda Bessie Betsy Blue Bella Buttercup".split())

def order(clues):
  for perm in perms(cows):
    if all(abs(perm.index(cow1) - perm.index(cow2)) == 1 for cow1, cow2 in clues):
      return perm

if __name__ == '__main__':
  with open("lineup.in", "r") as f:
    a = int(f.readline())
    clues = []
    for line in f:
      lst = line.strip().split()
      clues.append((lst[0], lst[-1]))
  with open("lineup.out", "w") as f:
    for i in order(clues): 
        print(i, file=f)