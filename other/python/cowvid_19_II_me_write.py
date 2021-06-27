def solve(cows):
  radius = float("inf")
  prev_pos, prev_stat = cows[0]
  for pos, stat in cows:
    if stat != prev_stat:
      radius = min(radius, pos - prev_pos)
    prev_pos, prev_stat = pos, stat
  
  sick = [cow for cow in cows if cow[1] == 1]
  count = 1
  left = sick[0][0]
  for pos, stat in sick:
    if pos not in range(left, left+radius):
      count += 1
    left = pos
  return count

if __name__ == "__main__":
  with open(0) as f:
    n = int(f.readline())
    matrix = sorted([tuple(map(int, line.strip().split())) for line in f])
  print(solve(matrix))