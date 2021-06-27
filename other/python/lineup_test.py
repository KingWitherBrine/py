from itertools import permutations as perms

cows = sorted('Bessie, Buttercup, Belinda, Beatrice, Bella, Blue, Betsy, Sue'.split(', '))

def livestock_lineup(constraints):
  for possible_answer in perms(cows): # possible_answer -> ['Bessie', 'Buttercup', 'Belinda', ..., 'Sue']
    if all(abs(possible_answer.index(cow1) - possible_answer.index(cow2)) == 1 for cow1, cow2 in constraints):
      return possible_answer
  return None

if __name__ == '__main__':
  with open('lineup.in') as f:
    n = int(f.readline())
    constraints = []  # [('Buttercup', 'Buttercup'), ('Blue', 'Bella'), ...]
    for line in f:
      words = line.strip().split()
      constraints.append((words[0], words[-1]))

  with open('lineup.out', 'w') as f:
    print(*livestock_lineup(constraints), sep='\n', file=f)