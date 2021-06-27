from itertools import permutations as perms

def cow_gymnastics(ranks, K, N):
  t = 0
  for i, j in perms(range(1, N+1), 2):
    if all(rank.index(i) < rank.index(j) for rank in ranks):
      t += 1
  return t
if __name__ == '__main__':
  with open("gymnastics.in", "r") as f: 
    K1, N1 = map(int, f.readline().split()) 
    ranks = [list(map(int, line.strip().split())) for line in f] 
  result = cow_gymnastics(ranks, K1, N1)
  with open("gymnastics.out", "w") as f:
    print(result, file=f)