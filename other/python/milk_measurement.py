def measure(nums):
  cows = {"Bessie": 7, "Mildred": 7, "Elsie": 7}
  winner = ""
  total_change = 0
  nums = sorted(nums)
  for day, name, change in nums:
    cows[name] += change
    # a = [key for key, value in cows.items() if value == max(cows.values())]
    a = "".join([key for key in cows if cows[key] == max(cows.values())])
    if a != winner:
      total_change += 1
      winner = a
  return total_change 
print(measure([[7, "Mildred", 3], [4, "Elsie", -1], [9, "Mildred", -1], [1, "Bessie", 2]]))
if __name__ == "__main__":
  with open(0) as f:
    N = int(f.readline())
    matrix = []
    for line in f:
      day, name, change = line.strip().split()
      matrix.append([int(day), name, int(change)])
  print(measure(matrix))