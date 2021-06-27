def solve(cows): # cows: [[7, 1], [1, 1]...[10, 0]]
  cows.sort()
  radius =  1# cows[-1][0] - cows[0][0] # float('inf')
  prev_position, prev_status = cows[0]
  for position, status in cows:
    if status != prev_status: # 1->0 or 0->1
      radius = min(radius, position - prev_position)
    prev_position, prev_status = position, status

  sick_cows = [cow for cow in cows if cow[1] == 1]
  count = 1
  left_bound = sick_cows[0][0]
  for position, status in sick_cows:
    if position not in range(left_bound, left_bound + radius):
      count += 1
    left_bound = position  # left_bound will ALWAYS update
  return count

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = sorted([list(map(int, f.readline().strip().split())) for i in range(n)])
    print(solve(n, matrix))