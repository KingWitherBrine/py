def solve(cows):
  logs = [None] * (len(cows) + 1)
  count = 0
  for cow_id, side in cows:
    if logs[cow_id] != None and logs[cow_id] != side:
      count += 1
    logs[cow_id] = side
  return count
if __name__ == "__main__":
  with open("crossroad.in") as f:
    n = int(f.readline())
    cows = [tuple(map(int, line.strip().split())) for line in f]
  with open("crossroad.out", "w") as f:
    print(solve(cows), file=f)