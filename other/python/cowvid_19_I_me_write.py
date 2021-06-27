def largest_distance(s):
  distance, current_start, distance_start = 0, -1, 0
  for i in range(len(s)):
    if s[i] == "1":
      if current_start != -1 and i - current_start > distance:
        distance = i - current_start
        distance_start = current_start
      current_start = i
  return distance, distance_start

def smallest_distance(s):
  distance, current_start = len(s) - 1, -1
  for i in range(len(s)):
    if s[i] == "1":
      if current_start != -1:
        distance = min(distance, i-current_start)
      current_start = i
  return distance

def put_cow_in_largest_distance(s):
  distance, distance_start = largest_distance(s)
  s = list(s)
  if distance >= 2:
    s[distance_start + distance//2] = "1"
    return smallest_distance(s)
  return 0

def solve(s):
  distance, distance_start = largest_distance(s)
  answer = 0 
  # C1: Put both cows in same gap
  if distance >= 3:
    new_s = list(s)
    new_s[distance_start+distance//3] = "1"
    new_s[distance_start+distance//3*2] = "1"
    answer = max(answer, smallest_distance(new_s))

  # C2: Put one cow at the very left, and one cow at the middle at the biggest gap
  if s[0] == "0":
    new_s = list(s)
    new_s[0] = "1"
    answer = max(answer, put_cow_in_largest_distance(new_s))

  # C3: Put one cow at the very right, and one cow at the biggest gap
  if s[-1] == "0":
    new_s = list(s)
    new_s[-1] = "1"
    answer = max(answer, put_cow_in_largest_distance(new_s))

  # C4: Put one cow at the very left, and one cow at the very right
  if s[0] == "0" and s[-1] == "0":
    new_s = list(s)
    new_s[0], new_s[-1] = "1", "1"
    answer = max(answer, smallest_distance(new_s))

  # C5: Put one cow in the middle of the biggest gap, then put the second cow in the next biggest gap
  if distance >= 2:
    new_s = list(s)
    new_s[distance_start+distance//2] = "1"
    answer = max(answer, put_cow_in_largest_distance(new_s))
  return answer

if __name__ == "__main__":
  with open(0) as f:
    n = int(f.readline())
    s = f.readline().strip()
  print(solve(s))